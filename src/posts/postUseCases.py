from flask import jsonify
from src.posts.postModel import Post
from src.conexionbdd import useCasesDatabase as db

def add_post(username, content):
    db.add_post(username, content)
    return {
        'Message': 'Post Added Successfully'
    }

def get_posts_by_id(id):
    users = []
    db.add_post()
    data = db.get_post_by_id(id)
    for row in data:
        post = Post
        adapt_post(post, row)
        users.append(post.get_post())
    return jsonify(users)

def adapt_post(post, row):
    post.set_user_id(row[0])
    post.set_content(row[1])
