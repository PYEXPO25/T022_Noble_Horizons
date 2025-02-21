from flask_bcrypt import Bcrypt
import json

bcrypt = Bcrypt()

# Function to load users from the JSON file
def load_users():
    with open("user.json", "r") as file:
        return json.load(file)

# Function to check if the password matches the stored hash
def check_password(stored_password_hash, password_to_check):
    return bcrypt.check_password_hash(stored_password_hash, password_to_check)
