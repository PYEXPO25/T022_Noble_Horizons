import os
import secrets

# Generate a secret key
secret_key = secrets.token_bytes(16)

# Save the secret key to a file
with open("secret_key.txt", "wb") as file:
    file.write(secret_key)

print(f"Secret key generated: {secret_key}")
