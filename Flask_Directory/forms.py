from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor, CKEditorField

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
