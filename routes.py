from app import app
from flask import redirect, render_template, request, session
import quizzer, users
from models import Question, Quiz, User

@app.route("/")
def index():
    return render_template("index.html", quizzes=quizzer.get_all_quizzes())

@app.route("/quiz/<int:id>")
def quiz(id):
    return render_template("quiz.html", questions=quizzer.get_questions_for_quiz_id(id))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        form_username = request.form["username"]
        form_email = request.form["email"]
        form_password = request.form["password"]
        form_password_verification = request.form["password-verification"]

        if form_password != form_password_verification:
            return redirect("/fail")
        if users.register(form_username, form_password, form_email):
            return redirect("/")
        else:
            return redirect("/fail")

@app.route("/fail")
def fail():
    return render_template("fail.html")

@app.route("/login", methods=["POST"])
def login():
    form_username = request.form["username"]
    form_password = request.form["password"]
    if users.login(form_username, form_password):
        return redirect("/")
    else:
        return redirect("/fail")
        
@app.route("/logout")
def logout():
    # del session["username"]
    users.logout()
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
def add_new_quiz_with_questions(number_of_questions):
    if request.method == "POST":
        if quizzer.add_questions(request, number_of_questions):
            return redirect("/")
        else:
            return redirect("/fail")
    else:
        return render_template("add_questions.html", number_of_questions=number_of_questions)