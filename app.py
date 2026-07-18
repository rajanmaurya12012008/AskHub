from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from functools import wraps
import pymysql
import bcrypt
import os
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Load configurations from config.py
app.config.from_object('config.Config')

# -------------------------------------------------------------
# DATABASE CONNECTION UTILITIES (Flask Context Managed)
# -------------------------------------------------------------

def get_db():
    """
    Returns a MySQL database connection, caching copy in the Flask context 'g'.
    This avoids creating multiple client connections per web request.
    """
    if 'db' not in g:
        try:
            g.db = pymysql.connect(
                host=app.config['DB_HOST'],
                user=app.config['DB_USER'],
                password=app.config['DB_PASSWORD'],
                database=app.config['DB_NAME'],
                port=app.config['DB_PORT'],
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True # Automatically save changes to the database
            )
        except pymysql.MySQLError as e:
            # Helpful debugging message if database isn't running or credentials are wrong
            print(f"Database Connection Error: {e}")
            raise e
    return g.db

@app.teardown_appcontext
def close_db(error):
    """
    Closes the connection when the request finishes, preventing connection leaks.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()


# -------------------------------------------------------------
# JINJA CUSTOM FILTERS & UTILS
# -------------------------------------------------------------

@app.template_filter('uppercase')
def uppercase_filter(value):
    """Custom template filter to capitalize characters (e.g. for user initials)."""
    return value.upper() if value else ''


# -------------------------------------------------------------
# ROUTE PROTECTION DECORATORS
# -------------------------------------------------------------

def login_required(f):
    """
    Decorator to prevent unauthenticated users from page routes (like posting questions).
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("You must be logged in to complete this action.", "danger")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# -------------------------------------------------------------
# CORE APPLICATION ROUTES
# -------------------------------------------------------------

@app.route('/')
def home():
    """
    Home page feed. Pulls all questions (latest first) along with metrics 
    like total answers and author's details to build feed and sidebar statistics.
    """
    db = get_db()
    cursor = db.cursor()
    
    # 1. Fetch questions feed
    questions_query = """
        SELECT q.id, q.title, q.description, q.created_at, q.user_id, u.username,
               (SELECT COUNT(*) FROM answers WHERE question_id = q.id) AS answer_count
        FROM questions q
        JOIN users u ON q.user_id = u.id
        ORDER BY q.created_at DESC
    """
    cursor.execute(questions_query)
    questions = cursor.fetchall()

    # 2. Fetch sidebar dashboard metrics
    cursor.execute("SELECT COUNT(*) AS total FROM users")
    total_users = cursor.fetchone()['total']

    cursor.execute("SELECT COUNT(*) AS total FROM questions")
    total_questions = cursor.fetchone()['total']

    cursor.execute("SELECT COUNT(*) AS total FROM answers")
    total_answers = cursor.fetchone()['total']

    stats = {
        'total_users': total_users,
        'total_questions': total_questions,
        'total_answers': total_answers
    }
    
    return render_template('home.html', questions=questions, stats=stats)


# -------------------------------------------------------------
# USER AUTHENTICATION SYSTEM
# -------------------------------------------------------------

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Sign Up handler. Performs duplicate checking, encodes password via bcrypt,
    and creates new users in the database.
    """
    if 'user_id' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # Server-side validation
        if not username or not email or not password:
            flash("All fields are required.", "danger")
            return render_template('signup.html')

        if len(password) < 6:
            flash("Password must be at least 6 characters long.", "danger")
            return render_template('signup.html')

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return render_template('signup.html')

        db = get_db()
        cursor = db.cursor()

        # Check if Username or Email is already registered
        cursor.execute("SELECT id FROM users WHERE username = %s OR email = %s", (username, email))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("Username or Email is already registered.", "danger")
            return render_template('signup.html')

        # Secure password using bcrypt hashing
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Insert new user using parameterized queries (SQL Injection Safe)
        insert_query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (username, email, hashed_password))
        
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log In handler. Looks up username or email and validates hashed credentials.
    """
    if 'user_id' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        credential = request.form.get('credential', '').strip()
        password = request.form.get('password', '')

        if not credential or not password:
            flash("Both fields are required.", "danger")
            return render_template('login.html')

        db = get_db()
        cursor = db.cursor()

        # Find user by username OR email
        find_query = "SELECT * FROM users WHERE username = %s OR email = %s"
        cursor.execute(find_query, (credential, credential))
        user = cursor.fetchone()

        # Validate existence & hashed password check
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            # Store primary user identity in session dict
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['email'] = user['email']
            
            flash(f"Welcome back, {user['username']}!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid username/email or password.", "danger")
            return render_template('login.html')

    return render_template('login.html')


