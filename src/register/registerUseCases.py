from src.register.userRegisterModel import RegisterUser
from src.conexionbdd import useCasesDatabase as db


def create_user(username, pdw):
    new_user = RegisterUser()
    new_user.set_username(username)
    new_user.set_pdw(pdw)
    if db.add_user(new_user.get_username(), new_user.get_pdw()):
        return {
            'message': 'Registro Existoso'
        }
    else:
        return {
            'message': 'Registro Incorrecto'
        }
