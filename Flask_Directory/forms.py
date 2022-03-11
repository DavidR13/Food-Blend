from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class FindRecipes(FlaskForm):
    search = StringField("What are you looking for?", validators=[DataRequired()])
    diet = SelectField("Choose your diet (or leave blank):", choices=[
        ('', ''),
        ('gluten free', 'Gluten Free'),
        ('ketogenic', 'Ketogenic'),
        ('vegetarian', 'Vegetarian'),
        ('lacto-vegetarian', 'Lacto-Vegetarian'),
        ('vegan', 'Vegan'),
        ('pescetarian', 'Pescetarian'),
    ], default='')
    submit = SubmitField("Submit")


class Register(FlaskForm):
    full_name = StringField("Full Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


class Login(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
