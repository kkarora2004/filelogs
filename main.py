import json
from flask import Flask, jsonify, request
app = Flask(__name__)

foods = [
 { 'id': 1, 'name': 'BBQ' },
 { 'id': 2, 'name': 'chicken' },
 { 'id': 3, 'name': 'banana' }
]


nextFoodId = 4

@app.route('/foods', methods=['GET'])
def get_foods():
 return jsonify(foods)

@app.route('/foods/<int:id>', methods=['GET'])
def get_food_by_id(id: int):
 food = get_food(id)
 if food is None:
   return jsonify({ 'error': 'food does not exist'}), 404
 return jsonify(food)

def get_food(id):
 return next((f for f in foods if f['id'] == id), None)

def food_is_valid(food):
 for key in food.keys():
   if key != 'name':
    return False
 return True

@app.route('/foods', methods=['POST'])
def create_food():
    global nextFoodId
    food = request.get_json()  # <-- fix here
    if not food_is_valid(food):
        return jsonify({ 'error': 'Invalid food properties.' }), 400

    food['id'] = nextFoodId
    nextFoodId += 1
    foods.append(food)

    return '', 201, { 'location': f'/foods/{food["id"]}' }

@app.route('/foods/<int:id>', methods=['PUT'])
def update_food(id: int):
    food = get_food(id)
    if food is None:
        return jsonify({ 'error': 'food does not exist.' }), 404

    updated_food = request.get_json()  # <-- fix here
    if not food_is_valid(updated_food):
        return jsonify({ 'error': 'Invalid food properties.' }), 400

    food.update(updated_food)
    return jsonify(food)


@app.route('/foods/<int:id>', methods=['DELETE'])
def delete_food(id: int):
 global foods
 food = get_food(id)
 if food is None:
   return jsonify({ 'error': 'food does not exist.' }), 404

 foods = [f for f in foods if f['id'] != id]
 return jsonify(foods), 200

if __name__ == '__main__':
   app.run(port=5000)