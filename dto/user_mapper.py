from dto.user_output_dto import UserOutputDto
from entity.user import User
from multipledispatch import dispatch
from flask_restful.reqparse import Namespace

@dispatch(object)
def to_dto(entity):
    return UserOutputDto(
        entity.name,
        entity.email,
        entity.id
    )

@dispatch(list)
def to_dto(entities):
    for i in range(len(entities)):
        entities[i] = to_dto(entities[i])

    return entities

@dispatch(Namespace)
def to_entity(args):
    return User(args['name'], args['email'], args['password'])