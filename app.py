from datetime import datetime
from os import getenv

from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

## Database ##
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql" + getenv("DATABASE_URL")[8:]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
db = SQLAlchemy(app)

## Models ##
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


## Routes
@app.route("/")
def index():
    quizzes = Quiz.query.all()
    return render_template("index.html", quizzes=quizzes)


@app.route("/quiz/<int:id>")
def quiz(id):
    questions = Question.query.filter_by(quiz_id=id)
    return render_template("quiz.html", questions=questions)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        form_username = request.form["username"]
        form_email = request.form["email"]
        form_password = request.form["password"]
        form_password_verification = request.form["password-verification"]
        
        username_exists = User.query.filter_by(username=form_username).first()
        email_exists = User.query.filter_by(username=form_email).first()

        if form_password != form_password_verification:
            return redirect("/fail")
        if username_exists or email_exists:
            return redirect("fail")
        
        hash_value = generate_password_hash(form_password)
        user = User(username=form_username, password=hash_value, email=form_email)
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/fail")
def fail():
    return render_template("fail.html")


@app.route("/login", methods=["POST"])
def login():
    form_username = request.form["username"]
    form_password = request.form["password"]
    user = User.query.filter_by(username=form_username).first()
    if not user:
        return redirect("/fail")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, form_password):
            session["username"] = form_username
            return redirect("/")
        else:
            return redirect("/fail")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/add-quiz/", methods=["GET", "POST"])
def add_quiz():
    if request.method == "POST":
        questions = request.form["questions"]
        url = "/add-questions/" + questions
        return redirect(url)
    else:
        return render_template("add_quiz.html")

@app.route("/add-questions/<int:number_of_questions>", methods=["GET", "POST"])
def add_questions(number_of_questions):
    if request.method == "POST":
        quiz = Quiz()
        for i in range(number_of_questions):
            form_question = request.form[f"question{i+1}"]
            form_answer = request.form[f"answer{i+1}"]
            quiz.questions.append(Question(question=form_question, answer=form_answer))
        db.session.add(quiz)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_questions.html", number_of_questions=number_of_questions)
