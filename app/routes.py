from flask import redirect, render_template, request, url_for, flash
from app import app

@app.route('/')
def index():
    return render_template('index.html')