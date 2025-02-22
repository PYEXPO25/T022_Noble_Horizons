from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from auth import check_password, load_users
import json
import os

app = Flask(__name__)
app.secret_key = "my_super_secret_key_12345"  # Required for session management

# Function to load users from the existing JSON file
def load_users():
    filepath = os.path.join(os.path.dirname(__file__), "user.json")
    with open(filepath, "r") as file:
        return json.load(file)

# Function to load student data from the new JSON file
def load_student_data():
    with open("student_data.json", "r") as file:
        return json.load(file)

# Function to load canteen data from the new JSON file
def load_canteen_data():
    with open("canteen_data.json", "r") as file:
        return json.load(file)

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

        # If username or password is incorrect, you can display a message or reload the page
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

# API route to return student data
@app.route("/api/student_data")
def api_student_data():
    return jsonify(load_student_data())

# API route to return canteen data
@app.route("/api/canteen_data")
def api_canteen_data():
    return jsonify(load_canteen_data())

if __name__ == "__main__":
    app.run(debug=True)
