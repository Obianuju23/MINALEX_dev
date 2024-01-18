#!/usr/bin/env python3
"""Template for our project app"""

from flask import Flask, jsonify, make_response
from api.v1.views.task import task_api
from api.v1.views.user import user_api
# from api.v1.views.admin import admin_api
from flask_cors import CORS
from models import storage

app = Flask(__name__)

# app.register_blueprint(admin_api)
app.register_blueprint(user_api)
app.register_blueprint(task_api)
CORS(app)


@app.teardown_appcontext
def shutdown(self):
    """Flask shutdown function"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Create a handler for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5200, debug=True)
