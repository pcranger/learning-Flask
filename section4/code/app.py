from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)  # define api


class Student(Resource):  # define resource
    def get(self, name):  # define method of this resource
        return {'student': name}  # define what this method do


# define how the path for the resource
api.add_resource(Student, '/student/<string:name>')
app.run(port=5000)
