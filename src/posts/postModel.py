class Post:
    def __init__(self):
        self._user_id
        self._content
    def set_user_id(self, user_id):
        self._user_id = user_id

    def get_user_id(self):
        return self._user_id

    def set_content(self, content):
        self._content = content

    def get_content(self):
        return self._content

    def get_post(self):
        return {
            'user_id': self._user_id,
            'content': self._content
        }