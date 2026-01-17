# Simple user database

users = {
    "admin": "admin123",
    "user": "user123",
    "doctor": "doctor123"
}
def validate_user(username, password):
    return users.get(username) == password
