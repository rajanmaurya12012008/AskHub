# AskHub Q&A Platform

AskHub is a community-based Question & Answer platform inspired by Quora, built for student developers to showcase basic full-stack web application development in Python Flask and MySQL. It maintains a clean, readable design using plain CSS (no structural frameworks like Bootstrap) and highlights essential concepts including secure password hashing with bcrypt, session routing guards, and database transactions.

---

## Features

### 1. User Authentication
* **Registration**: Users can sign up with a unique username, unique email address, and a secure password.
* **Secure Login**: Access validation checks and redirects authenticated members.
* **Logout**: Clears active sessions and revokes route permissions.

### 2. Home Feed
* Chronological listing of all user-submitted questions (latest first).
* Shows total answer counts and clickable links to user profiles.
* Side widget displaying direct application stats (users, questions, and replies counts).

### 3. Ask Questions
* Logged-in users can post queries detailing titles (minimum 10 chars) and detailed descriptions (minimum 20 chars).
* Anti-duplication, client validation layers, and server safety processing.

### 4. Direct Q&A Thread Discussion
* Read the full query header details and date.
* View answers posted by community members chronologically.
* Write a helpful reply via a form (requires active login session).

### 5. Profile Dashboards
* Highlights member statistics (number of asked questions and answered queries).
* Switch content views seamlessly between "Questions Asked" and "Answers Given" tabs using vanilla JS.

### 6. Built-in Security
* **Bcrypt Password Protection**: Passwords are encrypted using salted bcrypt hashing and never stored in plain text.
* **SQL Injection Mitigation**: All database operations use parameterized queries (`%s`).
* **Route Protection**: Decorator blocks non-authenticated visitors from key operations like posting questions and replies.

---

## Technologies Used
* **Backend**: Python (Flask)
* **Database**: MySQL (PyMySQL client connection mapping)
* **Frontend**: HTML5, Vanilla JavaScript, Plain CSS3 (Outfit & Plus Jakarta Sans typography)
* **Encryption**: `bcrypt` (python-bcrypt integration)

---

## Folder Structure

```text
AskHub/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── home.html
│   ├── ask.html
│   ├── question.html
│   └── profile.html
│
├── app.py
├── config.py
├── schema.sql
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Prerequisites
Ensure you have the following installed:
* Python 3.8 or higher.
* MySQL Server (e.g. through XAMPP, Laragon, or standalone community server installer).

### 2. Clone and Place Files
Make sure all repository files (or folder structures) reside inside your target server path (e.g., `d:\askhubgravity`).

### 3. Setup Python Virtual Environment
Open PowerShell inside your directory and run:
```powershell
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 5. Set Up MySQL Database
1. Open your local MySQL Command Line Client or tool (phpMyAdmin, DBeaver, HeidiSQL).
2. Create the target database or execute the schema script directly:
   ```sql
   SOURCE d:/askhubgravity/schema.sql;
   ```
   *Alternative: Copy and execute the contents of the `schema.sql` file in your database query editor.*

### 6. Adjust config.py Settings
Edit database settings in `config.py` if they differ from standard:
* `DB_HOST`: e.g. `'localhost'`
* `DB_USER`: e.g. `'root'`
* `DB_PASSWORD`: e.g. `''` (blank database password)
* `DB_NAME`: e.g. `'askhub'`

### 7. Run the Application
Start the development server using:
```powershell
python app.py
```
Open a browser and navigate to: `http://127.0.0.1:5000/`

---

## Future Improvements
* **Question Search**: Add a global search bar utilizing SQL `LIKE` selectors.
* **Upvotes & Downvotes**: Implement system metrics to gauge answers value.
* **Categories / Tags**: Permit categorizing queries (e.g., Programming, Science, Campus).
* **Avatar Uploads**: Let users upload custom image avatars for their profile card.
