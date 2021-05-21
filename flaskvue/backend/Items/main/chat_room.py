from threading import Lock
from flask import Flask, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect

from flask_cors import CORS, cross_origin
from . import main
from Items import socketio

def background_chat(msg, sid):
    
    socketio.emit('chat_message', {'msg': msg},
                  namespace='/chatroom',
                  room=sid)
    socketio.sleep(3)

@main.route('/index', methods=['GET'])
# @cross_origin()
def index():
    return 'welcome to the chatroom!'

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
    print('connect------------', request.sid)

@socketio.on('disconnect', namespace='/chatroom')
def disconnect():
    """关闭socket链接
    用户关闭浏览器页面，自动退出
    """
    print('Client disconnected', request.sid)