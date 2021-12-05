from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = """
        SELECT id, username, email, password, is_admin
        FROM users
        WHERE users.username = :username
        """
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    
    hash_value = user.password
    if check_password_hash(hash_value, password):
        session["username"] = username
        return True
    else:
        return False

def logout():
    del session["username"]

def register(username, password, email):
    sql = """
        SELECT EXISTS(
            SELECT username, email 
            FROM users 
            WHERE username=:username OR email=:email
        )
    """
    result = db.session.execute(sql, {"username": username, "email":email})
    exists = result.fetchone()[0]
    if exists:
        return False
    
    hash_value = generate_password_hash(password)
    sql = """
        INSERT INTO users (username, password, email, is_admin)
        VALUES (:username, :password, :email, :is_admin)
        """
    db.session.execute(sql, {
        "username": username,
        "password": hash_value,
        "email": email,
        "is_admin": 0
        }
    )
    db.session.commit()
    return login(username, password)

def get_logged_in_user():
    logged_in_user = session.get("username", 0)
    if not logged_in_user:
        return False
    sql = "SELECT * FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":logged_in_user}).fetchone()
    return result