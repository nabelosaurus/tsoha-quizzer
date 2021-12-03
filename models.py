from db import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    questions = db.relationship("Question", backref="competition", lazy=True)

    def __repr__(self):
        return f"Quiz #{self.id} - {self.date}"

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(50), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey(Quiz.id), nullable=False)

    def __repr__(self):
        return f"Quiz #{self.id} - {self.question[:30]}.."

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey(Quiz.id), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    score = db.Column(db.Integer, nullable=False)