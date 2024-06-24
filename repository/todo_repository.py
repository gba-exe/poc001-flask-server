class TodoRepository():
    todos =  {
        'todo1': {'task': 'build an API'},
        'todo2': {'task': '?????'},
        'todo3': {'task': 'profit!'},
    }

    cur_id = 4;

    def __init__(self, todos={}):
        if todos != {}:
            self.todos = todos
            self.cur_id = 0

    def get(self):
        return self.todos
    
    def get_by_id(self, todo_id):
        try:
            return self.todos[todo_id]
        except Exception:
            return None

    def add(self, task):
        try:
            todo_id = "todo%d" % self.cur_id
            self.todos[todo_id] = task

            self.cur_id+=1
            return self.todos[todo_id]
        except Exception:
            return None

    def delete(self, todo_id):
        del self.todos[todo_id]

    def update(self, todo_id, task):
        try:
            self.todos[todo_id] = task
        except Exception:
            return None 

        return self.todos[todo_id]

        