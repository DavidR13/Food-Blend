from flask import render_template, request, redirect, url_for, flash, abort
from Flask_Directory import app, api_functions, forms
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

    if request.method == 'POST':
        recipe = form.search.data
        diet = form.diet.data

        response = api_functions.get_recipes(recipe, diet)

    return render_template("find_recipes.html", form=form)