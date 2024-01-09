from flask import Blueprint, request, jsonify
from models.admin import Admin
from models import storage

admin_api = Blueprint('admin_api', __name__)


@admin_api.route('/admin', methods=['POST'])
def create_admin():
    data = request.get_json()

    # Validate and create an Admin instance
    admin = Admin(**data)
    admin.save()

    return jsonify(admin.to_dict()), 201


@admin_api.route('/admin/<admin_id>', methods=['GET'])
def get_admin(admin_id):
    admin = storage.get(Admin, admin_id)

    if admin:
        return jsonify(admin.to_dict())
    else:
        return jsonify({"error": "Admin not found"}), 404


@admin_api.route('/admin/<admin_id>', methods=['PUT'])
def update_admin(admin_id):
    admin = storage.get(Admin, admin_id)

    if admin:
        data = request.get_json()
        for key, value in data.items():
            setattr(admin, key, value)
        admin.save()
        return jsonify(admin.to_dict())
    else:
        return jsonify({"error": "Admin not found"}), 404


@admin_api.route('/admin/<admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    admin = storage.get(Admin, admin_id)

    if admin:
        admin.delete()
        return jsonify({"message": "Admin deleted successfully"})
    else:
        return jsonify({"error": "Admin not found"}), 404
