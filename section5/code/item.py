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

        try:
            self.insert(item)
        except:
            return {"message": "An error occured inserting the item."}, 500

        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUTES (?,?)"

        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name = ?"

        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message': 'Item deleted'}

    def put(self, name):
        # find item in db, if it exists, update it, if doesn't, insert it
        data = Item.parser.parse_args()

        item = self.find_by_name(name)  # find item
        updated_item = {'name': name, 'price': data['price']}

        if item is None:
            try:
                self.insert(updated_item)  # insert
            except:
                return {"message": "An error occured inserting the item."}, 500

        else:
            self.update(updated_item)  # update
        return item

        @classmethod
        def update(cls, item):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "UPDATE items SET price = ? WHERE name = ?"

            cursor.execute(query, (item['price'], item['name']))
            connection.commit()
            connection.close()
            return {'message': 'Item deleted'}
        # prevent adding item without a price by looking at json payload


class ItemList(Resource):
    # /items
    def get(self):
        return {'item': items}
