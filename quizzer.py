from db import db
import results, users


def get_all_quizzes():
    sql = db.session.execute(
        """
        SELECT quiz.id, quiz.date 
        FROM quiz
        """
    )
    return sql.fetchall()


def get_questions_for_quiz_id(id):
    sql = """
        SELECT question.id, question.question, question.answer, question.quiz_id
        FROM question
        WHERE question.quiz_id=:id
        """
    result = db.session.execute(sql, {"id": id})
    return result


def add_new_quiz_with_questions(request, number_of_questions):
    sql = "INSERT INTO quiz (date) VALUES (:date) RETURNING quiz.id"
    result = db.session.execute(sql, {"date": "NOW()"})
    quiz_id = result.fetchone()[0]
    for i in range(number_of_questions):
        form_question = request.form[f"question{i+1}"]
        form_answer = request.form[f"answer{i+1}"]
        sql = "INSERT INTO question (question, answer, quiz_id) VALUES (:question, :answer, :quiz_id)"
        db.session.execute(sql, {"question": form_question, "answer": form_answer, "quiz_id": quiz_id})
    db.session.commit()
    return True


def check_answer(question, answer):
    sql = """
        SELECT question.id, question.question, question.answer, question.quiz_id
        FROM question
        WHERE question.id=:id
        """
    result = db.session.execute(sql, {"id": question})
    question = result.fetchone()
    if question.answer == answer:
        return True
    return False

def get_quiz_for_question(question_id):
    sql = "SELECT * FROM question WHERE id=:id"
    result = db.session.execute(sql, {"id": question_id})
    quiz_id = result.fetchone().quiz_id
    return quiz_id


def process_answers(answers):
    points = 0
    for question, answer in answers.items():
        if check_answer(question, answer):
            points += 1
    user = users.get_logged_in_user()
    if not user:
        return False
    quiz = get_quiz_for_question(question)
    results.add_result(user.id, quiz, points)
    return True