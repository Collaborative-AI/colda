from flask import request

from Items import pyMongo
# import BluePrint
from Items.helper_api import helper_api_bp
from Items.authentication import token_auth

# @helper_api_bp.route('/ceshi', methods=['GET'])
@helper_api_bp.route('/changshi', methods=['GET'])
def changshi():
  print("NIHAO!!!!!")

#   zzz = id
#   print("aaaa", zzz)
#   args = request.args.get("id")
#   print("oo", args)
#   file_obj = request.get_json()
#   print(file_obj)

#   print("zhuanhuan", json.loads(file_obj['file']))

#   file_array = json.loads(file_obj['file'])
#   for i in file_array:
#     print(i)
#   print("data",request.values.get("Json"))
#   print("data",request.values.get("JSON"))
#   print("data2", request.get_data())
  return "good,NIHAO"

# @helper_api_bp.route('/ceshi', methods=['GET'])
@helper_api_bp.route('/changshi2', methods=['GET'])
def changshi2():
  print("wori")

  return "best,NIHAO"

@helper_api_bp.route('/ceshi/<string:ID>/<int:value>', methods=['GET'])
@token_auth.login_required
def ceshi(ID,value):
  print("jinlaile!!!!!")

  # zzz = id
  # print("aaaa", zzz)
  # args = request.args.get("ID")
  # print("ARGS",args)
  print("ID", ID)
  print("value", value)
  # print("oo", args)
  # file_obj = request.get_json()
  # print("FILE", file_obj)

  # print("zhuanhuan", json.loads(file_obj['file']))

  # file_array = json.loads(file_obj['file'])
  # for i in file_array:
  #   print(i)
  print("data",request.values.get("Json"))
  print("data",request.values.get("JSON"))
  print("data2", request.get_data())
  return "good"

@helper_api_bp.route('/create_unittest_user/', methods=['POST'])
def create_unittest_user():
    data = request.get_json()
    username = data['username']

    if User.query.filter_by(username = username).first():
        return 'repetition'

    user = User()
    user.from_dict(data, new_user=True)
    user.confirmed = 'true'
    db.session.add(user)
    db.session.commit()

    return 'gg'

# @helper_api_bp.route('/ceshi', methods=['GET'])
@helper_api_bp.route('/delete_unittest_db/', methods=['GET'])
def delete_unittest_db():
  
  # Message, Matched, Notification
  queries = Matched.query.all()
  for row in queries:
      db.session.delete(row)
      db.session.commit()

  Messages = Message.query.all()
  for row in Messages:
      db.session.delete(row)
      db.session.commit()

  Notifications = Notification.query.all()
  for row in Notifications:
      db.session.delete(row)
      db.session.commit()

  Pendings = Pending.query.all()
  for row in Pendings:
      db.session.delete(row)
      db.session.commit()

  Users = User.query.all()
  for row in Users:
      db.session.delete(row)
      db.session.commit()

  return "gg"

# @helper_api_bp.route('/ceshi', methods=['GET'])
@helper_api_bp.route('/delete_all_rows/', methods=['GET'])
@token_auth.login_required
def delete_all_rows():
  
  # Message, Matched, Notification
  queries = Matched.query.all()
  for row in queries:
      db.session.delete(row)
      db.session.commit()

  Messages = Message.query.all()
  for row in Messages:
      db.session.delete(row)
      db.session.commit()

  Notifications = Notification.query.all()
  for row in Notifications:
      db.session.delete(row)
      db.session.commit()

  Pendings = Pending.query.all()
  for row in Pendings:
      db.session.delete(row)
      db.session.commit()

  return "done"

@helper_api_bp.route('/delete_test_rows/', methods=['GET'])
@token_auth.login_required
def delete_test_rows():
  
  # Message, Matched, Notification
  queries = Matched.query.filter(Matched.test_indicator == "test").all()
  for row in queries:
      db.session.delete(row)
      db.session.commit()

  Messages = Message.query.filter(Message.test_indicator == "test").all()
  for row in Messages:
      db.session.delete(row)
      db.session.commit()

  Notifications = Notification.query.all()
  for row in Notifications:
      db.session.delete(row)
      db.session.commit()

  Stops = Stop.query.all()
  for row in Stops:
      db.session.delete(row)
      db.session.commit()

  Pendings = Pending.query.all()
  for row in Pendings:
      db.session.delete(row)
      db.session.commit()

  return "done"


