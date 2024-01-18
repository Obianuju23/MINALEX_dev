from flask import Blueprint, request, jsonify
from models.task import Task
from models.user import User
from models import storage
from models.utils.utils import validate_uuid4

task_api = Blueprint('task_api', __name__)


@task_api.route('/task', methods=['GET'], defaults={'task_id': None}, strict_slashes=False)
def get_all_tasks():
    all_tasks = [task.to_dict() for task in storage.all(Task).values()]
    return jsonify(all_tasks), 200


@task_api.route('/task/<task_id>', methods=['GET'], strict_slashes=False)
@validate_uuid4(id_param='task_id')
def get_task(task_id):
    task = storage.get(Task, task_id)
    return jsonify(task.to_dict())


@task_api.route('/users/<user_id>/task', methods=['POST'], strict_slashes=False)
@validate_uuid4(id_param='user_id')
def create_task(user_id):
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    data = request.get_json()
    required_fields = ['name', 'description']
    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Missing required field: {field}",
                "genFormat": "{'name': 'string', 'description': 'string'}"
            }), 400
    # validate the user_id is attached to a valid User
    user = storage.get(User, data['user_id'])
    if not user:
        return jsonify({"error": "Invalid user_id"}), 400
    data['user_id'] = user_id
    task = Task(**data)
    task.save()
    return jsonify(task.to_dict()), 201


@task_api.route('/task/<task_id>', methods=['PUT'], strict_slashes=False)
@validate_uuid4(id_param='task_id')
def update_task(task_id):
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    data = request.get_json()
    task = storage.get(Task, task_id)
    if not task:
        return (
            jsonify(
                {
                    "error": "Task not found",
                    "msg": f"Task with id {task_id} not found",
                    "remarks": "Operation Invalid",
                }
            ),
            404,
        )
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at', '__class__']:
            setattr(task, key, value)
    task.save()
    return jsonify(task.to_dict())


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
