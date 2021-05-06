from flask import Flask, jsonify
from flask_cors import CORS
from flask_script import Manager

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Using Command Line
manager = Manager(app=app)

# sanity check route
@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify('Hello!')


if __name__ == '__main__':
    # manager.run()
    app.run()
