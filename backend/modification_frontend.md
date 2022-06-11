1. unread_match_identifier.py中, '/users/<string:id>/identifier_content/' 返回值修改

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
          'assistor_username_list': assistor_username_list (list), 
          'identifier_content': identifier_content (list),      
          'task_id': task_id (string), 
          'task_mode': 'regression' (string), 
          'model_name': 'LinearRegression' (string), 
          'metric_name': 'RMSE' (string),
          'task_name': 'unittest' (string), 
          'task_description': 'unittest_desciption' (string)
      }
    - /match_identifier_content/<string:id>
      {
          'task_id': task_id, (string) 
          'identifier_content': identifier_content (list)
      }
    - /get_identifier_content/<string:id>
      {
          'task_id': task_id (string)
      }
    - /send_situation/<string:id>
     {
          'task_id': task_id (string),
          'assistor_random_id_to_residual_dict': assistor_random_id_to_residual_dict (dict)
      }
    - /get_situation_content/<string:id>
     {
          'task_id': task_id (string), 
          'rounds': cur_rounds_num (int)
      }
    - /send_output/<string:id>
     {
          'task_id': task_id (string), 
          'output_content': output_content (list)
      }
    - /get_output_content/<string:id>
     {
          'task_id': task_id (string), 
          'rounds': cur_rounds_num (int)
      }
   - test
    - /find_test_assistor/<string:id>
      {
          'identifier_content': identifier_content (list),      
          'task_id': task_id (string), 
          'test_id': test_id (string),
          'task_mode': 'regression' (string), 
          'model_name': 'LinearRegression' (string), 
          'metric_name': 'RMSE' (string),
          'test_name': 'unittest' (string), 
          'test_description': 'unittest_desciption' (string)
      }
    - /match_test_identifier_content/<string:id>
     {
          'task_id': task_id (string), 
          'test_id': test_id (string),
          'identifier_content': identifier_content (string)
      }
    - /get_test_identifier_content/<string:id>
     {
          'task_id': task_id(string) ,
          'test_id': test_id(string) ,
      }
    - /send_test_output/<string:id>
     {
          'task_id': task_id (string), 
          'test_id': test_Id (string),
          'output_content': output_content (list)
      }
    - /get_test_output_content/<string:id>
     {
          'task_id': task_id (string), 
          'test_id': test_id (string)
      }

3. 传出数据名称, 格式改变
   - train
    - /find_assistor/<string:id>
      {
          'task_id': task_id (string), 
          'assistor_num': len(assistor_id_list) (int),
     }
    - /match_identifier_content/<string:id>
      {
          "stored": "assistor match id stored" (string),
          "task_id": task_id (string)
      }
    - /get_identifier_content/<string:id>
      如果是sponsor:
      {
          'assistor_random_id_to_identifier_content_dict': assistor_random_id_to_identifier_content_dict (dict),
      }
      如果是assistor:
      {
          'sponsor_random_id_to_identifier_content_dict': sponsor_random_id_to_identifier_content_dict (dict),
      }
    - /send_situation/<string:id>
      {
        "message": "send situation successfully!" (string)
      }
    - /get_situation_content/<string:id>
      {
        'situation_content': situation_content (list),
        'sender_random_id': sender_random_id (string)
      }
    - /send_output/<string:id>
      {
        "send_output": "send output successfully" (string)
      }
    - /get_output_content/<string:id>
      {
        'assistor_random_id_to_output_content_dict': assistor_random_id_to_output_content_dict (dict)
      }
   - test
    - /find_test_assistor/<string:id>
      {
        'task_id': task_id (string), 
        'assistor_num': len(assistor_id_list) (int),
        'test_id': test_id (string)
      }
    - /match_test_identifier_content/<string:id>
      {
        "stored": "assistor test match id stored" (string),
        "test_id": test_id (string)
      }
    - /get_test_identifier_content/<string:id>
      如果是sponsor:
      {
          'assistor_random_id_to_identifier_content_dict': assistor_random_id_to_identifier_content_dict (dict),
      }
      如果是assistor:
      {
          'sponsor_random_id_to_identifier_content_dict': sponsor_random_id_to_identifier_content_dict (dict),
      }
    - /send_test_output/<string:id>
      {
        "send_test_output": "send test output successfully" (string)
      }
    - /get_test_output_content/<string:id>
      {
        'assistor_random_id_to_output_content_dict': assistor_random_id_to_output_content_dict (dict)
      }

4. 逻辑改变



5. 补充: 
    1. /check_sponsor/<string:id> 返回值为response = {        c
        'role': role  
    }

    2. '/get_test_history_id/<string:id>' -> '/get_test_task_id_history/<string:id>'  c

    3. stop_train_task / stop_test_task in Notification Table   c

    4. '/stop_train_task/<string:id>' 返回值:       c
        response = {
            "message": "delete successfully", 
            "isSponsor": False, 
            "cur_rounds_num": cur_rounds_num
        }
    5. url加前缀
    6. 修改get_user_history返回的key, 'items' => 'participated_sort_task_dict'
    7. Train_Task: assistor_id_list => assistor_id_dict, test_task_list => test_id_of_train_id_dict
    8. Test_Task: assistor_id_list => assistor_id_dict
    9. get_test_task_id_history 返回为'test_id_of_train_id_dict'
