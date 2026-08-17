from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=10)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=30)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=5, max=30), EqualTo("password", message="Passwords must match")])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=10)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=30)])
    submit = SubmitField("Login")