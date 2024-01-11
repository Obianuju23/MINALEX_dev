from flask import Blueprint, request, jsonify
from models.admin import Admin
from models import storage
# store password as brcypt hashed password
import bcrypt
from models.utils.utils import validate_uuid4


admin_api = Blueprint('admin_api', __name__)


@admin_api.route('/admin', methods=['POST'], strict_slashes=False)
def create_admin():
    """ Create a new Admin """
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
    all_obj = storage.all(Admin).values()
    for obj in all_obj:
        if obj.email == data['email']:
            return jsonify({"error": "Email already exists"}), 400
    # Validate and create an Admin instance
    admin = Admin(**data)
    admin.save()
    return jsonify(admin.to_dict()), 201


@admin_api.route('/admin', methods=['GET'], defaults={'admin_id': None}, strict_slashes=False)
@admin_api.route('/admin/<admin_id>', methods=['GET'], strict_slashes=False)
@validate_uuid4(id_param='admin_id')
def get_admin(admin_id):
    if admin_id:
        admin = storage.get(Admin, admin_id)
        return jsonify(admin.to_dict())
    all_admin = [admin.to_dict() for admin in storage.all(Admin).values()]
    return jsonify(all_admin), 200


@admin_api.route('/admin/<admin_id>', methods=['PUT'], strict_slashes=False)
@validate_uuid4(id_param='admin_id')
def update_admin(admin_id):
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if not admin_id:
        return jsonify({"error": "Admin ID is required"}), 404
    data = request.get_json()
    exclude = ['id', 'created_at', 'updated_at', '__class__']
    admin = storage.get(Admin, admin_id)
    all_obj = storage.all(Admin).values()
    if admin:
        # check if the content is not in the exclude list
        for key, value in data.items():
            if key not in exclude:
                for obj in all_obj:
                    if obj.email == data['email'] and obj.id != admin_id:
                        return jsonify({"error": "Email already exists"}), 400
                setattr(admin, key, value)
        # ensure the updated field email is not in the database
        all_obj = storage.all(Admin).values()
        for obj in all_obj:
            if obj.email == data['email'] and obj.id != admin_id:
                return jsonify({"error": "Email already exists"}), 400
        admin.save()
        return jsonify(admin.to_dict())
    else:
        return jsonify({"error": "Admin not found"}), 404


@admin_api.route('/admin/<admin_id>', methods=['DELETE'], strict_slashes=False)
@validate_uuid4(id_param='admin_id')
def delete_admin(admin_id):
    """ Delete a Admin """
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    admin = storage.get(Admin, admin_id)
    if admin:
        admin.delete()
        return jsonify({"message": "Admin deleted successfully"}), 200
    else:
        return jsonify({"error": "Admin not found"}), 404
