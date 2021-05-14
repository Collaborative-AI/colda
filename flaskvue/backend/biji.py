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
1. 进程线程？
2. 需要wss吗
3. 需要ssh吗
'''

'''
1. 传文件
2. 一个用户加入多个聊天
3. 同意才聊天
4. 数据库
'''