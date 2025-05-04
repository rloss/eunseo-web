from flask import Blueprint, render_template
import json
import os

log_bp = Blueprint('log', __name__)

@log_bp.route("/log")
def log():
    log_path = os.path.join("data", "log.json")
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    return render_template("log.html", logs=logs)
