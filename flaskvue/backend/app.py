from flask import Flask, jsonify
from flask_cors import CORS
from flask_script import Manager
from application import jsonrpc

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

@jsonrpc.method(name="Home.index")
def index():
    return "hello world!"

if __name__ == '__main__':
    # manager.run()
    app.run()
