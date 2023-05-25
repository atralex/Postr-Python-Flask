from flask import jsonify
from src.user.userModel import User
from src.conexionbdd import useCasesDatabase as db


def get_users():
    users = []
    data = db.get_users()
    for row in data:
        user = User
        list_user(user, row)
        users.append(user.get_usuario(user))
    return jsonify(users)


def list_user(usuario, row):
    usuario.set_id(usuario, row[0])
    usuario.set_username(usuario, row[1])
    usuario.set_pdw(usuario, row[2])

