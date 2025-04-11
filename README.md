🧠 Task manager
A simple and responsive web application to help you organize projects and manage your task flow effectively.

🚀 Features
✅ Functional Requirements
Create / update / delete projects

Add / update / delete tasks under projects

Prioritize tasks within a project

Set deadlines for each task

Mark tasks as done

Fully authenticated user experience — every user manages only their own tasks and projects

⚙️ Technical Stack
Layer	Tech Details
Backend	Python 3.12, Django 5.1
Frontend	HTML + Bootstrap 5 + HTMX
Auth	django-allauth
Container	Docker + Docker Compose
Responsiveness	Desktop & Mobile via Bootstrap Grid system
🌐 Behavior
Works as a single-page web application

AJAX-based interactions (thanks to HTMX) for all CRUD operations

Fully SSR (Server-Side Rendered) with Django templates

Modals and partial rendering supported for dynamic UI updates

🛠️ Setup Instructions
bash
Копіювати
Редагувати
# Clone repository
git clone https://github.com/yourname/productivity-manager.git
cd productivity-manager

# Set environment variables
cp .env.example .env  # edit values as needed

# Run with Docker Compose
docker-compose up --build
✅ Tests
Run all automated tests:

bash
docker-compose run web pytest
Test types:

test_models.py – Model logic and constraints

test_views.py – View-level integration

test_htmx.py – HTMX dynamic rendering and swapping

test_forms.py – Form validation logic

test_permissions.py – Access control and authorization