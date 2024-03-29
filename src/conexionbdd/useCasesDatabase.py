from flask import jsonify

from src.conexionbdd.databaseConexion import cur, conn


def get_users():
    cur.execute("SELECT * FROM usuarios")
    data = cur.fetchall()
    return data


def login_user(username, pdw):
    cur.execute("SELECT * FROM `usuarios` WHERE username=%s AND pdw=%s;", (username, pdw))
    data = cur.fetchall()
    return data


def add_user(username, pdw):
    cur.execute("INSERT INTO `usuarios` (id, username, pdw) VALUES (NULL, %s, %s);", (username, pdw))
    conn.commit()
    return True


def add_post(username, content):
    cur.execute("SELECT * FROM `usuarios` WHERE username=%s;", (username,))
    data = cur.fetchall()
    user_id = data[0][0]
    cur.execute("INSERT INTO `tweets` (`id`, `user_id`, `content`, `fecha_creacion`) VALUES (NULL, %s, %s, current_timestamp());;", (user_id, content))
    conn.commit()
    return True


def get_post_by_username(username):
    cur.execute("SELECT * FROM `usuarios` WHERE username=%s;", (username,))
    user = cur.fetchall()
    user_id = user[0][0]
    cur.execute("SELECT * FROM `tweets` WHERE user_id=%s;", (user_id,))
    data = cur.fetchall()
    return data

def try_get_user_by_username(username):
    cur.execute("SELECT * FROM `usuarios` WHERE username=%s;", (username,))
    data = cur.fetchall()
    return data
