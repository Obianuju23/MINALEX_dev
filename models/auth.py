# auth.py
from functools import wraps
from flask import g, jsonify

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if g.user.role != "admin":
            return jsonify({"error": "Admin privileges required"}), 403
        return func(*args, **kwargs)
    return wrapper
