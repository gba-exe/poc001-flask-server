from typing import List
from entity.user import User
import copy

class UserRepository():
    users: List[User] = list()

    cur_id = 0

    def get(self):
        return copy.copy(self.users)
    
    def get_by_id(self, user_id):
        for u in self.users:
            if u.id == int(user_id):
                return copy.copy(u)

    def get_by_email(self, email):
        for u in self.users:
            if u.email == email:
                return copy.copy(u)

    def add(self, user: User):
        user.id = self.cur_id
        self.users.append(user) 

        self.cur_id += 1
        return copy.copy(user)

    def delete(self, user_id):
        i = self.get_index(user_id)
        del self.users[i]

    def update(self, user_id, user: User):
        try:
            i = self.get_index(user_id)
            self.users[i] = user
        except Exception:
            return None
        
        return copy.copy(self.users[i])
    
    def exists_by_id(self, user_id):
        return False if self.get_by_id(user_id) == None else True 

    def exists_by_email(self, email):
        for u in self.users:
            if u.email == email:
                return True
        
        return False
    
    def get_index(self, user_id):
        return copy.copy(self.users.index(self.get_by_id(user_id)))