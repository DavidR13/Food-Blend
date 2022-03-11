from flask import render_template, request, redirect, url_for, flash, abort
from Flask_Directory import app, api_functions, linked_list
from .forms import FindRecipes, Register, Login
from .models import *
from . import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import os
from datetime import date


@app.route('/')
@app.route('/home')
def index():
    response = api_functions.get_random_recipes()
    random_recipes_list = []

    # if max daily API calls is reached
    if response is None:
        return render_template("home.html", recipes=random_recipes_list)

    for recipe in response['recipes']:
        # if there is no image for a recipe, make it an empty string
        if 'image' not in recipe:
            recipe['image'] = ''

        random_recipe = (recipe['title'], recipe['sourceUrl'], recipe['image'], recipe['readyInMinutes'], recipe['servings'])
        random_recipes_list.append(random_recipe)

    return render_template("home.html", recipes=random_recipes_list, user=current_user)


@app.route('/find-recipes', methods=['GET', 'POST'])
def get_recipes():
    form = FindRecipes()
    all_recipes = linked_list.LinkedList()
    all_recipes_list = []

    if request.method == 'POST':
        search_recipe = form.search.data
        search_diet = form.diet.data

        response = api_functions.get_recipes(search_recipe, search_diet)

        # if max daily API calls is reached
        if response is None:
            return render_template("find_recipes.html", form=form)

        for recipe in response['results']:
            response_recipe = (recipe['title'], recipe['readyInMinutes'], recipe['servings'], recipe['sourceUrl'],
                               recipe['image'], recipe['summary'])

            all_recipes.append_value(response_recipe)  # append recipe into the linked list

        all_recipes_list = all_recipes.to_list()  # convert all linked list values into a regular list

        return render_template("find_recipes.html", form=form, recipes=all_recipes_list, searched_recipe=search_recipe)
    return render_template("find_recipes.html", form=form, recipes=all_recipes_list, user=current_user)


@app.route('/community/<string:name>')
def communities(name):
    print(name)
    return render_template("communities.html", name=name, user=current_user)


@app.route('/community-post/<string:name>/<int:id>/<string:title>')
def show_individual_post(name, id, title):
    pass


@app.route('/create-post', methods=['GET', 'POST'])
@login_required
def post():
    pass


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    pass


@app.route('/delete-post/<int:post_id>', methods=['GET', 'POST', 'DELETE'])
@login_required
def delete_post(post_id):
    pass


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()

    if request.method == 'POST':
        full_name = form.full_name.data
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)

        user_exists = User.query.filter_by(email=email).first()

        if user_exists:
            flash('An account already exists with this email!', category='error')
            return redirect(url_for('login'))
        else:
            new_user = User(
                email=email,
                password=password,
                name=full_name,
                username=username
            )

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
        return redirect(url_for('index'))
    return render_template('register.html', form=form, user=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()

    if request.method == 'POST':
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('index'))
            else:
                flash('Wrong password, please try again.', category='error')
        else:
            flash('This user does not exist.', category='error')

    return render_template('login.html', form=form, user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))