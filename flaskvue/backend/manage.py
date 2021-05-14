# from flask_script import Manager
# from flask_socketio import SocketIO
# from flask import Flask, jsonify

# app = Flask(__name__)
# from flask import Flask, jsonify
# from flask_cors import CORS
# from flask_script import Manager
# from application import jsonrpc
#
from Items import create_app, socketio
app = create_app()
# manager = Manager(app)

if __name__ == '__main__':
    socketio.run(app, debug = True)

    # manager.run()
    # app.run()
    # python manage.py runserver -d -r -h 0.0.0.0 -p 5000 (运行)
