from flask import render_template, request, redirect, url_for, flash, abort
from Flask_Directory import app, api_functions
import os
from datetime import date


@app.route('/')
@app.route('/home')
def index():
    response = api_functions.get_random_recipes()
    random_recipes_list = []

    for recipe in response['recipes']:
        # if there is no image for a recipe, make it an empty string
        if 'image' not in recipe:
            recipe['image'] = ''

        random_recipe = (recipe['title'], recipe['sourceUrl'], recipe['image'], recipe['readyInMinutes'], recipe['servings'])
        random_recipes_list.append(random_recipe)

    return render_template("home.html", recipes=random_recipes_list)
