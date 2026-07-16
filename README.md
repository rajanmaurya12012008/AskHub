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
AskHub/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── home.html
│   ├── ask.html
│   ├── profile.html
│   └── ...
│
├── app.py
├── schema.sql
├── requirements.txt
└── README.md
```

---

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
