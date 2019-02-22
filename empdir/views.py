from flask import render_template
from empdir import app

@app.route('/')
def index():
    return render_template('index.html', title="Employee Directory App")