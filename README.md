<<<<<<< HEAD
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
=======
# 🚀 AskHub

> **Ask Questions. Share Knowledge. Build a Community.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 About

**AskHub** is a full-stack Question & Answer web application inspired by community discussion platforms where users can ask questions, share answers, and learn from each other.

The main goal of this project was not just to build another website, but to understand how real-world web applications work behind the scenes.

From user authentication to database management, every feature was developed to gain hands-on experience with backend development using **Flask** and **MySQL** while keeping the user experience clean and simple.

Whether you're a beginner exploring Flask or someone interested in how a discussion platform works, AskHub is a great project to understand the fundamentals of full-stack web development.

---

# ✨ Features

- 👤 User Registration
- 🔐 Secure Login & Logout
- 🔒 Password Hashing using bcrypt
- ❓ Ask Questions
- 💬 Post Answers
- 📋 Browse Questions
- 🗄️ MySQL Database Integration
- ⚡ Session-Based Authentication
- 🎨 Clean & Responsive Interface
- 🚀 Lightweight Flask Backend

---

# 🛡️ Security

Security was one of the important aspects considered while building AskHub.

Instead of storing passwords in plain text, **every password is securely hashed using bcrypt** before it is saved into the database.

This means that even if someone gains access to the database, they cannot see the original passwords of users.

### Security Features

- 🔒 Passwords are hashed using bcrypt
- 🚫 Plain text passwords are never stored
- 👤 Secure session-based authentication
- ✅ Password verification using bcrypt
- 🛡️ Better protection against password theft
- 
---

# 🛠️ Technologies Used

| Technology |         Purposes         |
|------------|--------------------------|
| Python     | Backend Programming      |
| Flask      | Web Framework            |
| MySQL      | Database                 |
| bcrypt     | Password Security        |
| HTML5      | Page Structure           |
| CSS3       | Styling                  |
| JavaScript | Client-side Interactions |

---

# 📂 Project Structure

```
>>>>>>> 7d5452711da3e15dc7fdbebf700bcd8d2a58416f
AskHub/
│
├── static/
│   ├── css/
<<<<<<< HEAD
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── templates/
│   ├── base.html
=======
│   ├── js/
│   └── images/
│
├── templates/
>>>>>>> 7d5452711da3e15dc7fdbebf700bcd8d2a58416f
│   ├── login.html
│   ├── signup.html
│   ├── home.html
│   ├── ask.html
<<<<<<< HEAD
│   ├── question.html
│   └── profile.html
│
├── app.py
├── config.py
=======
│   ├── profile.html
│   └── ...
│
├── app.py
>>>>>>> 7d5452711da3e15dc7fdbebf700bcd8d2a58416f
├── schema.sql
├── requirements.txt
└── README.md
```

---

<<<<<<< HEAD
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
=======
# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/rajanmaurya12012008/AskHub.git
```

Move into the project folder

```bash
cd AskHub
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure MySQL

Create a database

```sql
CREATE DATABASE askhub;
```

Import the database schema

```sql
SOURCE schema.sql;
```

Update your MySQL username and password inside `app.py`.

---

## 5️⃣ Run the Application

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

# 💡 Why I Built This Project

As a Computer Science student, I wanted to move beyond small coding exercises and build something closer to a real-world application.

AskHub gave me the opportunity to understand how authentication, databases, sessions, routing, and frontend-backend communication work together.

This project also helped me improve my problem-solving skills and gain practical experience in full-stack development.

Building AskHub was a valuable learning experience that strengthened my understanding of Flask, MySQL, and web application architecture.

---

# 📚 What I Learned

While building AskHub, I gained practical experience with:

- Flask Routing
- User Authentication
- Password Hashing with bcrypt
- Session Management
- CRUD Operations
- MySQL Database Design
- Template Rendering
- HTML, CSS & JavaScript Integration
- Backend Development
- Debugging & Problem Solving

---

# ⭐ Key Highlights

- Full-stack Flask Web Application
- Secure Authentication
- Session-Based Login System
- MySQL Database Integration
- Clean Project Structure
- Beginner-Friendly Codebase
- Easy to Extend with New Features
- Built with Scalability in Mind

---

# 🚀 Future Improvements

Some features I plan to add in future versions:

- ❤️ Like & Upvote System
- 💬 Comments & Replies
- 🏷️ Tags & Categories
- 🔍 Search Questions
- 👤 User Profiles
- 📸 Profile Picture Upload
- 📧 Email Verification
- 🔑 Forgot Password
- 🔔 Notifications
- 🌙 Dark Mode
- 📱 Improved Mobile Responsiveness
- 🤖 AI-powered Answer Suggestions
- 📊 Admin Dashboard

---

# 🤝 Contributing

Contributions, ideas, and suggestions are always welcome.

If you'd like to improve AskHub:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

Every contribution is appreciated.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Developer

### Rajan Maurya

**B.Tech CSE (AI & Machine Learning)**

I'm passionate about Artificial Intelligence, Machine Learning, Python, and Full-Stack Development.

I enjoy building projects that solve real-world problems while continuously learning new technologies.

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub. It motivates me to keep building and sharing more projects with the community.

---

### ⭐ Thank you for visiting AskHub!

*"Great communities are built when people ask questions without hesitation and share knowledge without limits."*
>>>>>>> 7d5452711da3e15dc7fdbebf700bcd8d2a58416f
