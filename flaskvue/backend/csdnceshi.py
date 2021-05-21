# from flask import Flask
# from flask_session import Session
# from flask_socketio import SocketIO
# from flask_cors import CORS
# from flask_socketio import SocketIO

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'chatroom'
# CORS(app, supports_credentials=True)
# socketio = SocketIO(app, cors_allowed_origins="*")


# @socketio.on('test', namespace='/api')   # 监听前端发回的包头 test ,应用命名空间为 api 
# def test():  # 此处可添加变量，接收从前端发回来的信息
#     print('触发test函数')
#     socketio.emit('api', {'data': 'test_OK'}, namespace='/api') # 此处 api 对应前端 sockets 的 api 

# '''
# 此处写入监听事件
# '''
# if __name__ == '__main__':
#     socketio.run(app, host='127.0.0.1', port='5000', debug=True) # 注意不再使用app.run



from threading import Lock
from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room, \
    leave_room, close_room, rooms, disconnect
from flask_cors import CORS

socketio = SocketIO()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chatroom'
CORS(app, supports_credentials=True)
# socketio = SocketIO(app, cors_allowed_origins="*")
socketio.init_app(app=app, cors_allowed_origins="*")



def background_chat(msg, sid):
    
    socketio.emit('chat_message', {'msg': msg},
                  namespace='/chatroom',
                  room=sid)
    socketio.sleep(3)

# @app.route('/index', methods=['GET'])
# def index():
#     return 'welcome to the chatroom!'

@socketio.on('join', namespace='/chatroom')
def join_chat(message):
    """创建聊天室
    """
    join_room(request.sid)
    print("join_chat")
    thread = socketio.start_background_task(background_chat, message, request.sid)
    emit('response', {'msg': '创建聊天室成功'})

@socketio.on('leave', namespace='/chatroom')
def leave_chat(message):
    """离开聊天室，仅删除当前用户
    """

@socketio.on('close', namespace='/chatroom')
def close_chat(message):
    """关闭聊天室，将所有用户移出
    """

@socketio.on('user_input', namespace='/chatroom')
def user_input(message):
    """获取用户输入
    """
    sid = request.sid
	# TODO

@socketio.on('connect', namespace='/chatroom')
def connect():
    """创建socket链接
    用户进入浏览器页面，自动加入
    """
    print('connect---------------', request.sid)

@socketio.on('disconnect', namespace='/chatroom')
def disconnect():
    """关闭socket链接
    用户关闭浏览器页面，自动退出
    """
    print('Client disconnected', request.sid)

if __name__ == '__main__':
    # app, socketio = create()
    socketio.run(app, debug=True, host="127.0.0.1", port=5000)
