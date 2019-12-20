from flask import Flask, request, jsonify
from flask_cors import CORS
from random import randint
import sqlite3
import requests
import os

app = Flask(__name__)
CORS(app)


# @app.route('/api/login', methods=["POST"])
# def getToken():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#     if username and password: 
#         with sqlite3.connect('data.db') as connection: 
#             cursor = connection.cursor()
#             sql = """SELECT token FROM accounts WHERE username=? AND password_hash=?"""
#             token = cursor.execute(sql, (username, password)).fetchone()
#             if token:
#                 return jsonify({"token":token})
#     return jsonify({"token": ""})


CRED_DIR = os.path.join(os.getenv('HOME'), ".credentials" )
SP_TOKEN = "SPOONACULAR.txt"
TOKENFILE = os.path.join(CRED_DIR, SP_TOKEN)
token = open(TOKENFILE).read().strip()

@app.route('/api/newRecipe', methods=["POST"])
def get_recipe_by_complex_search():
    data = request.get_json()
    ingredients = data.get('ingredients')
    number = data.get('number')
    # option to sort by popularity sort=popularity
    api_url = "https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&includeIngredients={ingredients}&instructionsRequired=true&addRecipeInformation=true&fillIngredients=true&ignorePantry=false&number={number}"
    get_url = api_url.format(api_key=token, ingredients=ingredients, number=number)
    response = requests.get(get_url)
    if response.status_code == 200:
        res = response.json()
        return jsonify({"data": res})
    else:
        return jsonify({"error": "API error"})

@app.route('/api/viewRecipe', methods=["POST"])
def view_recipe():
    data = request.get_json()
    recipe_id = data.get('id')
    api_url = "https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&id={recipe_id}&instructionsRequired=true&addRecipeInformation=true&fillIngredients=true&ignorePantry=false"
    get_url = api_url.format(api_key=token, recipe_id=recipe_id)
    response = requests.get(get_url)
    if response.status_code == 200:
        res = response.json()
        return jsonify({"data": res})
    else: 
        return jsonify({"error": "API error"})

@app.route('/api/saveUser', methods=["POST"])
def saveUser(): 
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    with sqlite3.connect('data.db') as connection: 
        cursor = connection.cursor()
        SQL = "SELECT id FROM users WHERE username=? AND password_hash=?;"
        token = cursor.execute(SQL, (username, password)).fetchone()
        if token == None: 
            token = str(randint(1000000000,9999999999))
            SQL = """INSERT INTO users (username, password_hash, token)
            VALUES (?,?,?);"""
            cursor.execute(SQL, (username, password, token))
        return jsonify({"token": token})




if __name__ == "__main__":
    app.run(debug=True)