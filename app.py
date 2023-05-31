from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS
from src.user import daoUser as userUC
from src.login import loginUseCases
from src.register import registerUseCases
from src.posts import postUseCases

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173", "allow_headers": "Content-Type, Authorization",
                                 "expose_headers": "Access-Control-Allow-Headers"}})


@app.route('/api/entities')
@cross_origin()
def get_all_entities():  # put application's code here
    return userUC.get_users()


@app.route('/api/login', methods=['POST'])
@cross_origin()
def login():
    user = request.get_json()
    username = user['username']
    pdw = user['pdw']
    print(user)
    return loginUseCases.login(username, pdw)


@app.route('/api/register', methods=['POST'])
@cross_origin()
def register():
    user = request.get_json()
    username = user['username']
    pdw = user['pdw']
    print(user)
    return registerUseCases.create_user(username, pdw)


@app.route('/api/addPost', methods=['POST'])
@cross_origin()
def add_post():
    post = request.get_json()
    username = post['username']
    content = post['content']
    return postUseCases.add_post(username, content)

@app.route('/api/listPostByUsername/<string:username>')
@cross_origin()
def list_post_by_username(username):
    return postUseCases.get_posts_by_username(username)


if __name__ == '__main__':
    app.run()
