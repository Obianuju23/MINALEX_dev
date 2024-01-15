from flask import Blueprint, request, jsonify
from models.task import Task
from models.user import User
from models import storage
from models.utils.utils import validate_uuid4

task_api = Blueprint('task_api', __name__)

@task_api.route('/task', methods=['POST'], strict_slashes=False)
def create_task():
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    data = request.get_json()
    required_fields = ['user_id', 'name', 'description']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    # validate the user_id is a valid UUID
    if not validate_uuid4(data['user_id']):
        return jsonify({"error": "Invalid user_id"}), 400
    # validate the user_id is attached to a valid User
    user = storage.get(User, data['user_id'])
    if not user:
        return jsonify({"error": "Invalid user_id"}), 400
    task = Task(**data)
    task.save()
    return jsonify(task.to_dict()), 201


@task_api.route('/task', methods=['GET'], defaults={'task_id': None}, strict_slashes=False)
@task_api.route('/task/<task_id>', methods=['GET'], strict_slashes=False)
@validate_uuid4(id_param='task_id')
def get_task(task_id):
    if task_id:
        task = storage.get(Task, task_id)
        return jsonify(task.to_dict())
    all_tasks = [task.to_dict() for task in storage.all(Task).values()]
    return jsonify(all_tasks), 200


@task_api.route('/task/<task_id>', methods=['PUT'], strict_slashes=False)
@validate_uuid4(id_param='task_id')
def update_task(task_id):
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    data = request.get_json()
    task = storage.get(Task, task_id)
    all_tasks = storage.all(Task).values()
    if task:
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at', '__class__']:
                setattr(task, key, value)
        task.save()
        return jsonify(task.to_dict())
    else:
        return jsonify({"error": "Task not found"}), 404


@task_api.route('/task/<task_id>', methods=['DELETE'], strict_slashes=False)
@validate_uuid4(id_param='task_id')
def delete_task(task_id):
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    task = storage.get(Task, task_id)
    if task:
        task.delete()
        return jsonify({"message": "Task deleted successfully"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404



