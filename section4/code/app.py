from flask import Flask
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
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item


# define how the path for the resource
api.add_resource(Item, '/item/<string:name>')
app.run(port=5000)
