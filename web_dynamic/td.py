#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""

from models.user import User
from models.task import Task
from models.admin import Admin
from flask import Flask, abort, flash, redirect, render_template, request, jsonify, session, url_for
from models import storage
from flask_cors import CORS
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'os.urandom(32)'  # Replace with your secret key
cors = CORS(app, resources={r"*": {"origins": "0.0.0.0"}})


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


@app.route('/login', strict_slashes=False)
def login():
    """The homepage of the application."""
    return render_template('login.html')


def order_task_by_priority(list_of_task):
    low = []
    medium = []
    high = []
    for tsk in list_of_task:
        if tsk.priority == 'low':
            low.append(tsk)
        elif tsk.priority == 'medium':
            medium.append(tsk)
        else :
            high.append(tsk)
    return low + medium + high


@app.route('/login/user', methods=['POST'], strict_slashes=False)
def login_user():
    """Render the Login page."""
    url = "http://127.0.0.1:5200/users/verify"
    print("Debug is here")

    # Check if the request has a JSON payload
    if not request.is_json:
        return jsonify({'error': 'Invalid request format'}), 400

    # Access JSON data
    data = request.json

    if "email" not in data or "password" not in data:
        return jsonify({'error': 'Missing email or password in request'}), 400

    email = data['email']
    password = data['password']

    obj = {
        'email': email,
        'password': password
    }

    headers = {
        'Content-Type': 'application/json'
    }

    print(obj)
    response = requests.post(url, json=obj, headers=headers)
    print("Hi", response.status_code)

    if response.status_code == 201:
        # just remember, we need to render this page based on his credentials
        flash("Successfully logged in", "success")
        user_id = response.json().get('id')
        user_obj = storage.get(User, user_id)  # Assuming 'storage' is defined
        print("Login Successful")
        print(user_obj.to_dict())
        # render the success page
        return redirect(url_for('success', user_id=user_id))
        # return redirect(url_for('get_task', user_id=user_id))
    else:
        flash("Wrong email or password", "danger")
        return jsonify({"error": "Wrong email or password"}), 401


@app.route('/success', strict_slashes=False)
def success():
    """Render the success page base on the user properties"""
    user_id = request.args.get('user_id')
    user = storage.get(User, user_id)

    # Render the success page with user properties
    return render_template('success.html', user=user)


@app.route('/user/<user_id>/tasks', strict_slashes=False)
def get_task(user_id):
    """Render the tasks page."""
    user_task = order_task_by_priority(storage.get(User, user_id).task)
    user = storage.get(User, user_id)
    return render_template('task.html', tasks=user_task, user=user, user_id=user_id)


@app.route('/task', strict_slashes=False)
def task():
    """The homepage of the application."""
    return render_template('new.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
