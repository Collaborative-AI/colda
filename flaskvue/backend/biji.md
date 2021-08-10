from redis import Redis

conn = Redis(host='127.0.0.1')
conn.delete(*conn.keys())
# value = conn['Apollo_flask_backendeyJjc3JmX3Rva2VuIjoiNjZlMGM1YjE1M2QzYTJhZDFhZThmNDExYmYxZjU2MmEzNjYyMTdjNCIsIm5hbWUiOiJ0ZXN0MiIsInJvb20iOiJiIn0.YJ3uLw.I-D9vBaBb71Hc1vBov-jx8McAzc']
# print(value)

v = conn.keys()
print(v)



# @app.template_global() all templates {{ sb(1,2) }}
# @app.template_filter() all templates {{ 1|db(2,3) }}

# 特殊装饰器
# @app.before_request 前
# @app.after_request 后
    # def a(response):
    #     print("a")
    #     return response

# @app.before_request
# def check_login():
#     if request.path == '/login':
#         return None
#     user = session.get('user_info')
#     if not user:
#         return redirect('/login')

# response = make_response(...)
#   return response

# 用一次, session实现
# flash, get_flashed_messages
# category, get_flashed_messages(category_filter=['x'])

# 蓝图 目录结构的划分， url加前缀, before_request 分组件

# pipreqs ./
# pip3 install -r requirements.txt

# 2 Localstack -> _request_ctx_stack (request,session) / _app_ctx_stack (app,g)
# g 一个请求的全局变量
# 可以处理多线程

# 第一种
# app.session_interface = RedisSessionInterface(
#     redis=Redis(host='127.0.0.1',port=5000),
#     key_prefix='Apollo_flask_backend'
# )
# 第二种设置 (可放到setting)
    # app.config['SESSION_TYPE'] = 'redis'
    # app.config['SESSION_REDIS'] = Redis(host='127.0.0.1',port=5000)
    # app.config['SESSION_KEY_PREFIX'] = 'Apollo_flask_backend'
    # app.config['']
    # Session(app)
# from flask_session import RedisSessionInterface
'''
app.session_interface = SecureCookieSessionInterface() 读存cookie, 实现2个功能
app.session_interface = RedisSessionInterface()
'''

# session要对字典的key修改才能识别， 识别__setitem__才触发indicator, 而后写入cookie(包在pop下)
# session['key'] = a
# session['modified'] = True 或者 SESSION_REFRESH_EACH_REQUEST = True
'''
组件:
1. flask-session:
    Redis/SQLalchemy...

2. 数据库连接池: DBUtils(pymysql) => 2种连接方式(SQL/ORM)
    减少损耗，提升性能


3. wtforms
    对python web框架做表单验证

4. SQLAlchemy
    关系对象映射
    类 => 表
    对象 => 记录（一行数据）

    当有了对应关系之后，不再需要编写SQL语句， 取而代之的是操作: 类，对象。
        ORM: models.User.objects.filter(id_gt=1,type__name='x')


5. flask-script

6. flask-migrate
    数据库迁移
'''
# __mro__ 继承顺序
# __dict__ 类中所有元素或者对象中所有元素

# metaclass 指定类由什么type创建


# 装饰器
# def wrapper(func):
#     # @functools.wraps(func)
#     def inner(*args,**kwargs):
#         print(args)
#         print("a")
#         print(func(*args, **kwargs))
#         return 111111

#     # print(args)
#     print(func)
#     return inner

# @wrapper
# def add(a1):
#     return a1+1000

# print(add.__name__)

'''
1. 进程 线程？
2. 需要wss吗
3. 需要ssh吗
'''

'''
1. data:y
2. model
'''

'''
server
Match: A,B,Intersect

后面: Intersect
'''
'''
Serverdatabase
    Conversation ID
        match: A, B, Intersect
        UserA_initial:
        UserB_initial:
        Intersect_initial:
        "第几次+(A,B)": url_for(y), intersect
        
db_metadata:
    Conversation ID
        match: A, B, Intersect
        UserA_initial:
        UserB_initial:
        Intersect_initial:
        autoinc: url_for(y)
'''

