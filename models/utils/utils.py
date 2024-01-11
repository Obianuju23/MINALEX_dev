# validation.py

from functools import wraps
from flask import jsonify
from uuid import UUID


def validate_uuid4(id_param='id'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Check if the provided id is a valid UUID4
                uuid_obj = UUID(kwargs[id_param], version=4)
            except ValueError:
                return jsonify({"error": "Invalid UUID format"}), 400
            return func(*args, **kwargs)

        return wrapper

    return decorator
