from db import db
from models import Question, Quiz, User


def get_all_quizzes():
    return Quiz.query.all()


def get_questions_for_quiz_id(id):
    return Question.query.filter_by(quiz_id=id)


def add_new_quiz_with_questions(request, number_of_questions):
    quiz = Quiz()
    for i in range(number_of_questions):
        form_question = request.form[f"question{i+1}"]
        form_answer = request.form[f"answer{i+1}"]
        quiz.questions.append(
            Question(question=form_question, answer=form_answer))
    db.session.add(quiz)
    db.session.commit()
    return True
