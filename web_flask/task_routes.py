from flask import Blueprint, request, jsonify,g
from models.task import Task
from models import storage
from models.auth import admin_required

task_api = Blueprint('task_api', __name__)


@task_api.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()

    # Validate and create a Task instance
    task = Task(**data)
    task.save()

    return jsonify(task.to_dict()), 201


@task_api.route('/task/<task_id>', methods=['GET'])
def get_task(task_id):
    task = storage.get(Task, task_id)

    if task:
        return jsonify(task.to_dict())
    else:
        return jsonify({"error": "Task not found"}), 404


@task_api.route('/task/<task_id>', methods=['PUT'])
def update_task(task_id):
    task = storage.get(Task, task_id)

    if task:
        data = request.get_json()
        for key, value in data.items():
            setattr(task, key, value)
        task.save()
        return jsonify(task.to_dict())
    else:
        return jsonify({"error": "Task not found"}), 404


@task_api.route('/task/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = storage.get(Task, task_id)

    if task:
        task.delete()
        return jsonify({"message": "Task deleted successfully"})
    else:
        return jsonify({"error": "Task not found"}), 404
