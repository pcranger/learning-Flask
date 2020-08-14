from flask import Flask, request
# request: filtering types of requests data
from flask_restful import Resource, Api, reqparse
# flask_restful automatically convert dict to json, so jsonify is not needed
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity
app = Flask(__name__)
app.secret_key = 'Hieu'
api = Api(app)
# app secrerity key(jwt token)
# when a function is sent jwt token, the user have that token will have access to that function cause he logged in
jwt = JWT(app, authenticate, identity)
# jwt creates new endpoints /auth

items = []

# item is a resource, it can get, post


class Item(Resource):
    # /item/<string:name>
    @jwt_required()
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

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        # create a new list without the item and overwrite the existing list with this
        return {'message': 'Item deleted'}

    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    # /items
    def get(self):
        return {'item': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
