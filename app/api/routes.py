from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Drink, Drink_schema, Drinks_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}

@api.route('/tequilaprofile', methods = ['POST'])
@token_required
def create_drink(current_user_token):
    name = request.json['name']
    alc_percentage = request.json['alc_percentage']
    tequila_type = request.json['tequila_type']
    origin = request.json['origin']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    drink = Drink(name, alc_percentage, origin, tequila_type, user_token = user_token )

    db.session.add(drink)
    db.session.commit()

    response = Drink_schema.dump(drink)
    return jsonify(response)

@api.route('/tequilaprofile', methods = ['GET'])
@token_required
def get_drink(current_user_token):
    a_user = current_user_token.token
    new_drink = Drink.query.filter_by(user_token = a_user).all()
    response = Drinks_schema.dump(new_drink)
    return jsonify(response)

@api.route('/tequilaprofile/<id>', methods = ['POST','PUT'])
@token_required
def update_drink(current_user_token,id):
    drink = Drink.query.get(id) 
    print(drink)
    drink.name = request.json['name']
    print(drink.name, request.json['name'])
    drink.alc_percentage = request.json['alc_percentage']
    drink.origin = request.json['origin']
    drink.tequila_type = request.json['tequila_type']
    drink.user_token = current_user_token.token

    db.session.commit()
    response = Drink_schema.dump(drink)
    return jsonify(response)

@api.route('/tequilaprofile/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    drink = Drink.query.get(id)
    db.session.delete(drink)
    db.session.commit()
    response = Drink_schema.dump(drink)
    return jsonify(response)