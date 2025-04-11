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

```bash
# Clone repository
git clone https://github.com/yourname/productivity-manager.git
cd productivity-manager

# Set environment variables
cp .env.example .env  # edit values as needed

# Run with Docker Compose
docker-compose up --build
