# 🧠 Productivity Manager

A simple and responsive web application to help you organize projects and manage your task flow effectively.

---

## 🚀 Features

### ✅ Functional Requirements

- Create / update / delete **projects**
- Add / update / delete **tasks** under projects
- Prioritize tasks within a project
- Set **deadlines** for each task
- Mark tasks as **done**
- Fully authenticated user experience — every user manages **only their own** tasks and projects

---

## ⚙️ Technical Stack

| Layer            | Tech Details                                                                 |
|------------------|-------------------------------------------------------------------------------|
| **Backend**      | Python 3.12, Django 5.1                                                       |
| **Frontend**     | HTML + Bootstrap 5 + Alpine.js + HTMX + Hyperscript                          |
| **Auth**         | `django-allauth`                                                              |
| **Container**    | Docker + Docker Compose                                                       |
| **Validation**   | Client-side (via Alpine.js) and server-side (via Django Forms)                |
| **Responsiveness** | Desktop & Mobile via Bootstrap Grid system                                   |

---

## 🌐 Behavior

- Works as a **single-page web application**
- AJAX-based interactions (thanks to **HTMX**) for all CRUD operations
- Fully **SSR (Server-Side Rendered)** with Django templates
- **Modals** and **partial rendering** supported for dynamic UI updates

---

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Anderli-dev/Test_RenovateHub.git
   cd Test_RenovateHub
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a .env file in the root directory of the project.
    You can use .env.sample as a template.
    Make sure to update the values inside .env according to your local environment if needed.

5. Start the application using Docker Compose:
```bash
docker-compose up --build
```
6. Apply migrations after launch: In a new terminal (in parallel with Docker):
```bash
docker-compose exec web python manage.py migrate
```

7. The application will be available at:
- [http://localhost:8000](http://localhost:8000)

If necessary, you can also create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```
