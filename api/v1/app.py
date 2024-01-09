#!/usr/bin/env python3
"""Template for our project app"""

from flask import Flask, jsonify, make_response
from web_flask import admin_routes 
from web_flask import user_routes
from web_flask import task_routes 
from flask_cors import CORS
import sys
import os

# Assuming app.py is in api/v1 directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)

# Add the parent and grandparent directories to sys.path
sys.path.append(parent_dir)
sys.path.append(grandparent_dir)

from models.engine.db_storage import DBStorage
# from models.engine import db_storage
# from models import storage
# from api.v1.views import app_views

app = Flask(__name__)
storage = DBStorage()
# app.register_blueprint(app_views)
app.register_blueprint(admin_routes)
app.register_blueprint(user_routes)
app.register_blueprint(task_routes)
# cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def shutdown(self):
    """Flask shutdown function"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Create a handler for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
