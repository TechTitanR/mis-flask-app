from flask import Flask, render_template, request, redirect, url_for, flash, send_file, make_response
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from sqlalchemy import func
from models import User, users, db, Inventory, Sales, Employee
from datetime import datetime, timedelta
import pandas as pd
from io import BytesIO
from xhtml2pdf import pisa
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Production-ready: PostgreSQL connection via env variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///mis.db')  # fallback to sqlite for dev
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    total_inventory = Inventory.query.count()
    total_sales = Sales.query.count()
    total_employees = Employee.query.count()
    total_quantity_sold = db.session.query(func.sum(Sales.quantity)).scalar() or 0

    sales_query = db.session.query(Sales.product_name, func.sum(Sales.quantity)).group_by(Sales.product_name).all()
    labels = [row[0] for row in sales_query]
    values = [row[1] for row in sales_query]

    sales_data = {'labels': labels, 'values': values}

    return render_template('dashboard.html',
                           role=current_user.role,
                           total_inventory=total_inventory,
                           total_sales=total_sales,
                           total_employees=total_employees,
                           total_quantity_sold=total_quantity_sold,
                           sales_data=sales_data)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/inventory')
@login_required
def inventory():
    items = Inventory.query.all()
    return render_template('inventory.html', items=items, role=current_user.role)

@app.route('/add_item', methods=['GET', 'POST'])
@login_required
def add_item():
    if current_user.role != 'admin':
        flash('Only admin can add items.', 'danger')
        return redirect(url_for('inventory'))

    if request.method == 'POST':
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        price = request.form['price']
        new_item = Inventory(item_name=item_name, quantity=quantity, price=price)
        db.session.add(new_item)
        db.session.commit()
        flash('Item added successfully!', 'success')
        return redirect(url_for('inventory'))

    return render_template('add_item.html')

@app.route('/edit_item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def edit_item(item_id):
    if current_user.role != 'admin':
        flash('Only admin can edit items.', 'danger')
        return redirect(url_for('inventory'))

    item = Inventory.query.get_or_404(item_id)

    if request.method == 'POST':
        item.item_name = request.form['item_name']
        item.quantity = request.form['quantity']
        item.price = request.form['price']
        db.session.commit()
        flash('Item updated successfully!', 'success')
        return redirect(url_for('inventory'))

    return render_template('edit_item.html', item=item)

@app.route('/delete_item/<int:item_id>', methods=['POST'])
@login_required
def delete_item(item_id):
    if current_user.role != 'admin':
        flash('Only admin can delete items.', 'danger')
        return redirect(url_for('inventory'))

    item = Inventory.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!', 'success')
    return redirect(url_for('inventory'))

@app.route('/sales')
@login_required
def sales():
    records = Sales.query.all()
    return render_template('sales.html', records=records, role=current_user.role)

@app.route('/add_sale', methods=['GET', 'POST'])
@login_required
def add_sale():
    if request.method == 'POST':
        product_name = request.form['product_name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        total_price = quantity * price
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sale = Sales(product_name=product_name, quantity=quantity, total_price=total_price, date=date)
        db.session.add(sale)
        db.session.commit()
        flash('Sale recorded!', 'success')
        return redirect(url_for('sales'))
    return render_template('add_sale.html')

# Employee routes
@app.route('/employees')
@login_required
def employees():
    all_employees = Employee.query.all()
    return render_template('employees.html', employees=all_employees, role=current_user.role)

@app.route('/add_employee', methods=['GET', 'POST'])
@login_required
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        position = request.form['position']
        date_joined = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_emp = Employee(name=name, email=email, position=position, date_joined=date_joined)
        db.session.add(new_emp)
        db.session.commit()
        flash('Employee registered successfully!', 'success')
        return redirect(url_for('employees'))

    return render_template('add_employee.html')

# Export Employee Excel
@app.route('/export/employees/excel')
@login_required
def export_employees_excel():
    employees = Employee.query.all()
    data = [{
        'ID': emp.id,
        'Name': emp.name,
        'Email': emp.email,
        'Position': emp.position,
        'Date Joined': emp.date_joined
    } for emp in employees]

    df = pd.DataFrame(data)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Employees')
    output.seek(0)
    return send_file(output, download_name="employees.xlsx", as_attachment=True)

# Export Employee PDF
@app.route('/export/employees/pdf')
@login_required
def export_employees_pdf():
    employees = Employee.query.all()
    html = render_template('employee_pdf_template.html', employees=employees)

    response = make_response()
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=employees.pdf'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return 'PDF generation failed'
    return response

# Weekly Report Generation (PDF/Excel)
@app.route('/download_report/<report_type>')
@login_required
def download_report(report_type):
    from_date = datetime.now() - timedelta(days=7)  # last 7 days
    sales = Sales.query.filter(Sales.date >= from_date.strftime("%Y-%m-%d %H:%M:%S")).all()

    data = [{
        'ID': sale.id,
        'Product Name': sale.product_name,
        'Quantity': sale.quantity,
        'Total Price': sale.total_price,
        'Date': sale.date
    } for sale in sales]

    df = pd.DataFrame(data)

    if report_type == 'excel':
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Weekly Sales')
        output.seek(0)
        return send_file(output, download_name='weekly_sales_report.xlsx', as_attachment=True)

    elif report_type == 'pdf':
        output = BytesIO()
        c = canvas.Canvas(output, pagesize=letter)
        width, height = letter
        y = height - 40
        c.setFont("Helvetica", 12)
        c.drawString(30, y, "Weekly Sales Report")

        y -= 30
        for index, row in df.iterrows():
            c.drawString(30, y, f"{row['ID']}: {row['Product Name']} | Qty: {row['Quantity']} | ₹{row['Total Price']} | {row['Date']}")
            y -= 20
            if y < 40:
                c.showPage()
                y = height - 40

        c.save()
        output.seek(0)
        return send_file(output, download_name='weekly_sales_report.pdf', as_attachment=True)

    else:
        flash('Invalid report type!', 'danger')
        return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