@helper_api_bp.route('/ceshi_mongo/', methods=['POST', 'GET'])
def ceshi_mongo():

    # a = str(uuid.uuid4())
    # print('ggg', a, len(a))

    # res = pyMongo.db.user.find_one_or_404({"name": "Ada Lovelace"})
    # print('res', res)
    # collections = pyMongo.db.list_collection_names()
    # print('collections_1', collections)
    # res = pyMongo.db.shuaiqi.insert_one({'x': 1})
    # print('res1', res)
    # collections = pyMongo.db.list_collection_names()
    # print('collections_2', collections)

    # user = pyMongo.db.User.find_one({'username': 'qq'})
    # print('user', user)

    # # pyMongo.db.User.insert_one({'username': 'qq'})
    # user = pyMongo.db.User.find_one({'username': 'qq'})
    # user_id = user['_id']
    # print('user2', user)
    # print(user['_id'], type(user['_id']))
    # print('hhh', str(user['_id']), type(str(user['_id'])))

    # user = pyMongo.db.User.find_one({'_id': str(user_id)})
    # print('user3', user)
    # user = pyMongo.db.User.find_one({'_id': user_id})
    # print('user4', user)

    # record = {
    #     'username': 'qia', 
    #     "information": [],
    # }
    # pyMongo.db.User.insert_one(record)

    # res = pyMongo.db.User.find_one({'username': 'qia'})
    # print('hhh', res)

    # pyMongo.db.User.update_one({'username': 'qia'}, {'$set':{'isTerminate': True}})
    # res = pyMongo.db.User.find_one({'username': 'qia'})
    # print('hhh6', res)

    # isTerminate = res['isTerminate']
    # print('type', type(isTerminate))

    # newObjectId = ObjectId()
    # print('hh', newObjectId, str(newObjectId))
    # record = {
    #     '_id': newObjectId,
    #     'username': 'qiab', 
    #     "information": [],
    # }
    # pyMongo.db.User.insert_one(record)
    # res = pyMongo.db.User.find_one({'username': 'qiab'})
    # print('res', res)
    # res = pyMongo.db.User.find_one_and_update({'username': 'qiab'}, {'$set':{'username': 'fghs'}})
    # print('res1', res)
    # res = pyMongo.db.User.find_one({'username': 'fghs'})
    # print('res2', res)

    # b = 'fff'
    # res = pyMongo.db.User.update_one({'username': 'fghs'}, {'$set': {'apple.' + b: 'good'}})
    # print('res3', res)
    # res = pyMongo.db.User.find_one({'username': 'fghs'})
    # print('res4', res)

    # a = SnowflakeGenerator(1)
    # print('fff', a)

    # a1 = uuid.uuid1()
    # a2 = uuid.uuid1()
    # print(a1, a2)

    # res = pyMongo.db.User.update_one({'username': 'hhhh'}, {'$set': {'apple.' + b: 'good'}})
    # print('res5', res)
    # res = pyMongo.db.User.find_one({'username': 'hhhh'})
    # print('res6', res)

    # record = {
    #     'username': 'hhhh', 
    #     "information": [],
    # }
    # res = pyMongo.db.User.insert_one(record)
    # print('res7', res)
    # res = pyMongo.db.User.update_one({'username': 'hhhh'}, {'$set': {'apple.' + b: 'good'}})
    # print('res8', res)
    # res = pyMongo.db.User.find_one({'username': 'hhhh'})
    # print('res9', res)

    # def xiaohanshu():
    #     return (5,6,7)
    
    # (a,b,c) = xiaohanshu()
    # print(a,b,c)

    # record = {
    #     'user_id': 'ceshi1',
    #     'username': 'ceshi_shijian1', 
    #     'email': 'gg1',
    #     "information": [],
    # }
    # res = pyMongo.db.User.insert_one(record)
    # record = {
    #     'user_id': 'ceshi2',
    #     'username': 'ceshi_shijian2', 
    #     'email': 'gg2',
    #     "information": [],
    # }
    # res = pyMongo.db.User.insert_one(record)

    # ceshi_shijian1 = pyMongo.db.User.find_one({'username': 'ceshi_shijian1'})
    # print('ceshi_shijian1', ceshi_shijian1)
    # ceshi_shijian2 = pyMongo.db.User.find_one({'username': 'ceshi_shijian2'})
    # print('ceshi_shijian2', ceshi_shijian2)
    # ceshi_shijian1_time = ceshi_shijian1['_id'].generation_time
    # ceshi_shijian2_time = ceshi_shijian2['_id'].generation_time
    # print('time', ceshi_shijian1_time, ceshi_shijian2_time)
    # a = ceshi_shijian2_time > ceshi_shijian1_time
    # b = ceshi_shijian2_time == ceshi_shijian1_time  
    # print(a, b)

    print('sss', dir(pyMongo))
    import sys


    

    # a = []
    # for i in range(2):
    #     a.append([])
    #     for j in range(1250000):
    #         a[-1].append(j)
    
    # print('sadfasd', sys.getsizeof(a))
    
    import bson
    # data = bson.BSON.encode({'a': a})
    # print('asdad', sys.getsizeof(data))
    # # 16000000
    # train_match_identifier_document = {
    #     'suhai': a
    # }
    # pyMongo.db.Train_Match_Identifier.insert_one(train_match_identifier_document)

    
    import io
    import json
    from gridfs import GridFS
    from io import BytesIO
    # a = io.StringIO('12321')
    # print('asdfasdf', a, dir(a))
    
    
    # print('&&&', data)
    # fileobj = BytesIO(b"these are the bytes")
    # # res = pyMongo.save_file(filename="lihai", fileobj=fileobj, base='fs')
    # res = pyMongo.save_file("lihai", fileobj, foo="bar")
    # print('res', res)

    # # print('###', dir(pyMongo.db))
    # # gridfs = GridFS(pyMongo.db)
    # # print('$$', dir(gridfs))

    # # res = gridfs.exists({"filename": "lihai"})
    # # print('res1', res)

    # # res = pyMongo.send_file(filename='lihai', base='fs')
    # res = pyMongo.send_file("lihai")
    # print('res2', res)

    # myfile = BytesIO(b"a" * 500 * 1024)
    # pyMongo.save_file("myfile.txt", myfile, base='User')
    # resp = pyMongo.send_file("myfile.txt", base="User")
    # for key, val in resp.items():
    #     print('sss', key, val)

    # fileobj = BytesIO(b"these are the bytes")
    a = [1,2,3]
    data = bson.BSON.encode({'a': a})
    # decoded_doc = bson.BSON(data).decode()
    # print('decoded_doc', decoded_doc)
    print('asdfad', type(data))
    # print('asdfas', isinstance(data, bson.BSON))
    fileobj = BytesIO(data)
    id = pyMongo.save_file("my-file1.txt", fileobj)
    print('dfdfs', id, type(id))
    gridfs = GridFS(pyMongo.db)
    gridfile = gridfs.find_one({"filename": "my-file1.txt"})
    print('gsdfad', dir(gridfile))
    # for key, val in gridfile.__dict__.items():
    #     print('sss', key, val)

    # res = gridfile.read()
    # print('res', res, type(res))
    # print('res2', bson.BSON(res).decode())

    # b = pyMongo.db.User
    # print('bbbb', b, dir(b))
    # assert gridfile.content_type == "text/plain"

    # a = fs.put(b"hello world")
    # fs.get(a).read()
    # data = json.dumps(a)
    # print('data', dir(data))
    # res = pyMongo.save_file(filename='lihai', fileobj=b"aaaa")
    # print('res', res)
    # res = pyMongo.send_file(filename='lihai')
    # print('res2', res)

    
    return 'gg'
