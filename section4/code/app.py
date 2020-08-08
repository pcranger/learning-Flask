from flask import Flask, request
# request: filtering types of requests data
from flask_restful import Resource, Api
# flask_restful automatically convert dict to json, so jsonify is not needed
app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404  # if the item name  cannot be found

    def post(self, name):
        data = request.get_json()  # accept only json type data
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'item': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
