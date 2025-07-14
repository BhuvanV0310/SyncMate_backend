# 🔐 SyncMate Backend

This is the backend for **SyncMate**, a smart matchmaking and interest-based profile system built with Flask and PostgreSQL.

---

## 🚀 Features

- User Registration
- Interest-based Matching System
- Shortlisting Users
- Auto-Seeding (100 Mock Users)
- CORS Enabled for Frontend Communication

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/BhuvanV0310/SyncMate_backend.git
cd SyncMate_backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Run the App

```bash
python run.py
```
The server will start at: http://localhost:5000

---

## Technologies Used
 - Python
 - Flask
 - SQLAlchemy
 - PostgreSQL (locally or via SQL dialect)
 - Faker (for mock data)
 - CORS (flask-cors)
