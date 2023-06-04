from src.register.userRegisterModel import RegisterUser
from src.conexionbdd import useCasesDatabase as db


def create_user(username, pdw):
    new_user = RegisterUser()
    new_user.set_username(username)
    new_user.set_pdw(pdw)
    if db.try_get_user_by_username(new_user.get_username()):
        return {
            'message': 'Usuario ya existe',
            'status': 400
        }
    else:
        if db.add_user(new_user.get_username(), new_user.get_pdw()):
            return {
                'message': 'Registro Existoso',
                'status': 200
            }
        else:
            return {
                'message': 'Registro Incorrecto',
                'status': 400
            }
