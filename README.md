# 
readme_content = """# Django To-Do List (CBVs)

A simple and elegant **To-Do List** web application built with **Django** using **Class-Based Views (CBVs)**. 
This project allows users to efficiently manage tasks with authentication, clean Bootstrap UI, and responsive design.

---

## 🚀 Features

- **User Authentication:** Login & Logout functionality
- **Task Management:** Create, Update, and Delete tasks
- **User-Specific Tasks:** Each user sees only their own tasks
- **Responsive Design:** Bootstrap 5 ensures mobile-friendly layout
- **Elegant Forms:** Dynamic buttons for Add / Update Task
- **Confirmation Prompts:** For safe deletion of tasks
- **Card Layout:** Tasks displayed in cards with shadows and spacing

---

## 🛠 Tech Stack

- **Backend:** Python 3.12, Django 5.2
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Tools:** VSCode (with Django Template extension)
- **Database:** SQLite (default Django DB)

---

## 📸 Screenshots

![alt text](Django_ToDo_CBVs.jpg)

![Django_ToDo_CBVs](https://github.com/user-attachments/assets/9c8871e0-4d4c-4e38-afb0-3e4fcb6da244)

---

## ⚙ Installation & Run

1. **Clone the repository:**

```bash
git clone https://github.com/bpourshojae/Django_ToDo_CBVs.git
cd Django_ToDo_CBVs

2. **Create a virtual environment and activate it:**

python -m venv venv
.\venv\Scripts\activate    # Windows
source venv/bin/activate   # Mac/Linux

3. **Install dependencies:**
pip install -r requirements.txt

4. **Apply Migrations:**
python manage.py venv venv

5. **Run the development server:**
python manage.py runserver

6. **Visit in Browser**
http://127.0.0.1:8000/

📝 Usage

Login: Enter your credentials to access your tasks

Add Task: Use the form to add new tasks

Update Task: Edit task details by clicking the Update button

Delete Task: Click Delete and confirm to remove tasks

View Tasks: Tasks are displayed in a responsive card layout

Django_ToDo_CBVs/
│
├─ basic_app/           # Django app
│  ├─ templates/        # HTML templates
│  ├─ models.py
│  ├─ views.py
│  └─ ...
│
├─ Django_ToDo_CBVs/    # Project folder
│  ├─ settings.py
│  └─ ...
│
├─ manage.py
└─ requirements.txt
