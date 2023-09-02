from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Drink, Drink_schema, Drinks_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}

@api.route('/drink', methods = ['POST'])
@token_required
def create_drink(current_user_token):
    name = request.json['name']
    alc_percentage = request.json['alcohol percentage']
    tequila_type = request.json['tequila type']
    origin = request.json['origin']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    drink = Drink(name, alc_percentage, tequila_type, origin, user_token = user_token )

    db.session.add(drink)
    db.session.commit()

    response = Drinks_schema.dump(drink)
    return jsonify(response)