import requests
import os
from Flask_Directory import json_functions


def get_random_recipes():
    random_recipes_url = f"https://api.spoonacular.com/recipes/random?number=8&apiKey={os.environ['API_KEY']}"

    response = requests.get(url=random_recipes_url).json()
    json_functions.save_to_file(response, "random_recipes_response.json")
    results = json_functions.read_from_file("random_recipes_response.json")
    return results


def get_recipes(query, diet):
    recipes_url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&diet={diet}&" \
                  f"addRecipeInformation=true&apiKey={os.environ['API_KEY']}"

    response = requests.get(url=recipes_url).json()
    json_functions.save_to_file(response, "recipes_response.json")
    results = json_functions.read_from_file("random_recipes_response.json")
    return results
