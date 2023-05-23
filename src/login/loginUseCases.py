from src.login.loginUserModel import LoginUser
from src.conexionbdd import useCasesDatabase as db


def login(username, pdw):
    newUser = LoginUser()
    newUser.set_username(username)
    newUser.set_pdw(pdw)
    if db.login_user(newUser.get_username(), newUser.get_pdw()):
        return {
            'message': 'Inicio exitoso',
            'token': 'Token Generado'
        }
    else:
        return {
            'message': 'Login Incorrecto'
        }
