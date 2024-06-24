from flask_restful import reqparse, Resource

from service.todo_service import TodoService

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

service = TodoService()

class TodoById(Resource):

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}

        updated_todo = service.update(todo_id, task)

        return updated_todo, 200
    
    def get(self, todo_id):
        return service.get_by_id(todo_id)

    def delete(self, todo_id):
        service.delete(todo_id)
        return [], 204

class Todos(Resource):

    def get(self):
        return service.get()

    def post(self):
        args = parser.parse_args()
        task = {'task': args['task']}
        saved_todo = service.create(task)
        return saved_todo, 201