@app.route('/logout')
def logout():
    """
    Logs current user out, clearing the HTTP session variables.
    """
    session.clear()
    flash("You have been successfully logged out.", "success")
    return redirect(url_for('home'))


# -------------------------------------------------------------
# QUESTIONS & ANSWERS LOGIC
# -------------------------------------------------------------

@app.route('/ask', methods=['GET', 'POST'])
@login_required
def ask():
    """
    Allows authenticated users to post new questions with a title and description.
    """
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()

        # Basic validations
        if len(title) < 10:
            flash("Question title must be at least 10 characters long.", "danger")
            return render_template('ask.html')

        if len(description) < 20:
            flash("Question details must be at least 20 character descriptions.", "danger")
            return render_template('ask.html')

        db = get_db()
        cursor = db.cursor()

        # Insert question securely
        insert_query = "INSERT INTO questions (title, description, user_id) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (title, description, session['user_id']))

        flash("Your question has been posted successfully!", "success")
        return redirect(url_for('home'))

    return render_template('ask.html')


@app.route('/question/<int:question_id>')
def question_detail(question_id):
    """
    Displays the details of a single question and list of associated answers.
    """
    db = get_db()
    cursor = db.cursor()

    # Get Single Question details with author name
    question_query = """
        SELECT q.id, q.title, q.description, q.created_at, q.user_id, u.username
        FROM questions q
        JOIN users u ON q.user_id = u.id
        WHERE q.id = %s
    """
    cursor.execute(question_query, (question_id,))
    question = cursor.fetchone()

    if not question:
        flash("Oops! That thread was not found.", "danger")
        return redirect(url_for('home'))

    # Get Answers to this question
    answers_query = """
        SELECT a.id, a.content, a.created_at, a.user_id, u.username
        FROM answers a
        JOIN users u ON a.user_id = u.id
        WHERE a.question_id = %s
        ORDER BY a.created_at ASC
    """
    cursor.execute(answers_query, (question_id,))
    answers = cursor.fetchall()

    return render_template('question.html', question=question, answers=answers)


@app.route('/question/<int:question_id>/answer', methods=['POST'])
@login_required
def submit_answer(question_id):
    """
    Submits an answer associated with a particular question.
    """
    content = request.form.get('content', '').strip()

    if len(content) < 5:
        flash("Your answer must contain at least 5 character inputs.", "danger")
        return redirect(url_for('question_detail', question_id=question_id))

    db = get_db()
    cursor = db.cursor()

    # Verify if the question actually exists
    cursor.execute("SELECT id FROM questions WHERE id = %s", (question_id,))
    if not cursor.fetchone():
        flash("Question thread details invalid.", "danger")
        return redirect(url_for('home'))

    # Insert into Answers table
    insert_query = "INSERT INTO answers (content, question_id, user_id) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (content, question_id, session['user_id']))

    flash("Answer submitted successfully!", "success")
    return redirect(url_for('question_detail', question_id=question_id))


# -------------------------------------------------------------
# USER PROFILE INTERFACES
# -------------------------------------------------------------

@app.route('/profile/<int:user_id>')
def profile(user_id):
    """
    Renders user profile dashboard containing stats and listings of 
    questions and answers authored by this user.
    """
    db = get_db()
    cursor = db.cursor()

    # Look up User Profile credentials
    cursor.execute("SELECT id, username, email, created_at FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()

    if not user:
        flash("User profile details do not exist.", "danger")
        return redirect(url_for('home'))

    # Fetch all Questions asked by this user
    questions_query = """
        SELECT q.id, q.title, q.description, q.created_at,
               (SELECT COUNT(*) FROM answers WHERE question_id = q.id) AS answer_count
        FROM questions q
        WHERE q.user_id = %s
        ORDER BY q.created_at DESC
    """
    cursor.execute(questions_query, (user_id,))
    questions = cursor.fetchall()

    # Fetch all Answers given by this user with details of target question title
    answers_query = """
        SELECT a.id, a.content, a.created_at, a.question_id, q.title AS question_title
        FROM answers a
        JOIN questions q ON a.question_id = q.id
        WHERE a.user_id = %s
        ORDER BY a.created_at DESC
    """
    cursor.execute(answers_query, (user_id,))
    answers = cursor.fetchall()

    return render_template('profile.html', user=user, questions=questions, answers=answers)


# -------------------------------------------------------------
# STARTING APPLICATION
# -------------------------------------------------------------

if __name__ == '__main__':
    # Start the Flask environment local server with debug support.
    # Set to False in production environments.
    app.run(host='0.0.0.0', port=5000, debug=True)
