import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get('https://botw-compendium.herokuapp.com/api/v3/compendium/category/creatures').json()
    food_data = [food for food in response['data'] if food['edible'] is True]

    return food_data
