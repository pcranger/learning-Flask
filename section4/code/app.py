from flask import Flask, request
# request: filtering types of requests data
from flask_restful import Resource, Api
# flask_restful automatically convert dict to json, so jsonify is not needed
app = Flask(__name__)
app.secret_key = 'Hieu'
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        # next(filter()): return the first item found from items of filer function or none if there is no item
        item = next(filter(lambda x: x['name'] == name, items), None)
        # if the item name  cannot be found
        return {'item': None}, 200 if item else 404

    def post(self, name):
        # if found an item and it's not None
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists. for".format(name)}, 400
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
