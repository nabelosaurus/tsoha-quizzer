from app import app
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = getenv(
    "SQLALCHEMY_TRACK_MODIFICATIONS")
db = SQLAlchemy(app)
