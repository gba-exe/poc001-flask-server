
from flask import Flask
from flask_restful import Api, Resource

from controller.todo_controller import TodoById, Todos

app = Flask(__name__)
api = Api(app)

api.add_resource(Todos, '/todos')
api.add_resource(TodoById, '/todos/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)