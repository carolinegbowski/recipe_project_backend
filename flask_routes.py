from flask import Flask, request, jsonify, json, Response
from flask_cors import CORS
from random import randint
import sqlite3
import requests
import os

app = Flask(__name__)
CORS(app)

DEBUGGER = False

CRED_DIR = os.path.join(os.getenv('HOME'), ".credentials" )
SP_TOKEN = "SPOONACULAR.txt"
TOKENFILE = os.path.join(CRED_DIR, SP_TOKEN)
token = open(TOKENFILE).read().strip()

@app.route('/api/newRecipe', methods=["POST"])
def get_recipe_by_complex_search():
    if DEBUGGER == True:
        res = {"results":[{"vegetarian":"true","vegan":"false","glutenFree":"true","dairyFree":"true","veryHealthy":"false","cheap":"false","veryPopular":"false","sustainable":"false","weightWatcherSmartPoints":6,"gaps":"no","lowFodmap":"false","ketogenic":"false","whole30":"false","preparationMinutes":0,"cookingMinutes":0,"sourceUrl":"https://lexiscleankitchen.com/honey-glazed-carrots/","spoonacularSourceUrl":"https://spoonacular.com/honey-glazed-carrots-1051408","aggregateLikes":1,"spoonacularScore":44.0,"healthScore":9.0,"creditsText":"Lexi's Clean Kitchen","sourceName":"Lexi's Clean Kitchen","pricePerServing":68.56,"id":1051408,"title":"Honey Glazed Carrots","readyInMinutes":45,"servings":4,"image":"https://spoonacular.com/recipeImages/1051408-312x231.jpg","imageType":"jpg","cuisines":[],"dishTypes":["side dish"],"diets":["gluten free","dairy free","lacto ovo vegetarian"],"occasions":["easter"],"winePairing":{},"analyzedInstructions":[{"name":"","steps":[{"number":1,"step":"Heat a large pan (at least 12 inches), over medium high heat and add oil.","ingredients":[{"id":4582,"name":"cooking oil","image":"vegetable-oil.jpg"}],"equipment":[{"id":404645,"name":"frying pan","image":"pan.png"}]},{"number":2,"step":"Once hot, place carrots cut side down and sear for 3 minutes, until the carrots start to caramelize. Give them a good shake and let them sear again for an additional 3 minutes.","ingredients":[{"id":11124,"name":"carrot","image":"sliced-carrot.png"}],"equipment":[],"length":{"number":6,"unit":"minutes"}},{"number":3,"step":"Add 1/2 teaspoon of salt and stir the pan.","ingredients":[{"id":2047,"name":"salt","image":"salt.jpg"}],"equipment":[{"id":404645,"name":"frying pan","image":"pan.png"}]},{"number":4,"step":"Carefully add 1/2 cup water and cover pan with tight fitting lid and cook for 7 minutes over medium heat. Uncover and reduce heat the medium low and continue to cook until the water has evaporate and the carrots are cooked though. If the water has reduced before the carrots have cooked, add a tablespoon more water at a time until they have cooked through.","ingredients":[{"id":11124,"name":"carrot","image":"sliced-carrot.png"},{"id":14412,"name":"water","image":"water.png"}],"equipment":[{"id":404645,"name":"frying pan","image":"pan.png"}],"length":{"number":7,"unit":"minutes"}},{"number":5,"step":"Once water has reduced, add butter (or dairy free oil) and honey and stir well and continue to cook until the carrots are glazed and the honey is bubbling, about 5 minutes. Season with 1/4 teaspoon large flaky sea salt.","ingredients":[{"id":1012047,"name":"sea salt","image":"salt.jpg"},{"id":11124,"name":"carrot","image":"sliced-carrot.png"},{"id":19296,"name":"honey","image":"honey.png"},{"id":14412,"name":"water","image":"water.png"},{"id":4582,"name":"cooking oil","image":"vegetable-oil.jpg"}],"equipment":[],"length":{"number":5,"unit":"minutes"}}]}],"usedIngredientCount":1,"missedIngredientCount":6,"likes":0,"missedIngredients":[{"id":19296,"amount":3.0,"unit":"tablespoons","unitLong":"tablespoons","unitShort":"Tbsp","aisle":"Nut butters, Jams, and Honey;Health Foods","name":"honey","original":"3 tablespoons honey","originalString":"3 tablespoons honey","originalName":"honey","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/honey.png"},{"id":4582,"amount":1.0,"unit":"tablespoon","unitLong":"tablespoon","unitShort":"Tbsp","aisle":"Oil, Vinegar, Salad Dressing","name":"oil","original":"1 tablespoon oil","originalString":"1 tablespoon oil","originalName":"oil","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/vegetable-oil.jpg"},{"id":4053,"amount":2.0,"unit":"tablespoons","unitLong":"tablespoons","unitShort":"Tbsp","aisle":"Oil, Vinegar, Salad Dressing","name":"olive oil","original":"2 tablespoons butter, coconut oil or olive oil","originalString":"2 tablespoons butter, coconut oil or olive oil","originalName":"butter, coconut oil or olive oil","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/olive-oil.jpg"},{"id":2047,"amount":0.5,"unit":"teaspoon","unitLong":"teaspoons","unitShort":"tsp","aisle":"Spices and Seasonings","name":"salt","original":"½ teaspoon salt","originalString":"½ teaspoon salt","originalName":"salt","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/salt.jpg"},{"id":1012047,"amount":0.25,"unit":"teaspoon","unitLong":"teaspoons","unitShort":"tsp","aisle":"Spices and Seasonings","name":"sea-salt","original":"1/4 teaspoon flaky sea salt, to garnish","originalString":"1/4 teaspoon flaky sea salt, to garnish","originalName":"flaky sea salt, to garnish","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/salt.jpg"},{"id":14412,"amount":0.5,"unit":"cup","unitLong":"cups","unitShort":"cup","aisle":"Beverages","name":"water","original":"1/2 cup water","originalString":"1/2 cup water","originalName":"water","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/water.png"}],"usedIngredients":[{"id":11124,"amount":2.0,"unit":"pound","unitLong":"pounds","unitShort":"lb","aisle":"Produce","name":"carrots","original":"2 pound carrots, peeled and sliced on the bias about ¼” thick","originalString":"2 pound carrots, peeled and sliced on the bias about ¼” thick","originalName":"carrots, peeled and sliced on the bias about ¼” thick","metaInformation":["thick","peeled","sliced"],"image":"https://spoonacular.com/cdn/ingredients_100x100/sliced-carrot.png"}],"unusedIngredients":[]},{"vegetarian":"false","vegan":"false","glutenFree":"true","dairyFree":"false","veryHealthy":"false","cheap":"false","veryPopular":"false","sustainable":"false","weightWatcherSmartPoints":1,"gaps":"no","lowFodmap":"false","ketogenic":"false","whole30":"false","preparationMinutes":10,"cookingMinutes":20,"sourceUrl":"http://www.closetcooking.com/2018/03/parmesan-roasted-carrot-fries.html","spoonacularSourceUrl":"https://spoonacular.com/parmesan-roasted-carrot-fries-991414","aggregateLikes":220,"spoonacularScore":66.0,"healthScore":8.0,"creditsText":"Closet Cooking","sourceName":"Closet Cooking","pricePerServing":44.79,"id":991414,"title":"Parmesan Roasted Carrot Fries","readyInMinutes":30,"servings":6,"image":"https://spoonacular.com/recipeImages/991414-312x231.jpg","imageType":"jpg","cuisines":["American"],"dishTypes":["side dish"],"diets":["gluten free"],"occasions":[],"winePairing":{"pairedWines":[],"pairingText":"","productMatches":[]},"analyzedInstructions":[{"name":"","steps":[{"number":1,"step":"Gently toss the carrot fries in the oil, salt and pepper, sprinkle on the cheese and mix to coat before spreading on them in a single layer on a silicon mat or parchment paper lined baking sheet.","ingredients":[{"id":1102047,"name":"salt and pepper","image":"salt-and-pepper.jpg"},{"id":11124,"name":"carrot","image":"sliced-carrot.png"},{"id":4582,"name":"cooking oil","image":"vegetable-oil.jpg"}],"equipment":[{"id":404770,"name":"baking paper","image":"baking-paper.jpg"},{"id":404727,"name":"baking sheet","image":"baking-sheet.jpg"}]},{"number":2,"step":"Roast in a a preheated 425F/220C oven until tender and lightly charred, about 16-20 minutes, mixing half way through.","ingredients":[],"equipment":[{"id":404784,"name":"oven","image":"oven.jpg","temperature":{"number":425.0,"unit":"Fahrenheit"}}],"length":{"number":20,"unit":"minutes"}}]}],"usedIngredientCount":1,"missedIngredientCount":3,"likes":0,"missedIngredients":[{"id":4582,"amount":1.0,"unit":"tablespoon","unitLong":"tablespoon","unitShort":"Tbsp","aisle":"Oil, Vinegar, Salad Dressing","name":"oil","original":"1 tablespoon oil","originalString":"1 tablespoon oil","originalName":"oil","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/vegetable-oil.jpg"},{"id":1033,"amount":0.5,"unit":"cup","unitLong":"cups","unitShort":"cup","aisle":"Cheese","name":"parmigiano reggiano","original":"1/2 cup parmigiano reggiano (parmesan cheese), grated","originalString":"1/2 cup parmigiano reggiano (parmesan cheese), grated","originalName":"parmigiano reggiano (parmesan cheese), grated","metaInformation":["grated","(parmesan cheese)"],"image":"https://spoonacular.com/cdn/ingredients_100x100/parmesan.jpg"},{"id":1102047,"amount":6.0,"unit":"servings","unitLong":"servings","unitShort":"servings","aisle":"Spices and Seasonings","name":"salt and pepper","original":"salt and pepper to taste","originalString":"salt and pepper to taste","originalName":"salt and pepper to taste","metaInformation":["to taste"],"image":"https://spoonacular.com/cdn/ingredients_100x100/salt-and-pepper.jpg"}],"usedIngredients":[{"id":11124,"amount":2.0,"unit":"pounds","unitLong":"pounds","unitShort":"lb","aisle":"Produce","name":"carrots","original":"2 pounds carrots, peeled and sliced into 1/4 in thick 'fries'","originalString":"2 pounds carrots, peeled and sliced into 1/4 in thick 'fries'","originalName":"carrots, peeled and sliced into 1/4 in thick 'fries'","metaInformation":["thick","peeled","sliced into 1/4 in  'fries'"],"image":"https://spoonacular.com/cdn/ingredients_100x100/sliced-carrot.png"}],"unusedIngredients":[]},{"vegetarian":"true","vegan":"false","glutenFree":"true","dairyFree":"false","veryHealthy":"false","cheap":"false","veryPopular":"false","sustainable":"false","weightWatcherSmartPoints":4,"gaps":"no","lowFodmap":"true","ketogenic":"false","whole30":"false","preparationMinutes":15,"cookingMinutes":15,"sourceUrl":"https://www.tasteofhome.com/recipes/sweet-candied-carrots","spoonacularSourceUrl":"https://spoonacular.com/sweet-candied-carrots-938032","aggregateLikes":11,"spoonacularScore":37.0,"healthScore":4.0,"creditsText":"Taste of Home","sourceName":"Taste of Home","pricePerServing":28.56,"id":938032,"title":"Sweet Candied Carrots","readyInMinutes":30,"servings":8,"image":"https://spoonacular.com/recipeImages/938032-312x231.jpg","imageType":"jpg","cuisines":[],"dishTypes":["side dish"],"diets":["gluten free","lacto ovo vegetarian","fodmap friendly"],"occasions":[],"winePairing":{},"analyzedInstructions":[{"name":"","steps":[{"number":1,"step":"Place carrots in a large saucepan; add 1 in. of water. Bring to a boil. Reduce heat; cover and simmer for 8-10 minutes or until crisp-tender.","ingredients":[{"id":11124,"name":"carrot","image":"sliced-carrot.png"}],"equipment":[{"id":404669,"name":"sauce pan","image":"sauce-pan.jpg"}],"length":{"number":10,"unit":"minutes"}},{"number":2,"step":"Drain and set aside.","ingredients":[],"equipment":[]},{"number":3,"step":"In the same pan, combine the butter, brown sugar, salt and pepper; cook and stir until butter is melted. Return carrots to the pan; cook and stir over medium heat for 5 minutes or until glazed.","ingredients":[{"id":1102047,"name":"salt and pepper","image":"salt-and-pepper.jpg"},{"id":19334,"name":"brown sugar","image":"dark-brown-sugar.png"},{"id":11124,"name":"carrot","image":"sliced-carrot.png"},{"id":1001,"name":"butter","image":"butter-sliced.jpg"}],"equipment":[{"id":404645,"name":"frying pan","image":"pan.png"}],"length":{"number":5,"unit":"minutes"}}]}],"usedIngredientCount":1,"missedIngredientCount":4,"likes":0,"missedIngredients":[{"id":19334,"amount":0.25,"unit":"cup","unitLong":"cups","unitShort":"cup","aisle":"Baking","name":"brown sugar","original":"1/4 cup packed brown sugar","originalString":"1/4 cup packed brown sugar","originalName":"packed brown sugar","metaInformation":["packed"],"image":"https://spoonacular.com/cdn/ingredients_100x100/dark-brown-sugar.png"},{"id":1001,"amount":0.25,"unit":"cup","unitLong":"cups","unitShort":"cup","aisle":"Milk, Eggs, Other Dairy","name":"butter","original":"1/4 cup butter","originalString":"1/4 cup butter","originalName":"butter","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg"},{"id":2047,"amount":0.25,"unit":"teaspoon","unitLong":"teaspoons","unitShort":"tsp","aisle":"Spices and Seasonings","name":"salt","original":"1/4 teaspoon salt","originalString":"1/4 teaspoon salt","originalName":"salt","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/salt.jpg"},{"id":2032,"amount":0.125,"unit":"teaspoon","unitLong":"teaspoons","unitShort":"tsp","aisle":"Spices and Seasonings","name":"white pepper","original":"1/8 teaspoon white pepper","originalString":"1/8 teaspoon white pepper","originalName":"white pepper","metaInformation":["white"],"image":"https://spoonacular.com/cdn/ingredients_100x100/white-pepper.png"}],"usedIngredients":[{"id":11124,"amount":2.0,"unit":"pounds","unitLong":"pounds","unitShort":"lb","aisle":"Produce","name":"carrots","original":"2 pounds carrots, cut into sticks","originalString":"2 pounds carrots, cut into sticks","originalName":"carrots, cut into sticks","metaInformation":["cut into sticks"],"image":"https://spoonacular.com/cdn/ingredients_100x100/sliced-carrot.png"}],"unusedIngredients":[]},{"vegetarian":"true","vegan":"true","glutenFree":"true","dairyFree":"true","veryHealthy":"false","cheap":"false","veryPopular":"true","sustainable":"false","weightWatcherSmartPoints":2,"gaps":"no","lowFodmap":"true","ketogenic":"false","whole30":"true","preparationMinutes":10,"cookingMinutes":30,"sourceUrl":"http://www.foodnetwork.com/recipes/ina-garten/roasted-carrots-recipe-1940444","spoonacularSourceUrl":"https://spoonacular.com/roasted-carrots-968871","aggregateLikes":694,"spoonacularScore":86.0,"healthScore":16.0,"creditsText":"Foodnetwork","sourceName":"Foodnetwork","pricePerServing":30.92,"id":968871,"title":"Roasted Carrots","readyInMinutes":40,"servings":6,"cuisines":[],"dishTypes":["side dish"],"diets":["gluten free","dairy free","paleolithic","lacto ovo vegetarian","primal","fodmap friendly","whole 30","vegan"],"occasions":[],"winePairing":{},"analyzedInstructions":[{"name":"","steps":[{"number":1,"step":"Watch how to make this recipe.","ingredients":[],"equipment":[]},{"number":2,"step":"Preheat the oven to 400 degrees F.","ingredients":[],"equipment":[{"id":404784,"name":"oven","image":"oven.jpg","temperature":{"number":400.0,"unit":"Fahrenheit"}}]},{"number":3,"step":"If the carrots are thick, cut them in half lengthwise; if not, leave whole. Slice the carrots diagonally in 1 1/2-inch-thick slices. (The carrots will shrink while cooking so make the slices big.) Toss them in a bowl with the olive oil, salt, and pepper.","ingredients":[{"id":4053,"name":"olive oil","image":"olive-oil.jpg"},{"id":11124,"name":"carrot","image":"sliced-carrot.png"},{"id":1002030,"name":"pepper","image":"pepper.jpg"},{"id":2047,"name":"salt","image":"salt.jpg"}],"equipment":[{"id":404783,"name":"bowl","image":"bowl.jpg"}]},{"number":4,"step":"Transfer to a sheet pan in 1 layer and roast in the oven for 20 minutes, until browned and tender.","ingredients":[],"equipment":[{"id":404784,"name":"oven","image":"oven.jpg"},{"id":404645,"name":"frying pan","image":"pan.png"}],"length":{"number":20,"unit":"minutes"}},{"number":5,"step":"Toss the carrots with minced dill or parsley, season to taste, and serve.","ingredients":[{"id":11124,"name":"carrot","image":"sliced-carrot.png"},{"id":2045,"name":"dill","image":"dill.jpg"}],"equipment":[]}]}],"usedIngredientCount":1,"missedIngredientCount":4,"likes":0,"missedIngredients":[{"id":1002030,"amount":0.5,"unit":"teaspoons","unitLong":"teaspoons","unitShort":"tsp","aisle":"Spices and Seasonings","name":"black pepper","original":"1/2 teaspoons freshly ground black pepper","originalString":"1/2 teaspoons freshly ground black pepper","originalName":"freshly ground black pepper","metaInformation":["black","freshly ground"],"image":"https://spoonacular.com/cdn/ingredients_100x100/pepper.jpg"},{"id":2045,"amount":2.0,"unit":"tablespoons","unitLong":"tablespoons","unitShort":"Tbsp","aisle":"Produce;Spices and Seasonings","name":"fresh dill","original":"2 tablespoons minced fresh dill or parsley","originalString":"2 tablespoons minced fresh dill or parsley","originalName":"minced fresh dill or parsley","metaInformation":["fresh","minced"],"image":"https://spoonacular.com/cdn/ingredients_100x100/dill.jpg"},{"id":1082047,"amount":1.25,"unit":"teaspoons","unitLong":"teaspoons","unitShort":"tsp","aisle":"Spices and Seasonings","name":"kosher salt","original":"1 1/4 teaspoons kosher salt","originalString":"1 1/4 teaspoons kosher salt","originalName":"kosher salt","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/salt.jpg"},{"id":4053,"amount":3.0,"unit":"tablespoons","unitLong":"tablespoons","unitShort":"Tbsp","aisle":"Oil, Vinegar, Salad Dressing","name":"olive oil","original":"3 tablespoons good olive oil","originalString":"3 tablespoons good olive oil","originalName":"good olive oil","metaInformation":["good"],"image":"https://spoonacular.com/cdn/ingredients_100x100/olive-oil.jpg"}],"usedIngredients":[{"id":11124,"amount":12.0,"unit":"","unitLong":"","unitShort":"","aisle":"Produce","name":"carrots","original":"12 carrots","originalString":"12 carrots","originalName":"carrots","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/sliced-carrot.png"}],"unusedIngredients":[],"image":"https://spoonacular.com/recipeImages/968871-312x231.jpg","imageType":"jpg"},{"vegetarian":"true","vegan":"false","glutenFree":"true","dairyFree":"false","veryHealthy":"false","cheap":"false","veryPopular":"false","sustainable":"false","weightWatcherSmartPoints":3,"gaps":"no","lowFodmap":"true","ketogenic":"false","whole30":"false","preparationMinutes":1,"cookingMinutes":13,"sourceUrl":"https://lmld.org/sweet-glazed-carrots/","spoonacularSourceUrl":"https://spoonacular.com/brown-sugar-glazed-carrots-1101577","aggregateLikes":1,"spoonacularScore":32.0,"healthScore":4.0,"creditsText":"Like Mother, Like Daughter","sourceName":"Like Mother, Like Daughter","pricePerServing":28.04,"id":1101577,"title":"Brown Sugar Glazed Carrots","readyInMinutes":14,"servings":4,"image":"https://spoonacular.com/recipeImages/1101577-312x231.jpg","imageType":"jpg","cuisines":[],"dishTypes":["side dish"],"diets":["gluten free","lacto ovo vegetarian","fodmap friendly"],"occasions":["easter"],"winePairing":{"pairedWines":[],"pairingText":"","productMatches":[]},"analyzedInstructions":[{"name":"","steps":[{"number":1,"step":"Fill a large pot with a couple inches of water and bring to a boil over medium high heat (or prepare your steamer and put your steam insert over the top) and cook your carrots for about 8 minutes, or until fork tender.","ingredients":[{"id":11124,"name":"carrot","image":"sliced-carrot.png"}],"equipment":[{"id":404752,"name":"pot","image":"stock-pot.jpg"}],"length":{"number":8,"unit":"minutes"}},{"number":2,"step":"Drain the water from the pan and add the butter, brown sugar, salt, and pepper and stir until the butter is melted, brown sugar is dissolced.","ingredients":[{"id":19334,"name":"brown sugar","image":"dark-brown-sugar.png"},{"id":1001,"name":"butter","image":"butter-sliced.jpg"},{"id":1002030,"name":"pepper","image":"pepper.jpg"},{"id":2047,"name":"salt","image":"salt.jpg"}],"equipment":[{"id":404645,"name":"frying pan","image":"pan.png"}]},{"number":3,"step":"Cook the carrots in the glaze for about 5 minutes, stirring occasionally to coat them in the glaze nicely.","ingredients":[{"id":11124,"name":"carrot","image":"sliced-carrot.png"}],"equipment":[],"length":{"number":5,"unit":"minutes"}}]}],"usedIngredientCount":1,"missedIngredientCount":4,"likes":0,"missedIngredients":[{"id":1001,"amount":2.0,"unit":"Tbs","unitLong":"Tbs","unitShort":"Tbs","aisle":"Milk, Eggs, Other Dairy","name":"butter","original":"2 Tbs butter (1/2 stick)","originalString":"2 Tbs butter (1/2 stick)","originalName":"butter (1/2 stick)","metaInformation":["()"],"image":"https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg"},{"id":19334,"amount":2.0,"unit":"Tbs","unitLong":"Tbs","unitShort":"Tbs","aisle":"Baking","name":"brown sugar","original":"2 Tbs brown sugar","originalString":"2 Tbs brown sugar","originalName":"brown sugar","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/dark-brown-sugar.png"},{"id":2047,"amount":0.25,"unit":"tsp","unitLong":"teaspoons","unitShort":"tsp","aisle":"Spices and Seasonings","name":"salt","original":"1/4 tsp salt","originalString":"1/4 tsp salt","originalName":"salt","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/salt.jpg"},{"id":1002030,"amount":1.0,"unit":"dash","unitLong":"dash","unitShort":"dash","aisle":"Spices and Seasonings","name":"pepper","original":"1 dash pepper","originalString":"1 dash pepper","originalName":"pepper","metaInformation":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/pepper.jpg"}],"usedIngredients":[{"id":11124,"amount":1.0,"unit":"pound","unitLong":"pound","unitShort":"lb","aisle":"Produce","name":"carrots","original":"1 pound carrots (peeled and sliced into thin 3-4 inch pieces, or use baby carrots)","originalString":"1 pound carrots (peeled and sliced into thin 3-4 inch pieces, or use baby carrots)","originalName":"carrots (peeled and sliced into thin 3-4 inch pieces, or use baby carrots)","metaInformation":["peeled","sliced into thin 3-4 inch pieces, or use baby carrots)"],"image":"https://spoonacular.com/cdn/ingredients_100x100/sliced-carrot.png"}],"unusedIngredients":[]}],"offset":0,"number":5,"totalResults":18501}
        return jsonify({"data": res})
    else: 
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

@app.route('/api/getIngredients', methods=["POST"])
def get_ingredients():
    print(request.method)
    if DEBUGGER == True: 
        res = {"ingredients":[{"name":"diced bacon strips","image":"raw-bacon.png","amount":{"metric":{"value":2.0,"unit":""},"us":{"value":2.0,"unit":""}}},{"name":"brown sugar","image":"dark-brown-sugar.png","amount":{"metric":{"value":4.0,"unit":"tsps"},"us":{"value":4.0,"unit":"tsps"}}},{"name":"carrots","image":"sliced-carrot.png","amount":{"metric":{"value":4.0,"unit":"medium"},"us":{"value":4.0,"unit":"medium"}}},{"name":"onion","image":"brown-onion.png","amount":{"metric":{"value":40.0,"unit":"ml"},"us":{"value":0.25,"unit":"cup"}}},{"name":"pepper","image":"pepper.jpg","amount":{"metric":{"value":0.125,"unit":"tsps"},"us":{"value":0.125,"unit":"tsps"}}}]}
        print(res)
        return jsonify({"data": res})
    else: 
        data = request.get_json()
        print(data)
        recipe_id = data.get('id')
        api_url = "https://api.spoonacular.com/recipes/{recipe_id}/ingredientWidget.json?apiKey={api_key}"
        get_url = api_url.format(api_key=token, recipe_id=recipe_id)
        response = requests.get(get_url)
        if response.status_code == 200:
            res = response.json()
            return jsonify({"data": res})
        else: 
            return jsonify({"error": "API error"})

@app.route('/api/getInstructions', methods=["POST"])
def get_instructions():
    if DEBUGGER == True: 
        res = [{"name":"","steps":[{"number":1,"step":"Place carrots in a small saucepan; cover with water. Bring to a boil. Reduce heat; cover and simmer for 7-9 minutes or until tender.","ingredients":[{"id":11124,"name":"carrot","image":"sliced-carrot.png"}],"equipment":[{"id":404669,"name":"sauce pan","image":"sauce-pan.jpg"}],"length":{"number":9,"unit":"minutes"}},{"number":2,"step":"Meanwhile, in a small skillet, cook bacon over medium heat until crisp. Remove with a slotted spoon to paper towels; drain, reserving 2 teaspoons drippings. Saute onion in the drippings. Stir in brown sugar and pepper until brown sugar is melted.","ingredients":[{"id":19334,"name":"brown sugar","image":"dark-brown-sugar.png"},{"id":1002030,"name":"pepper","image":"pepper.jpg"},{"id":10123,"name":"bacon","image":"raw-bacon.png"},{"id":11282,"name":"onion","image":"brown-onion.png"}],"equipment":[{"id":404636,"name":"slotted spoon","image":"slotted-spoon.jpg"},{"id":405895,"name":"paper towels","image":"paper-towels.jpg"},{"id":404645,"name":"frying pan","image":"pan.png"}]},{"number":3,"step":"Drain carrots; toss with onion mixture. Top with bacon.","ingredients":[{"id":11124,"name":"carrot","image":"sliced-carrot.png"},{"id":10123,"name":"bacon","image":"raw-bacon.png"},{"id":11282,"name":"onion","image":"brown-onion.png"}],"equipment":[]}]}]
        return jsonify({"data": res})
    else: 
        data = request.get_json()
        recipe_id = data.get('id')
        api_url = "https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions?apiKey={api_key}&stepBreakdown=false"
        get_url = api_url.format(api_key=token, recipe_id=recipe_id)
        response = requests.get(get_url)
        if response.status_code == 200:
            res = response.json()
            return jsonify({"data" : res})
        else: 
            return jsonify({"error" : "API error"})


@app.route('/api/newUser', methods=["POST"])
def newUser(): 
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    token = str(randint(1000000000,9999999999))
    with sqlite3.connect('data.db') as connection: 
        cursor = connection.cursor()
        SQL = """INSERT INTO accounts (username, password, token)
            VALUES (?,?,?);"""
        cursor.execute(SQL, (username, password, token))
        SQL = """ SELECT id, token FROM accounts WHERE username=?;"""
        info = cursor.execute(SQL, (username, )).fetchone()
        info_json = json.dumps(info)
        return Response(info_json)

@app.route('/api/logIn', methods=["POST"])
def logIn():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        SQL = "SELECT id, token FROM accounts WHERE username=? AND password=?;"
        info = cursor.execute(SQL, (username, password)).fetchone()
        info_json = json.dumps(info)
        return Response(info_json)


@app.route('/api/saveRecipe', methods=["POST"])
def saveRecipe():
    data = request.get_json()
    recipe_id = data.get('recipeID')
    recipe_title = data.get('title')
    recipe_image = data.get('image')
    account_id = data.get('accountID')
    with sqlite3.connect('data.db') as connection: 
        cursor = connection.cursor()
        SQL = """ INSERT INTO recipes (recipe_id, recipe_title, recipe_image, account_id) 
            VALUES (?,?,?,?);"""
        cursor.execute(SQL, (recipe_id, recipe_title, recipe_image, account_id))
        return jsonify({"recipe save": "success"})

@app.route('/api/unsaveRecipe', methods=["POST"])
def unsaveRecipe():
    data = request.get_json()
    recipe_id = data.get('recipeID')
    account_id = data.get('accountID')
    with sqlite3.connect('data.db') as connection: 
        cursor = connection.cursor()
        SQL = """ DELETE FROM recipes WHERE recipe_id=? AND account_id=?;"""
        cursor.execute(SQL, (recipe_id, account_id))
        return jsonify({"recipe unsave": "success"})

@app.route('/api/popularRecipes', methods=["POST"])
def popular_recipes():
    if DEBUGGER == True: 
        with open("popularRecipes.json", "r") as json_object:
            res = json.load(json_object)
            return jsonify({'data': res})
    else: 
        data = request.get_json()
        number = data.get('number')
        api_url = "https://api.spoonacular.com/recipes/random?apiKey={api_key}&number={number}"
        get_url = api_url.format(api_key=token, number=number)
        response = requests.get(get_url)
        if response.status_code == 200:
            res = response.json()
            return jsonify({"data" : res})
        else: 
            return jsonify({"error" : "API error"})

@app.route('/api/myRecipes', methods=['POST'])
def get_my_recipes(): 
    data = request.get_json()
    account_id = data.get('id')
    with sqlite3.connect('data.db') as connection: 
        cursor = connection.cursor()
        SQL = """ SELECT * FROM recipes WHERE account_id=?"""
        info = cursor.execute(SQL, (account_id,)).fetchall()
        res = []
        for row in info:
            data = {}
            data['pk'] = row[0]
            data['id'] = row[1]
            data['image'] = row[2]
            data['title'] = row[3]
            res.append(data)
        print(res)
        return jsonify({"data": res})
        




if __name__ == "__main__":
    app.run(debug=True)