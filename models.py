# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# Dummy Users
users = {
    'admin': {'password': 'adminpass', 'role': 'admin'},
    'employee': {'password': 'employeepass', 'role': 'employee'}
}

# User Model
class User(UserMixin):
    def __init__(self, username):
        self.id = username
        self.role = users[username]['role']

# Inventory Table
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Sales Table
class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(100), nullable=False)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    position = db.Column(db.String(100), nullable=False)
    date_joined = db.Column(db.String(100), nullable=False)
