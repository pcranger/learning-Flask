from flask import Flask, request
# request: filtering types of requests data
from flask_restful import Api
# flask_restful automatically convert dict to json, so jsonify is not needed
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'Hieu'
api = Api(app)
# app secrerity key(jwt token)
# when a function is sent jwt token, the user have that token will have access to that function cause he logged in
jwt = JWT(app, authenticate, identity)
# jwt creates new endpoints /auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
