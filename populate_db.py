import json
from argon2 import PasswordHasher
from Main import app  # Import the Flask app instance
from create_db import db, User, Stock, Transaction  # Import classes from create_db.py

import json
from argon2 import PasswordHasher

# Initialize the password hasher
ph = PasswordHasher()

# Load the data from data.json
with open('data.json', 'r') as f:
    data = json.load(f)

# Hash the passwords for each user
for user in data['users']:
    user['password'] = ph.hash(user['password'])

# Write the hashed passwords back to data.json
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Define a function to populate the database from the JSON file
def populate_from_json(filename):
    # Set up the application context
    with app.app_context():
        # Open the JSON file and load the data
        with open(filename, 'r') as f:
            data = json.load(f)

        # Initialize the password hasher
        ph = PasswordHasher()

        # Iterate over the users in the JSON data and add them to the database
        for user_data in data.get('users', []):
            # Hash the password
            hashed_password = ph.hash(user_data['password'])
            # Replace the plaintext password with the hashed password
            user_data['password'] = hashed_password
            user = User(**user_data)
            db.session.add(user)

        # Commit the changes to the database
        db.session.commit()

# If this script is run directly, populate the database from the JSON file
if __name__ == '__main__':
    populate_from_json('data.json')