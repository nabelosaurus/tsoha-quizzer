from db import db

class InvalidResultError(Exception):
    pass

def add_result(user_id, quiz_id, points):
    try:
        sql = """
        INSERT INTO competition (user_id, quiz_id, date, score) 
        VALUES (:user_id, :quiz_id, :date, :score)
        """
        db.session.execute(sql, {
            "user_id": user_id,
            "quiz_id": quiz_id,
            "date": "NOW()",
            "score": points
            }
        )
        db.session.commit()
    except:
        raise InvalidResultError("Error registering result.")


def top_10_by_user():
    pass

def top_25_all():
    sql = db.session.execute(
        """
        SELECT users.username, sum(competition.score) 
        FROM users, competition 
        WHERE users.id = competition.user_id 
        GROUP BY users.id 
        ORDER BY sum 
        DESC LIMIT 25
        """
    )
    result = sql.fetchall()
    return result

def top_10_by_quiz():
    pass