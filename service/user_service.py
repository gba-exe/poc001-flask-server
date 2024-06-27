import re
from flask_restful import abort
from entity.user import User
from repository.user_repository import UserRepository


class UserService():
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    passwd_regex = '^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*[!#$%&? "*@-]).*$'

    repository = UserRepository()

    def get(self):
        return self.repository.get()
    
    def get_by_id(self, user_id: int):
        user = self.repository.get_by_id(user_id)
        if user == None:
            abort(404, message="Usuario nao encontrado")

        return user

    def create(self, user: User):
        self.__validate(user.email, user.password)

        if user.name == None:
            abort(400, message="Nome e obrigatorio")

        if (self.repository.exists_by_email(user.email)):
            abort(409, message="Email ja cadastrado")

        return self.repository.add(user)

    def delete(self, user_id):
        if self.repository.exists_by_id(user_id):
            abort(404, message="Usuario nao encontrado")

        self.repository.delete(user_id)
    
    def update(self, user_id, user):
        self.__validate(user.email, user.password)

        user.id = int(user_id)

        updated_user = self.repository.update(user_id, user)

        if updated_user == None:
            abort(404, message="Usuario nao encontrado")

        return updated_user

    def login(self, email, password):
        user = self.repository.get_by_email(email)

        if user == None:
            return False

        if user.password != password:
            return False

        return True

    def __validate(self, email, password):

        if (email == None or len(email) < 1):
            abort(400, message="Email e obrigatorio")

        if (password == None or len(password) < 1):
            abort(400, message="Senha e obrigatoria")

        if (not re.fullmatch(self.email_regex, email)):
            abort(400, message="Email invalido")

        if (not re.fullmatch(self.passwd_regex, password)):
            abort(400, message="Senha invalida")
