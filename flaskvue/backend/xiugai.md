1. unread_match_id.py中, '/users/<string:id>/identifier_content/' 返回值修改

2. unread_output.py中, get_user_test_output() 访问路径修改
   - send_situation中, 传输数据从residual_list修改为:     assistor_random_id_to_residual_dict:{
     assistor_random_id_1: residual_1,
     assistor_random_id_n: residual_n,
   }, 去掉assistor_random_id_list

3. 如何更新token? token增加续签功能，过期前n分钟更新, 加入到短轮训返回中

4. 修改notification逻辑

5. 统一返回格式, 都为dict

6. 修改数据库逻辑

7. 修改task_id使用uuid4, user_id使用id
    - uuid4 
      - 当索引占空间
      - uuid4会重复, 改成uuid1 / uuid 2
        - uuid1
          基于时间的UUID通过计算当前时间戳、随机数和机器MAC地址得到
        - uuid2
          基于时间的UUID算法相同，但会把时间戳的前4位置换为POSIX的UID或GID。这个版本的UUID在实际中较少用到
      - 无法有序递增, 递增能够让数据在插入时更方便建立主键索引，提高索引树的性能
      - 使用雪花算法 (snowflake)
      - uuid长度为32+4bytes, snowflake长度19 bytes, 64bit转成int
        - 最高位是符号位，因为生成的 ID 总是正数，始终为0，不可用。
        - 41位的时间序列，精确到毫秒级，41位的长度可以使用69年。时间位还有一个很重要的作用是可以根据时间进行排序。
        - 10位的机器标识，10位的长度最多支持部署1024个节点。
        - 12位的计数序列号，序列号即一系列的自增ID，可以支持同一节点同一毫秒生成多个ID序号，12位的计数序列号支持每个节点每毫秒产生4096个ID序号。
    - https://www.cnblogs.com/oklizz/p/11865750.html
    - https://xie.infoq.cn/article/05ca77a58fd21e7e1d8432434
    - 使用MondoDB的id当user id老是需要转换 => 开一个user_id

8. 修改轮训返回值 （带新token), 同时Key都加下划线

9. 修改传入的数据形式，都为dict

10. find_assistor传入名称: id_file => identifier_content

11. match_assistor_id中的传入名称: file => identifier_content

12. 没有id的url加上<string:id>

前端接轨:
1. url改变:
   注:
    1. 将id改为identifier以便理解
    2. 每个url后加上id

   - train
    - /find_assistor/<string:id>
    - /match_identifier_content/<string:id>
    - /get_identifier_content/<string:id>
    - /send_situation/<string:id>
    - /get_situation_content/<string:id>
    - /send_output/<string:id>
    - /get_output_content/<string:id>
   - test
    - /find_test_assistor/<string:id>
    - /match_test_identifier_content/<string:id>
    - /get_test_identifier_content/<string:id>
    - /send_test_output/<string:id>
    - /get_test_output_content/<string:id>

2. 传入数据名称, 格式改变
   - train
    - /find_assistor/<string:id>
      {
          'assistor_username_list': assistor_username_list, 
          'identifier_content': identifier_content,      
          'task_id': task_id, 
          'task_mode': 'regression', 
          'model_name': 'LinearRegression', 
          'metric_name': 'RMSE',
          'task_name': 'unittest', 
          'task_description': 'unittest_desciption'
      }
    - /match_identifier_content/<string:id>
      {
          'task_id': task_id, 
          'identifier_content': identifier_content
      }
    - /get_identifier_content/<string:id>
      {
          'task_id': task_id
      }
    - /send_situation/<string:id>
     {
          'task_id': task_id,
          'assistor_random_id_to_residual_dict': assistor_random_id_to_residual_dict
      }
    - /get_situation_content/<string:id>
     {
          'task_id': task_id, 
          'rounds': cur_rounds_num
      }
    - /send_output/<string:id>
     {
          'task_id': task_id, 
          'output_content': output_content
      }
    - /get_output_content/<string:id>
     {
          'task_id': task_id, 
          'rounds': cur_rounds_num
      }
   - test
    - /find_test_assistor/<string:id>
      {
          'identifier_content': identifier_content,      
          'task_id': task_id, 
          'test_id': test_id,
          'task_mode': 'regression', 
          'model_name': 'LinearRegression', 
          'metric_name': 'RMSE',
          'test_name': 'unittest', 
          'test_description': 'unittest_desciption'
      }
    - /match_test_identifier_content/<string:id>
     {
          'task_id': task_id, 
          'test_id': test_id,
          'identifier_content': identifier_content
      }
    - /get_test_identifier_content/<string:id>
     {
          'task_id': task_id,
          'test_id': test_id,
      }
    - /send_test_output/<string:id>
     {
          'task_id': task_id, 
          'test_id': test_Id,
          'output_content': output_content
      }
    - /get_test_output_content/<string:id>
     {
          'task_id': task_id, 
          'test_id': test_id
      }

3. 传出数据名称, 格式改变
   - train
    - /find_assistor/<string:id>
      {
          'task_id': task_id, 
          'assistor_num': len(assistor_id_list),
     }
    - /match_identifier_content/<string:id>
      {
          "stored": "assistor match id stored",
          "task_id": task_id
      }
    - /get_identifier_content/<string:id>
      如果是sponsor:
      {
          'assistor_random_id_to_identifier_content_dict': assistor_random_id_to_identifier_content_dict,
      }
      如果是assistor:
      {
          'sponsor_random_id_to_identifier_content_dict': sponsor_random_id_to_identifier_content_dict,
      }
    - /send_situation/<string:id>
      {
        "message": "send situation successfully!"
      }
    - /get_situation_content/<string:id>
      {
        'situation_content': situation_content,
        'sender_random_id': sender_random_id
      }
    - /send_output/<string:id>
      {
        "send_output": "send output successfully"
      }
    - /get_output_content/<string:id>
      {
        'assistor_random_id_to_output_content_dict': assistor_random_id_to_output_content_dict
      }
   - test
    - /find_test_assistor/<string:id>
      {
        'task_id': task_id, 
        'assistor_num': len(assistor_id_list),
        'test_id': test_id
      }
    - /match_test_identifier_content/<string:id>
      {
        "stored": "assistor test match id stored",
        "test_id": test_id
      }
    - /get_test_identifier_content/<string:id>
      如果是sponsor:
      {
          'assistor_random_id_to_identifier_content_dict': assistor_random_id_to_identifier_content_dict,
      }
      如果是assistor:
      {
          'sponsor_random_id_to_identifier_content_dict': sponsor_random_id_to_identifier_content_dict,
      }
    - /send_test_output/<string:id>
      {
        "send_test_output": "send test output successfully"
      }
    - /get_test_output_content/<string:id>
      {
        'assistor_random_id_to_output_content_dict': assistor_random_id_to_output_content_dict
      }

4. 逻辑改变