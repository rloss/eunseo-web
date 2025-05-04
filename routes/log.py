from flask import Blueprint, render_template, request, redirect
import json
import os
from datetime import datetime

log_bp = Blueprint('log', __name__)

LOG_FILE = os.path.join("data", "log.json")

@log_bp.route("/log", methods=["GET", "POST"])
def log():
    if request.method == "POST":
        new_entry = {
            "date": datetime.now().strftime("%Y.%m.%d %H:%M"),
            "title": request.form["title"],
            "content": request.form["content"]
        }

        # 기존 로그 불러오기
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except FileNotFoundError:
            logs = []

        # 새 로그 추가
        logs.insert(0, new_entry)

        # 다시 저장
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)

        return redirect("/log")

    # GET 요청: 로그 리스트 보여주기
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    return render_template("log.html", logs=logs)
