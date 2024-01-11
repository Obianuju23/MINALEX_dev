from flask import Blueprint, request, jsonify
from models.user import User
from models import storage
from models.utils.utils import validate_uuid4
# store password as brcypt hashed password
import bcrypt


user_api = Blueprint('user_api', __name__)


@user_api.route('/user', methods=['POST'], strict_slashes=False)
def create_user():
    """ Create a new User """
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    data = request.get_json()
    # ensure the required fields are in the data
    required_fields = ['email', 'first_name', 'last_name', 'password']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    hash_pwd = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    data['password'] = hash_pwd
    # check if email already exists
    all_obj = storage.all(User).values()
    for obj in all_obj:
        if obj.email == data['email']:
            return jsonify({"error": "Email already exists"}), 400
    # Validate and create an User instance
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201


@user_api.route('/user', methods=['GET'], defaults={'user_id': None}, strict_slashes=False)
@user_api.route('/user/<user_id>', methods=['GET'], strict_slashes=False)
@validate_uuid4(id_param='user_id')
def get_user(user_id):
    if user_id:
        user = storage.get(User, user_id)
        return jsonify(user.to_dict())
    all_user = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(all_user), 200


@user_api.route('/user/<user_id>', methods=['PUT'], strict_slashes=False)
@validate_uuid4(id_param='user_id')
def update_user(user_id):
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    data = request.get_json()
    exclude = ['id', 'created_at', 'updated_at', '__class__']
    user = storage.get(User, user_id)
    all_obj = storage.all(User).values()
    if user:
        # check if the content is not in the exclude list
        for key, value in data.items():
            if key not in exclude:
                for obj in all_obj:
                    if obj.email == data['email'] and obj.id != user_id:
                        return jsonify({"error": "Email already exists"}), 400
                setattr(user, key, value)
        # ensure the updated field email is not in the database
        all_obj = storage.all(User).values()
        for obj in all_obj:
            if obj.email == data['email'] and obj.id != user_id:
                return jsonify({"error": "Email already exists"}), 400
        user.save()
        return jsonify(user.to_dict())
    else:
        return jsonify({"error": "User not found"}), 404


@user_api.route('/user/<user_id>', methods=['DELETE'], strict_slashes=False)
@validate_uuid4(id_param='user_id')
def delete_user(user_id):
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    user = storage.get(User, user_id)
    if user:
        user.delete()
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404
