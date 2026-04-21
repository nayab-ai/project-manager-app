

# 📄 README.md (Project Manager App – Django)

```md id="pmr1"
# 🚀 Project Manager App (Django)

This is a simple **Project Management Web Application** built using **Django (Python)** as part of my internship Task 3.

The project helps users manage tasks and organize projects in a simple and efficient way.

---

## 📌 Project Overview

The Project Manager App allows users to:
- Create and manage projects
- Add and track tasks
- Organize work in a structured way
- Manage data through Django backend

This project is built using Django’s MVT (Model-View-Template) architecture.

---

## ✨ Features

- 📁 Create Projects  
- 📝 Add Tasks  
- 📊 Task Management System  
- 🔐 Django Admin Panel  
- 🗄️ SQLite Database Integration  
- ⚙️ Backend powered by Django  

---

## ⚙️ Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS (Django Templates)
- Database: SQLite
- Server: Django Development Server

---

## 📁 Project Structure

```

project_manager/
│
├── project_manager/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── core/
│   │       ├── home.html
│   │       ├── project.html
│   │       └── task.html
│
├── db.sqlite3
├── manage.py

````

---

## 🚀 How to Run This Project

1. Clone repository:
```bash id="run1"
git clone https://github.com/nayab-ai/project-manager-app.git
````

2. Go to project folder:

```bash id="run2"
cd project-manager-app
```

3. Install Django:

```bash id="run3"
pip install django
```

4. Run migrations:

```bash id="run4"
python manage.py migrate
```

5. Start server:

```bash id="run5"
python manage.py runserver
```

6. Open in browser:

```id="run6"
http://127.0.0.1:8000/
```

---

## 🎯 What I Learned

* Django project structure
* CRUD operations (Create, Read, Update, Delete)
* Backend development concepts
* URL routing and views
* Database integration with SQLite
* Project organization system

---

## 📌 Internship Task

This project is completed as **Task (Project Manager App)** under the **CodeAlpha Internship Program**.

---

## 📬 Feedback

Suggestions and improvements are always welcome!

---
