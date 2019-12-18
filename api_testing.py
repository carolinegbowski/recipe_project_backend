import requests
import os

# GET https://api.spoonacular.com/recipes/complexSearch

CRED_DIR = os.path.join(os.getenv('HOME'), ".credentials" )
SP_TOKEN = "SPOONACULAR.txt"
TOKENFILE = os.path.join(CRED_DIR, SP_TOKEN)
token = open(TOKENFILE).read().strip()
print(token)

def get_recipe_by_ingredients():
    api_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}&ingredients={ingredients}&number={number}"
    get_url = api_url.format(api_key=token, ingredients='apples,+flour,+sugar', number="1" )
    response = requests.get(get_url)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)
    return

def get_recipe_by_complex_search():
    # option to sort by popularity sort=popularity
    api_url = "https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&includeIngredients={ingredients}&instructionsRequired=true&addRecipeInformation=true&fillIngredients=true&ignorePantry=false&number={number}"
    get_url = api_url.format(api_key=token, ingredients='mushroom,+onion', number="1" )
    response = requests.get(get_url)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)
    return





if __name__ == "__main__":
    get_recipe_by_complex_search()