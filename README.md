## # TaskFlow

A simple, user-focused task management web application built with Django. TaskFlow helps users organize their daily work, manage deadlines, track task completion, and stay on top of their responsibilities.

**Live Demo:** https://taskflow-qhe7.onrender.com

---

## Features

- **User Authentication** — User registration, login, and logout.
- **Task Management (CRUD)** — Create, view, edit, and delete tasks.
- **User-Specific Tasks** — Each user can access and manage only their own tasks.
- **Task Status** — Mark tasks as completed or pending.
- **Priority Management** — Organize tasks according to priority.
- **Due Dates** — Assign deadlines to tasks.
- **Overdue Tracking** — Identify overdue tasks.
- **Filtering & Sorting** — Organize tasks based on different criteria.
- **Form Validation** — Handle invalid input appropriately.
- **Responsive Interface** — Clean interface with HTML, CSS, and JavaScript.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Django | Web framework |
| SQLite | Database (development/current deployment) |
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Frontend interactions |
| Gunicorn | Production WSGI server |
| WhiteNoise | Static file serving |
| Git & GitHub | Version control |
| Render | Deployment and hosting |

---

## Project Structure

```text
TaskFlow/
│
├── task_manager/            # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── taskmanager_app/         # Main application
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/                # HTML templates
├── static/                   # CSS, JS, and other static assets
├── staticfiles/               # Collected static files
│
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/DebajyotiBindu/TaskFlow.git
cd TaskFlow
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Replace `your-secret-key` with your own Django secret key.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the application at:

http://127.0.0.1:8000/

---

## Deployment

TaskFlow is deployed on **Render** using Gunicorn.

The deployment process includes:

- Installing dependencies from `requirements.txt`.
- Collecting static files using Django's `collectstatic`.
- Applying database migrations.
- Starting the application using Gunicorn.
- Serving static assets using WhiteNoise.

### Production Commands

**Build Command:**

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

**Start Command:**

```bash
python manage.py migrate && gunicorn task_manager.wsgi:application
```

Production environment variables are configured through the Render dashboard.

---

## Security

- Passwords are managed through Django's authentication system.
- Authenticated users can access their own tasks.
- Task queries are restricted to the logged-in user.
- Sensitive configuration is managed through environment variables.
- Debug mode is disabled in production.

---

## Future Improvements

- Persistent PostgreSQL database for production.
- Improved dashboard analytics.
- Additional task organization features.
- Further UI/UX improvements.

---


*Built as a hands-on project to learn Django backend development, authentication, database management, and deployment.*