'''
1. 传文件 (1)
2. 一个用户加入多个聊天
3. 同意才聊天 (1)
4. 数据库 (1)

1. 确定数据库, 选择与结构
2. 比对文件
3. 加入多个聊天
'''


'''
# from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
# from Items import socketio

# CORS(app, resources=r'/*')
    # socketio = SocketIO(app, cors_allowed_origins="*") # websocket 跨域
    # socketio.init_app(app=app,cors_allowed_origins="*")
Websocket 代码:

chatroom----------------------------------

from threading import Lock
from flask import Flask, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from redis import Redis
from flask_cors import CORS, cross_origin
from . import main
from Items import socketio

def background_chat(msg, sid):
    
    socketio.emit('chat_message', {'msg': msg},
                  namespace='/chatroom',
                  room=sid)
    socketio.sleep(3)

@main.route('/index', methods=['GET'])
@cross_origin()
def index():
  # chosen_room = request.get_json()
  return "Welcome to Chatroom!"
    #  emit('response', {'msg': 'welcome to chatroom'})

@socketio.on('upload_file', namespace='/chatroom')
def upload_file(file):
    """upload file
    """
    print("jinlaile")
    # print("zheshi!!", file)
    emit('response', {'msg': '接收成功'})

@socketio.on('connect', namespace='/chatroom')
def connect():
    """创建socket链接
    用户进入浏览器页面，自动加入
    """
    emit('response', {'msg': "websocket connect successfully"})

@socketio.on('init', namespace='/chatroom')
def init(name):

    # print("init------------", session)
    # if session.get('name') is None:
    #   session['name'] = "test1"
    session['name'] = name
    session['sessionID'] = request.sid
    session['name_to_sessionID'] = (name, request.sid)

    print('init------------', request.sid)
    print(session['sessionID'])
    print(session['name_to_sessionID'])

    conn = Redis(host='127.0.0.1')
    conn.set(name=name,value=request.sid)
    join_room(request.sid)

    emit('response', {'msg': "websocket connect successfully"})

@socketio.on('join_chat', namespace='/chatroom')
def join_chat(chosen_room):
    """创建聊天室
    """
    conn = Redis(host='127.0.0.1')
    conn.set(name=session.get('name'),value=chosen_room)

    session['room'] = chosen_room
    join_room(chosen_room)
    # join_room("2")

    print("join_chat")
    print("message", chosen_room)
    # thread = socketio.start_background_task(background_chat, message, chosen_room)

    emit('response', {'msg': '创建聊天室成功'})

@socketio.on('invite', namespace='/chatroom')
def invite(cooperator):
    """invite people
    """
    print("invite---------------------", cooperator)

    conn = Redis(host='127.0.0.1')
    
    cooperator_split = cooperator.split(",")
    for i in range(len(cooperator_split)-1):
      room_send_to = conn.get(name=cooperator_split[i]).decode()
      print("invite---------------", room_send_to)
      emit('invite_message', {'msg': 'Do you want to connect:' + session.get('name')}, room=room_send_to)

    # print("room_send_to",room_send_to)
    # # print("test1",conn.get(name='test1').decode(), type(conn.get(name='test1').decode()))
    # # print("test2",conn.get(name='test2').decode())
    # # room = session.get('random_index')
    # # print("room",room,type(room))

    # emit('message', {'msg': 'Do you want to connect:' + session.get('name'),'room':"a"}, room=room_send_to)

    emit('response', {'msg': "invite successfully"})

@socketio.on('text', namespace='/chatroom')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    print("text------------------")
    room = session.get('room')
    print("room", room, "message", message)

    emit('chat_message', {'msg': session.get('name') + ':' + message}, room=room)

@socketio.on('leave', namespace='/chatroom')
def leave_chat(message):
    """离开聊天室，仅删除当前用户
    """
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

@socketio.on('close', namespace='/chatroom')
def close_chat(message):
    """关闭聊天室，将所有用户移出
    """


@socketio.on('disconnect', namespace='/chatroom')
def disconnect():
    """关闭socket链接
    用户关闭浏览器页面，自动退出
    """
    print('Client disconnected------------------------', request.sid)



events--------------------------------------
from flask import session, request, url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from redis import Redis
# from werkzeug import secure_filename


socketio.on 接收从客户端发送来的WebSocket消息, 第一个参数是event名称。
connect, disconnect, message和json是SocketIO产生的特殊events。
message传递字符串，JSON传递JSON


# @main.route('/store', methods=['POST'])
# def store():
#     if request.method == 'POST':
#         f = request.files['file']
#         print("aaaa")

@socketio.on('init', namespace='/index')
def init(message):
    
    # session['name_to_random_index'] = (form.name.data, random_index)
    name_to_random_index = session.get('name_to_random_index')
    print("name_to_random_index", name_to_random_index)

    conn = Redis(host='127.0.0.1')
    conn.set(name=name_to_random_index[0],value=name_to_random_index[1])
    # print(conn.keys())

    cur_index = name_to_random_index[1]
    join_room(cur_index)
    
    print("init-------------------")
    print("text",session.get('name', ''))
    print("sid",request.sid)

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

    session['room'] = "a"

    name = session.get('name', '')
    room = session.get('room', '')

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
    print("chat------------------")
    print("text",session.get('name', ''))
    print("sid",request.sid)
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)

@socketio.on('file', namespace='/chat')
def file(message, methods=['GET', 'POST']):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
        # f.save(secure_filename(f.filename))
        # from flask import current_app
        # f.save(os.path.join(current_app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))  
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



form-----------------------------------------
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[Required()])
    submit = SubmitField('Enter Your Name')

class RoomForm(FlaskForm):
    """Accepts a nickname and a room."""
    room = StringField('Room', validators=[Required()])
    # user = StringField('Connect User', validators=[Required()])
    submit = SubmitField('Enter Chatroom')

# class ConnectUserForm(FlaskForm):
#     """Accepts a nickname and a room."""
#     room = StringField('Connect User', validators=[Required()])
#     submit = SubmitField('Enter User Name')

routes--------------------------------------------
from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import NameForm, RoomForm
import random


@main.route('/ceshi',methods=['GET'])
def ceshi():
  return "chenggong"

@main.route('/diyi', methods=['GET', 'POST'])
def diyi():
    """Login form to enter a room."""
    form = NameForm()
    if form.validate_on_submit():
        
        session['name'] = form.name.data

        random_index = random.randint(0,10000)
        session['random_index'] = random_index

        session['name_to_random_index'] = (form.name.data, random_index)
        # session['room'] = form.room.data
        return redirect(url_for('main.index'))
        # render_template('main_page.html')
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        # form.room.data = session.get('room', '')
    return render_template('login.html', form=form)
    # return render_template('main_page.html')

# @main.route('/main_page', methods=['GET', 'POST'])
# def main_page():
#     # return None
#     render_template('main_page.html')
    

@main.route('/index1', methods=['GET', 'POST'])
def index1():
    """Login form to enter a room."""
    form = RoomForm()
    # form = ConnectUserForm()
    if form.validate_on_submit():
        # session['user'] = form.user.data
        session['room'] = form.room.data
        return redirect(url_for('main.chat'))
    elif request.method == 'GET':
        # form.user.data = session.get('user', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', name=session.get('name', ''), form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    
    name = session.get('name', '')
    room = session.get('room', '')
    print("name",name,"room",room)
    if name == '' or room == '':
        return redirect(url_for('main.index'))
    return render_template('chat.html', name=name, room=room)

# socketio = SocketIO()

# Flask-SQLAlchemy plugin
db = SQLAlchemy()

# Flask-Migrate plugin
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('setting.DevelopmentConfig')

    # Initialize Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Substitue session to redis
    Session(app)
    
    # Enable CORS
    CORS(app)
    # CORS(app, supports_credentials=True) 

    # Init Flask-SQLAlchemy
    db.init_app(app)

    # Init Flask-Migrate
    migrate.init_app(app, db)

    return app

'''