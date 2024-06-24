from flask_restful import abort
from repository.todo_repository import TodoRepository


class TodoService():
    db = TodoRepository()

    def get(self):
        return self.db.get()

    def get_by_id(self, todo_id):
        todo = self.db.get_by_id(todo_id)
        if todo == None:
            abort(404)

        return todo

    def create(self, task):
        return self.db.add(task)

    def update(self, todo_id, task):
        updated_todo = self.db.update(todo_id, task)

        if updated_todo == None:
            abort(404)
        
        return updated_todo

    def delete(self, todo_id):
        self.db.delete(todo_id)