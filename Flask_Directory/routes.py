from flask import render_template, request, redirect, url_for, flash, abort
from Flask_Directory import app, api_functions, forms, linked_list
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
    form = forms.FindRecipes()
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
    return render_template("find_recipes.html", form=form, recipes=all_recipes_list)


@app.route('/community/<string:name>')
def communities(name):
    print(name)
    return render_template("communities.html", name=name)


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
    form = forms.Register()

    if request.method == 'POST':
        full_name = form.full_name.data
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.Login()

    if request.method == 'POST':
        email = form.email.data
        password = form.password.data

        # need to get user from db, check if it exists, check password hash, and login user if it all checks out

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))