from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Load users from JSON
def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

# Load timetable data from JSON
def load_timetable():
    with open("timetable.json", "r") as file:
        return json.load(file)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()

        # Check if user exists
        for user in users:
            if user["username"] == username and user["password"] == password:
                session["username"] = username  # Store session
                return redirect(url_for("chatbot_interface"))

    return render_template("login.html")

@app.route("/chatbot")
def chatbot_interface():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("bot_interface.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/api/timetable")
def api_timetable():
    return jsonify(load_timetable())

if __name__ == "__main__":
    app.run(debug=True)
