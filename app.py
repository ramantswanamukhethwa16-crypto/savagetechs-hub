
from flask import Flask, render_template, redirect, url_for, request
import os

app = Flask(__name__)

@app.route("/")
def login():
    # Render your Firebase login/signup page template
    return render_template("login.html")

@app.route("/home")
def home():
    # Once authenticated, render your main app dashboard
    return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

