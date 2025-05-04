from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/log")
def log():
    return render_template("log.html")

@app.route("/lab")
def lab():
    return render_template("lab.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000)) 
    app.run(host="0.0.0.0", port=port)
