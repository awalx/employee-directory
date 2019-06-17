from flask import render_template
from empdir import app, db
from empdir.models import Employees

@app.route('/')
def index():
    employees = Employees.query.all()
    return render_template('index.html', title="Employee Directory App", employees=employees)