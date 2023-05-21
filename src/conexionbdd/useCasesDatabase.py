from src.conexionbdd.databaseConexion import cur, conn


def get_users():
    cur.execute("SELECT * FROM usuarios")
    data = cur.fetchall()
    return data


def add_user(id, username, pdw):
    cur.execute("INSERT INTO `usuarios` (id, username, pdw) VALUES (%s, %s, %s);", (id, username, pdw))
    conn.commit()
    cur.close()
