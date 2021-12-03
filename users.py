from db import db
from models import User
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    user = User.query.filter_by(username=username).first()
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
    username_exists = User.query.filter_by(username=username).first()
    email_exists = User.query.filter_by(email=email).first()
    if username_exists or email_exists:
        return False
    
    hash_value = generate_password_hash(password)
    user = User(username=username, password=hash_value, email=email)
    db.session.add(user)
    db.session.commit()
    return login(username, password)