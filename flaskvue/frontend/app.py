from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# @app.route('/books', methods=['GET'])
# def all_books():

#     BOOKS = [
#         {
#             'title': 'On the Road',
#             'author': 'Jack Kerouac',
#             'read': True
#         },
#         {
#             'title': 'Harry Potter and the Philosopher\'s Stone',
#             'author': 'J. K. Rowling',
#             'read': False
#         },
#         {
#             'title': 'Green Eggs and Ham',
#             'author': 'Dr. Seuss',
#             'read': True
#         }
#     ]
#     return jsonify({
#         'status': 'success',
#         'books': BOOKS
#     })


if __name__ == '__main__':
    app.run()
