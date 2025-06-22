# 📊 MIS Flask App

A simple and customizable **Management Information System (MIS)** built using **Flask**, **SQLAlchemy**, **Bootstrap**, and **Chart.js**.  
Supports features like Inventory Management, Sales Tracking, Employee Registration, Auto-generated PDF/Excel Reports, and Dark Mode.

---

## 🚀 Live Demo
🔗 [https://mis-flask-app.onrender.com](https://mis-flask-app.onrender.com)

---

## 📂 Project Structure

```plaintext
mis-flask-app/
│
├── app.py # Main Flask application
├── models.py # SQLAlchemy models (Inventory, Sales, Employee)
├── requirements.txt # All Python dependencies
├── render.yaml # Render deployment config
├── .env # Environment variables (excluded via .gitignore)
├── Readme.md # Project Documentation
├── LICENSE # License file
│
├── static/
│ └── css/
│ └── style.css # Custom CSS styles
│
├── templates/
│ ├── login.html
│ ├── dashboard.html
│ ├── inventory.html
│ ├── add_item.html
│ ├── edit_item.html
│ ├── sales.html
│ ├── add_sale.html
│ ├── employees.html
│ ├── add_employee.html
│ └── employee_pdf_template.html
│
└── mis.db # SQLite DB (used for local development only)

```

---

## 💻 Tech Stack

- **Backend**: Flask, Flask-Login, Flask-SQLAlchemy
- **Database**: PostgreSQL (for production), SQLite (local dev)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Deployment**: Render.com
- **PDF/Excel Generation**: `xhtml2pdf`, `openpyxl`, `xlsxwriter`, `reportlab`

---

## ✨ Features

- 🔐 **User Authentication (Login, Logout)**
- 📦 **Inventory Management** (Add/Edit/Delete Products)
- 💰 **Sales Management** (Record, Track Sales)
- 👨‍💼 **Employee Management** (Register, Export Employees as PDF/Excel)
- 📈 **Dashboard with Chart.js Visualizations**
- 📋 **Auto-Generated Weekly Sales Reports (PDF/Excel)**
- 🖥️ **Responsive UI with Bootstrap 5**
- ☁️ **Deployed on Render with PostgreSQL**

---

## ⚙️ Setup Instructions (Local)

1. **Clone this repo:**
```bash
git clone https://github.com/TechTitanR/mis-flask-app.git
cd mis-flask-app
```

2. **Create & activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up .env file:**
```bash
DATABASE_URL=postgresql://user:password@host:port/dbname
SECRET_KEY=your_secret_key
```

5. **Run the app:**
```bash
flask run
```

6. **Open in Browser:**
```bash
http://127.0.0.1:5000/
```

---

## ☁️ Deployment (Render)
- Auto-deployed via Render.com using render.yaml & PostgreSQL database.
- Production server runs via Gunicorn.

---

## 📄 Auto-Generated Reports
- Weekly Sales Reports can be downloaded as:
- A. 📝 Excel (XLSX)
- B. 📄 PDF

- Location: Dashboard → Bottom Right Buttons

---

## 📝 License
- This project is licensed under the MIT License.

---

## 🤝 Acknowledgements
- Flask
- Render
- Chart.js
- Bootstrap

---

## 📧 Contact
- Rishi Bakliwal 🚀 
- Email: rishibakliwaljain@gmail.com

