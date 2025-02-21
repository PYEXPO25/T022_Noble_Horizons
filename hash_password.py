from flask_bcrypt import Bcrypt

# Initialize Flask-Bcrypt
bcrypt = Bcrypt()

# Your password
password = "000"

# Hash the password
hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

# Print the hashed password
print(hashed_password)
