from flask import session, request, url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import os
from . import main
from redis import Redis
# from werkzeug import secure_filename

'''
socketio.on 接收从客户端发送来的WebSocket消息, 第一个参数是event名称。
connect, disconnect, message和json是SocketIO产生的特殊events。
message传递字符串，JSON传递JSON
'''

# @main.route('/store', methods=['POST'])
# def store():
#     if request.method == 'POST':
#         f = request.files['file']
#         print("aaaa")

@socketio.on('init', namespace='/index')
def init(message):
    
    name_to_random_index = session.get('name_to_random_index')
    print("name_to_random_index", name_to_random_index)

    conn = Redis(host='127.0.0.1')
    conn.set(name=name_to_random_index[0],value=name_to_random_index[1])
    print(conn.keys())

    cur_index = name_to_random_index[1]
    join_room(cur_index)
    
    print("init")
    emit('status', {'msg': "Login Successfully"}, room=cur_index)
    # emit('status', {'msg': session.get('name') + ':' }, room=cur_index)

@socketio.on('send_message', namespace='/index')
def send_message(message):

    conn = Redis(host='127.0.0.1')
    room_send_to = int(conn.get(name=message['msg']).decode())

    print("room_send_to",room_send_to)
    print("test1",conn.get(name='test1').decode(), type(conn.get(name='test1').decode()))
    print("test2",conn.get(name='test2').decode())
    room = session.get('random_index')
    print("room",room,type(room))

    emit('message', {'msg': 'Do you want to connect:' + session.get('name'),'room':"a"}, room=room_send_to)

@socketio.on('accept', namespace='/index')
def accept(message):
    print("bbbbb")
    session['room'] = "a"

    name = session.get('name', '')
    room = session.get('room', '')

    print("ccccc")
    # return render_template('chat.html', name=name, room=room)
    emit('redirect', {'url': url_for('main.chat')})
    # conn = Redis(host='127.0.0.1')
    # room_send_to = int(conn.get(name=message['msg']).decode())

    # print("room_send_to",room_send_to)
    # print("test1",conn.get(name='test1').decode(), type(conn.get(name='test1').decode()))
    # print("test2",conn.get(name='test2').decode())
    # room = session.get('random_index')
    # print("room",room,type(room))

    # emit('message', {'msg': 'Do you want to connect:' + session.get('name'),'room':"a"}, room=room_send_to)


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message,methods=['GET', 'POST']):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    print("text",session.get('name', ''))
    print("sid",request.sid)
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)

@socketio.on('file', namespace='/chat')
def file(message, methods=['GET', 'POST']):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    print("oooo3")
    print(message['msg'])
        # f.save(secure_filename(f.filename))
        # from flask import current_app
        # f.save(os.path.join(current_app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
    print("oooo2")
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)
    # emit('json', {'msg': session.get('name') + ':' + "shoudaole"}, room=room)

@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

