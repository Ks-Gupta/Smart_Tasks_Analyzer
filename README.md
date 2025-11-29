
---

# 🧠 Smart Task Analyzer

A smart AI-powered system that analyzes user tasks and provides structured insights, scoring, and recommendations using a backend powered by Django and a simple frontend interface.

---

## 🚀 Features

* **Task Scoring System** – Automatically score tasks based on complexity, impact, and priority
* **REST API Backend** (Django + DRF) for task submissions
* **Frontend UI** for interacting with the system
* **Database Storage** using SQLite
* **Modular architecture** for easy modifications and improvements

---

## 🏗️ Tech Stack

### **Backend**

* Django
* Django REST Framework
* SQLite3

### **Frontend**

* HTML, CSS, JavaScript

### **Tools**

* Git & GitHub
* Python
* REST APIs

---

## 📁 Project Structure

```
Smart_Task_Analyzer/
│── task-analyzer/
│   ├── backend/
│   │   ├── manage.py
│   │   ├── requirements.txt
│   │   ├── task_analyzer/
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   ├── wsgi.py
│   │   ├── tasks/
│   │       ├── models.py
│   │       ├── serializers.py
│   │       ├── views.py
│   │       ├── scoring.py
│   ├── frontend/
│       ├── index.html
│       ├── script.js
│       ├── style.css
│── README.md
```

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/Ks-Gupta/Smart_Tasks_Analyzer.git
cd Smart_Tasks_Analyzer/task-analyzer/backend
```

---

### **2️⃣ Create a virtual environment**

```bash
python3 -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

---

### **3️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

---

### **4️⃣ Run database migrations**

```bash
python manage.py migrate
```

---

### **5️⃣ Start the backend server**

```bash
python manage.py runserver
```

Backend will run at:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### **6️⃣ Open the frontend**

Simply open:

```
task-analyzer/frontend/index.html
```

in your browser.

---

## 📌 API Endpoints (Important)

| Method | Endpoint         | Description               |
| ------ | ---------------- | ------------------------- |
| POST   | `/tasks/submit/` | Submit a task for scoring |
| GET    | `/tasks/`        | Get all tasks             |
| GET    | `/tasks/<id>/`   | Get task details          |

---

## 🎯 Future Improvements

* Add user authentication
* Add LLM-powered task description analysis
* Improve scoring algorithm
* Add a React/Next.js frontend
* Deploy to cloud (Render, Railway, AWS)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 📄 License

This project is open-source and available under the **MIT License**.

---
