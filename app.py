from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render 환경이 제공하는 포트 사용
    app.run(host="0.0.0.0", port=port)