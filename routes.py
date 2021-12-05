from app import app
from flask import redirect, render_template, request, session
import quizzer, users, results
from forms import LoginForm, RegistrationForm, AddQuizForm


@app.route("/")
def index():
    return render_template("index.html", quizzes=quizzer.get_all_quizzes(), login_form=LoginForm())


@app.route("/quiz/<int:id>")
def quiz(id):
    return render_template("quiz.html", questions=quizzer.get_questions_for_quiz_id(id), login_form=LoginForm())


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "GET":
        return render_template("register.html", form=form, login_form=LoginForm())
    if request.method == "POST":
        form_username = request.form["username"]
        form_email = request.form["email"]
        form_password = request.form["password"]
        form_password_verification = request.form["password_verification"]

        if form_password != form_password_verification:
            return render_template("fail.html", message="Password and verification don't match.", login_form=LoginForm())
        if users.register(form_username, form_password, form_email):
            return redirect("/")
        else:
            return render_template("fail.html", message="Username or email already registered.", login_form=LoginForm())


@app.route("/fail")
def fail(message):
    return render_template("fail.html", message=message, login_form=LoginForm())


@app.route("/login", methods=["POST"])
def login():
    form_username = request.form["username"]
    form_password = request.form["password"]
    if users.login(form_username, form_password):
        return redirect("/")
    else:
        return render_template("fail.html", message="Wrong username or password.", login_form=LoginForm())


@app.route("/logout")
def logout():
    # del session["username"]
    users.logout()
    return redirect("/")


@app.route("/add-quiz/", methods=["GET", "POST"])
def add_quiz():
    if request.method == "POST":
        questions = request.form["number_of_questions"]
        url = "/add-questions/" + questions
        return redirect(url)
    else:
        return render_template("add_quiz.html", login_form=LoginForm(), form=AddQuizForm())


@app.route("/add-questions/<int:number_of_questions>", methods=["GET", "POST"])
def add_new_quiz_with_questions(number_of_questions):
    if request.method == "POST":
        if quizzer.add_new_quiz_with_questions(request, number_of_questions):
            return redirect("/")
        else:
            return render_template("fail.html", message="Could not add quiz.", login_form=LoginForm())
    else:
        return render_template("add_questions.html", number_of_questions=number_of_questions, login_form=LoginForm())


@app.route("/answer/", methods=["POST"])
def answer():
    if quizzer.process_answers(request.form):
        return redirect("/")
    else:
        return redirect("/")

@app.route("/top25", methods=["GET"])
def top25():
    return render_template("top25.html", results=results.top_25_all(), login_form=LoginForm())