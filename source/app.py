from chatbot import chatbot
from flask import Flask, render_template, request, session, redirect, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.static_folder = 'static'

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.sqlite3')
    conn.row_factory = sqlite3.Row  # Allows fetching data as dictionaries
    return conn

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/index")
def home():
    if 'id' in session:
        return render_template("index.html")
    else:
        return redirect("/")

@app.route("/logout")
def logout():
    session.pop("id", None)
    return redirect("/")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run()
