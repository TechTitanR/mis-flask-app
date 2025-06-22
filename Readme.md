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
