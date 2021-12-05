from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, Length, NumberRange

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField("Email", validators=[DataRequired(), Length(min=6, max=80)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=256)])
    password_verification = PasswordField("Verify password", validators=[Length(min=8, max=256)])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=256)])
    submit = SubmitField("Login")


class AddQuizForm(FlaskForm):
    number_of_questions = IntegerField("Questions", validators=[DataRequired(), NumberRange(min=1, max=30)])
    submit = SubmitField("Add")
