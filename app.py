from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from auth import check_password, load_users  # Import functions from auth.py
import json
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Initialize Bcrypt
bcrypt = Bcrypt()

# Read the secret key from the generated file (secret_key.txt)
with open("secret_key.txt", "rb") as file:
    app.secret_key = file.read()

# Load users from JSON file
def load_users():
    filepath = os.path.join(os.path.dirname(__file__), "user.json")
    with open(filepath, "r") as file:
        return json.load(file)

# Function to check password using Bcrypt
def check_password(stored_password_hash, password_to_check):
    return bcrypt.check_password_hash(stored_password_hash, password_to_check)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()

        # Check if user exists and password matches
        for user in users:
            if user["username"] == username and check_password(user["password"], password):
                session["username"] = username  # Store session
                return redirect(url_for("chatbot_interface"))

        # If username or password is incorrect, display a message
        return "Invalid credentials, please try again"

    return render_template("login.html")

@app.route("/chatbot")
def chatbot_interface():
    if "username" not in session:
        return redirect(url_for("login"))  # If the user is not logged in, redirect to login
    return render_template("bot_interface.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/api/timetable")
def api_timetable():
    with open("timetable.json", "r") as file:
        return jsonify(json.load(file))

if __name__ == "__main__":
    app.run(debug=True)
