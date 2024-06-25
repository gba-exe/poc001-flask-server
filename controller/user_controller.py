from flask import json
from flask_restful import Resource, reqparse

from dto.user_mapper import to_dto, to_entity
from entity.user import User
from service.user_service import UserService
from utils.json import to_json

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('email', type=str, required=True)
parser.add_argument('password', type=str, required=True)

service = UserService()

class Users(Resource):

    def get(self):
        users = service.get()

        if not users:
            return [], 204

        users_dto = to_dto(users)

        return to_json(users_dto), 200

    def post(self):
        args = parser.parse_args()
        
        user =  User(args['name'], args['email'], args['password'])

        saved_user = service.create(user)

        return to_json(to_dto(saved_user)), 201

class UserById(Resource):
    
    def get(self, id):
        user = service.get_by_id(id)

        user_dto = to_dto(user)

        return to_json(user_dto), 200

    def put(self, id):
        args = parser.parse_args()
        
        user = User(args['name'], args['email'], args['password'])

        updated_user = service.update(id, user)

        return to_json(to_dto(updated_user)), 200

    def delete(self, id):
        service.delete(id)

        return [], 204

class UserLogin(Resource):

    def post(self):
        args = parser.parse_args()

        return service.login(args['email'], args['password']), 200
