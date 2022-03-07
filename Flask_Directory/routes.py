from flask import render_template, request, redirect, url_for, flash, abort
from Flask_Directory import app, api_functions, forms, linked_list
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required
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

    return render_template("home.html", recipes=random_recipes_list)


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


@app.route('/register')
def register():
    pass


@app.route('/login')
def login():
    pass