class LoginUser:
    def __init__(self):
        self._pdw = None
        self._username = None


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
            'username': self._username,
            'pdw': self._pdw
        }