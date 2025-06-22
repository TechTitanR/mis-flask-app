# 📊 MIS Flask App

A simple and customizable **Management Information System (MIS)** built using **Flask**, **SQLAlchemy**, **Bootstrap**, and **Chart.js**.  
Supports features like Inventory Management, Sales Tracking, Employee Registration, Auto-generated PDF/Excel Reports, and Dark Mode.

---

## 🚀 Features

- 🔑 **User Authentication (Login/Logout)**
- 🗃️ **Inventory Management** (Add, Edit, Delete Items)
- 💰 **Sales Records Management** (Add Sales)
- 👥 **Employee Registration & Export to PDF/Excel**
- 📈 **Dynamic Dashboard** with Sales Chart (Chart.js)
- 📑 **Auto-generated Weekly Sales Report** (Download as PDF/Excel)
- 🌗 **Dark Mode Toggle** (Persisted across pages)
- ⚙️ **Role-based access control** (Admin/User)
- 🏭 **PostgreSQL-ready for production (Render deployment)**

---

## 💻 Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, Bootstrap 5, Chart.js
- **Database**: SQLite (Dev) / PostgreSQL (Prod)
- **ORM**: SQLAlchemy
- **Authentication**: Flask-Login
- **PDF/Excel Export**: ReportLab, xhtml2pdf, pandas, xlsxwriter

---

## 🏗️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/mis-flask-app.git
cd mis-flask-app
```

---

2. **Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

---

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

---

4. **Set Up Database**

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

---

5. **Run the Application (Dev Mode)**

```bash
flask run
python app.py
```

---

6. **Open in Browser**

```bash
http://127.0.0.1:5000/
```

---

## 📝 Environment Variables (for Render/PostgreSQL)
Create .env file:

```bash
DATABASE_URL=postgresql://username:password@hostname:port/databasename
SECRET_KEY=your_secret_key
```

Update app.py to use:

```bash
import os
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///mis.db')
app.secret_key = os.getenv('SECRET_KEY', 'supersecretkey')
```

---

## 📄 Auto-Generated Reports
- Weekly Sales Reports can be downloaded as:
-- 📝 Excel (XLSX)
--📄 PDF

-Location: Dashboard → Bottom Right Buttons

---

## 🌍 Live Demo 

---

## 🖼️ Screenshots

---

## 🤝 Contributing
- Pull requests are welcome. For major changes, open an issue first.

---

## 📃 License
- MIT License

---

## ✨ Developed By
Rishi Bakliwal 🚀
rishibakliwaljain@gmail.com
