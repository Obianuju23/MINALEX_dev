#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""

from models.user import User
from models.task import Task
from models.admin import Admin
from flask import Flask, render_template, request, jsonify
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the database at the end of the request."""
    storage.close()


@app.route('/', strict_slashes=False)
def index():
    """The homepage of the application."""
    return render_template('index.html')

@app.route('/home', strict_slashes=False)
def home():
    """The homepage of the application."""
    return render_template('index.html')


@app.route('/signup', strict_slashes=False)
def signup():
    """The homepage of the application."""
    return render_template('login_register.html')


@app.route('/login', strict_slashes=False)
def login():
    """The homepage of the application."""
    return render_template('login.html')


@app.route('/task', strict_slashes=False)
def task():
    """The homepage of the application."""
    return render_template('task.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
