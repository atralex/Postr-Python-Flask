class User:
    def __init__(self):
        self._id
        self._username
        self._pdw

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_username(self, username):
        self._username = username

    def get_username(self):
        return self._username

    def set_pdw(self, pdw):
        self._pdw = pdw

    def get_pdw(self):
        return self._pdw

    def get_usuario(self):
        return {
            'id': self._id,
            'username': self._username,
            'pdw': self._pdw
        }