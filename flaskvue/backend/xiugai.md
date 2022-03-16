1. unread_match_id.py中, '/users/<int:id>/match_id_file/' 返回值修改

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

12. 没有id的url加上<int:id>