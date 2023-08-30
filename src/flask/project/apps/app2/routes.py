from apps.app2 import blueprint
from apps.app2.models import Food
from apps import db
from flask import request
import json


@blueprint.route('/')
def route_default():
    return "app2 index"


@blueprint.route('/say/<word>')
def route_test(word):
    return word


@blueprint.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    name = data['name']
    age = data['age']
    return json.dumps({name: name, age: age}), 200


@blueprint.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    food = Food(name=data['name'], price=data['price'])
    db.session.add(food)
    db.session.commit()
    return "success", 200


@blueprint.route('/read/<id>', methods=['GET'])
def read(id):
    food = Food.query.get_or_404(id)
    return f"{food.name} {food.price}", 200


@blueprint.route('/read', methods=['GET'])
def read_all():
    all_food = Food.query.all()
    return f"{len(all_food)} {all_food[1].name}", 200


@blueprint.route('/update/<id>', methods=['PATCH'])
def update(id):
    food = Food.query.get_or_404(id)
    food.price += 1000
    db.session.commit()
    return "success", 200


@blueprint.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    Food.query.filter_by(id=id).delete()
    db.session.commit()
    return "success", 200
