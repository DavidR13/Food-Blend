import requests
import os


def get_random_recipes():
    random_recipes_url = f"https://api.spoonacular.com/recipes/random?number=6&apiKey={os.environ['API_KEY']}"

    response = requests.get(url=random_recipes_url).json()
    return response


def get_recipes(query, diet):
    recipes_url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&diet={diet}&" \
                  f"addRecipeInformation=true&apiKey={os.environ['API_KEY']}"

    response = requests.get(url=recipes_url).json()
    return response
