#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""

from models.user import User
from models.task import Task
from flask import Flask, abort, flash, redirect, render_template, request, jsonify, session, url_for
from models import storage
from flask_cors import CORS
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'os.urandom(32)'  # Replace with your secret key
CORS(app)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the database at the end of the request."""
    storage.close()


@app.route('/home', strict_slashes=False)
@app.route('/', strict_slashes=False)
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
    # Check if the request has a JSON payload
    # if not request.is_json:
    #     return jsonify({'error': 'Invalid request format'}), 400
    
    # Get the email and password from the request payload
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({'error': 'Password is required'}), 400
    
    obj = {
        'email': email,
        'password': password
    }
    # set headers
    headers = {
        'Content-Type': 'application/json'
    }

    url = "http://127.0.0.1:5200/user/verify"
    response = requests.post(url, json=obj, headers=headers)

    if response.status_code == 201:
        # just remember, we need to render this page based on his credentials
        flash("Successfully logged in", "success")
        user_id = response.json().get('id')
        user_obj = storage.get(User, user_id)  # Assuming 'storage' is defined
        # render the success page
        return redirect(url_for('success', user_id=user_id))
        # return redirect(url_for('get_task', user_id=user_id))
    else:
        flash("Wrong email or password", "danger")
        return jsonify({"error": "Wrong email or password"}), 401


@app.route('/success', strict_slashes=False)
def success():
    """Render the success page base on the user properties"""
    """Render the success page based on the user properties"""
    from models.user import User
    
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User not found"}), 404
    user = storage.get(User, user_id)
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


@app.route('/register/new', methods=['POST'], strict_slashes=False)
def register_new():
    """Render the Register page."""
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    middle_name = request.form.get('middle_name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    
    if password != confirm_password:
        flash("Password mismatch", "danger")
        return "Password mismatch", (400)
    obj = {
        'first_name': first_name,
        'last_name': last_name,
        'middle_name': middle_name,
        'email': email,
        'password': password,
        'role': 'user'
    }
    print(obj)
    headers = {
        'Content-Type': 'application/json'
    }
    url = "http://127.0.0.1:5200/user"
    response = requests.post(url, json=obj, headers=headers)
    if response.status_code == 200:
        flash("Successfully registered", "success")
        return render_template('login.html')
    else:
        flash("Email already exists", "danger")
        return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
