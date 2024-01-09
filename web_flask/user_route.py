from flask import Blueprint, request, jsonify
from models.user import User
from models import storage

user_api = Blueprint('user_api', __name__)


@user_api.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    # Validate and create a User instance
    user = User(**data)
    user.save()

    return jsonify(user.to_dict()), 201


@user_api.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = storage.get(User, user_id)

    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({"error": "User not found"}), 404


@user_api.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = storage.get(User, user_id)

    if user:
        data = request.get_json()
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return jsonify(user.to_dict())
    else:
        return jsonify({"error": "User not found"}), 404


@user_api.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = storage.get(User, user_id)

    if user:
        user.delete()
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"error": "User not found"}), 404
