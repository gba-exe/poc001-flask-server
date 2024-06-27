
from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

from controller.user_controller import UserById, UserLogin, Users

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

api.add_resource(Users, '/users')
api.add_resource(UserById, '/users/<int:id>')
api.add_resource(UserLogin, '/users/login')

if __name__ == '__main__':
    app.run(debug=True)