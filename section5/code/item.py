import sqlite3
from flask_jwt import jwt_required, current_identity
from flask_restful import Resource, reqparse


class Item(Resource):
    # /item/<string:name>
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank"
                        )

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return {'message': 'Item not found'}, 404

    def post(self, name):
        # call the get method above to check database, but get method requre jwt token, so we seperate the find_by_name to different method, and call it from both get and post
        if self.find_by_name(name):
            # if found an item and it's not None
            return {'message': "An item with name '{}' already exists. for".format(name)}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        connection = sqlite3.connect(data.db)
        cursor = connection.cursor()

        query = "INSERT INTO items VALUTES (?,?)"

        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        # create a new list without the item and overwrite the existing list with this
        return {'message': 'Item deleted'}

    def put(self, name):

        data = Item.parser.parse_args()

        # prevent adding item without a price by looking at json payload
        parser = reqparse.RequestParser()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            items.update(data)
        return item


class ItemList(Resource):
    # /items
    def get(self):
        return {'item': items}
