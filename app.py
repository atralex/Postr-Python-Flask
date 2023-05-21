from flask import Flask
from flask_cors import cross_origin
from src.user import daoUser as userUC

app = Flask(__name__)


@app.route('/api/entities')
@cross_origin()
def hello_world(): # put application's code here
    return userUC.get_users()

@app.route('/api/crear')
@cross_origin()
def set_mock_user():
    userUC.create_user()
    return {
        'code': 200
    }

if __name__ == '__main__':
    app.run()
