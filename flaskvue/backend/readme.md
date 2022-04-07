pip1. First time launch:
    1. cd into backend
    2. pip install pipenv
    3. pipenv install
    4. pipenv shell
    5. flask run --with-threads

2. launch after first time
    1. pipenv install
    2. pipenv shell
    3. flask run --with-threads


4. Install Package: pipenv install + package name

5. Migrate the database: (create table in database e.g.sqlite3 mysql)
     0. migration .env add (render_as_batch=True,)
     (with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True,
            process_revision_directives=process_revision_directives,
            **current_app.extensions['migrate'].configure_args
        ))
     1. flask db migrate -m "comment"
     2. flask db upgrade (flask db downgrade => rollback)
            
6. Test: 
    
        1. modify the python code in Test files
        2. Running: flask test
    
7. 3 users:
      1. id=4 username=testa email=126@gmail.com password=123
      2. id=5 username=testb email=127@gmail.com password=123
      2. id=6 username=testc password=123

8. unittest must start with test(filename )

9. mysql command (mac):
    login: mysql -u root -p
    show databases: show databases;
    create new database: create database NAME charset=utf8;
    1.  mysql.server start (start server)
    2.  mysql.server stop  (end server)
    3.  mysql.server restart

<!-- Second way:
1. configure the make_shell_context() in manage.py (Start a python interpreter containing the context of the application)

2. Execution:
        Use HTTPie to test the API (need 2 terminals)
            1. run the flask in one terminal (1-3 steps) (must run the server)
            2. Do 1-2 steps in another terminal, then command. Example: 
            http POST http://localhost:5000/users username=test1 password=123 -->

1: testa apolloumn.email@gmail.com Aa1234567!
2: testb Aa1234567!

database_name = 'apollo_aws_mysql_unittest'
3: xie1 Xie1@123
4：xie2 Xie2@123
5: leq1 Leq1@123
5: leq2 Leq2@123


10. AWS RDB information:
    end point: apollodatabase.cb9jianlqhw8.us-east-2.rds.amazonaws.com
    port: 3306
    master username: apollo
    password: Aa1234567!


.env: 系统环境变量


11. 上服务器:
    注掉create_unittest_user

12. Docker教程:
    0. Basic concept:
        Image（镜像）: 构建和打包 / 菜
        Container（容器）: 执行和启动 / 饭盒
    1. 建立Dockerfile
    2. In Dockerfile, type:
        1. FROM

13. Elastic BeanStalk (All code deployed to Elastic Beanstalk needs to be "stateless" I.E. Never make changes directly to a running beanstalk instance using SSH or FTP):
    1. Preparation: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html
    2. navigate to backend file
    3. Freeze requirements:
        pipenv lock -r > requirements.txt 
    4. brew install awsebcli
    5. https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html (follow this or jump to step 6)
    6. Change ur entryfile to application.py and the flask instance to application
    7. Type in your command: export FLASK_APP=application.py
    8. Type in command: eb init -p python-3.8 synspot --region us-east-2
    9. (Optional) If you meet: You have not yet set up your credentials or your credentials are incorrect
        You must provide your credentials.
        (aws-access-id): from step 6 => https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-configuration.html => https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys
        Or you can use this directly:
        aws-access-id: AKIAW7PAIJ4ER2AWJUVR
        aws-secret-key: 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   
    10. create .ebignore file and add: virt
    11. Create a folder named: .ebextensions and create file: xx.config 
            Some instuctions:
                1. Configuration Options: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html
                2. How to update configuration: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-configuration-methods-after.html
                3. General options for all environments: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html
                4. Configure VPC config: https://docs.aws.amazon.com/zh_cn/elasticbeanstalk/latest/dg/using-features.managing.vpc.html
    12. Go to AWS console and create a VPC (10.0.0.0/16) (无类域间路由 (Classless Inter-Domain Routing (CIDR)) 块的形式为 VPC 指定 IPv4 地址范围) （CIDR缩小了路由器的路由表大小，减少了地址浪费）
        0. Video Link: https://www.youtube.com/watch?v=ifno8NKj51g&ab_channel=OneCloudHelper
        0. CIDR Explnation: https://wendangmao.com/doc/15c3481c814d2b160b4e767f5acfa1c7ab00827e-16.html
        1. Create 1 VPC (10.0.0.0/16)
        2. Create 2 public subnets (10.0.0.0/24 and 10.0.1.0/24, 主机位数一样=>网络位数一样=>网络地址需要不同)
        3. Create 1 Internet Gateway and attach it to VPC
        4. Create 1 public route table and associate 2 public subnets
        5. Add 0.0.0.0/0 to public route table
    13. Type in command: eb create synspot-env
    14. To run app: eb open
    15. Re-deploy app: eb deploy
        

14. Elastic BeanStalk + MongoDB Atlas
    1. 总体介绍: https://docs.aws.amazon.com/zh_cn/prescriptive-guidance/latest/migration-mongodb-atlas/migration-mongodb-atlas.pdf
    2. MongoDB Atlas与其他云数据库对比: https://www.mongodb.com/cloud/atlas/compare
    3. 介绍serverless, 对比serverless和cluster https://www.mongodb.com/community/forums/t/frequently-asked-questions-atlas-serverless-instances/131992
    4. serverless模式收费标准: https://www.mongodb.com/docs/atlas/billing/serverless-instance-costs/
    5. serverless与cluster对比: https://www.mongodb.com/docs/atlas/choose-database-deployment-type/#std-label-ref-deployment-types
    6. cluster收费表格: https://www.mongodb.com/mongodb-on-aws-pricing
    7. shared限制: https://www.mongodb.com/docs/atlas/reference/free-shared-limitations/#std-label-atlas-free-tier
    8. dedicated vs shared: https://www.mongodb.com/docs/atlas/cluster-tier/
    9. 如何升级shared为dedicated: https://www.mongodb.com/docs/realm/reference/upgrade-shared-cluster/
    10. 总结: 三种类型: serverless / dedicated / shared
        1. dedicated和shared为同一种类型(cluster)，都使用aws ec2部署. shared规格包括M0, M2, M5, dedicated包括更高级别的. (https://www.mongodb.com/mongodb-on-aws-pricing)
        2. dedicated为shared的升级版（使用更大的内存，存储更多的数据，更好的CPU等）,同时拥有一些额外功能, 如sharded cluster（分片，提升扩展性）, database auditing(数据库审计，记录信息，如CRUD), Encryption at Rest using Customer Key Management(加密存储在硬盘的数据)等。注: 可随时升级 （shared限制: https://www.mongodb.com/docs/atlas/reference/free-shared-limitations/#std-label-atlas-free-tier）
        3. serverless vs (dedicated / shared), serverless根据写入，读出，备份等操作的数据量收钱，价目表在(https://www.mongodb.com/docs/atlas/billing/serverless-instance-costs/), 读出为4KB当做一次read，$0.3/million, 写入为1KB当做一次, $1.25/million. 例子: 如果写入一个10MB的文件，即算为操作了10000次。同时serverless是新出的模式，有些功能尚未完善，如MongoDB Charts, Monitoring and alerting, Granular database auditing, Private networking, etc.

15. MongoDB模式 (https://blog.csdn.net/u014401141/article/details/78864419):
    1. 备份，故障恢复
        1. master slave (用于备份，故障恢复，读扩展)
            1. 在数据库集群中要明确的知道谁是主服务器,主服务器只有一台.
            2. 从服务器要知道自己的数据源也就是对应的主服务是谁.
            3. –master用来确定主服务器,–slave 和 –source 来控制从服务器
        2. replica set（推荐）
            1. 该集群没有特定的主数据库。
            2. 如果哪个主数据库宕机了，集群中就会推选出一个从属数据库作为主数据库顶上，这就具备了自动故障恢复功能
    2. sharding (当数据量达到T级别，磁盘内存无法应对CRUD操作，需要应用分片技术应对瓶颈)
        1. 路由: mongos.首先我们要了解”片键“的概念，也就是说拆分集合的依据是什么？按照什么键值进行拆分集合….好了，mongos就是一个路由服务器，它会根据管理员设置的“片键”将数据分摊到自己管理的mongod集群，数据和片的对应关系以及相应的配置信息保存在”config服务器”上。
        2. 配置服务器:mongod普通的数据库，一般是一组而图中我们只画了一个，由路由管理。它的作用是记录对数据分片的规则，存储所有数据库元信息（路由、分片）的配置
        3. 片区:具体的存储信息，根据路由配置的片键不同
    3. 储存模式为 Binary Serialized Document Format (BSON), 是类json的一种二进制形式的存储格式，简称Binary JSON

16. MongoDB GridFS:
    0. GridFS Documentation: https://www.mongodb.com/docs/manual/core/gridfs/
    1. GridFS uses a default chunk size of 255 kB; that is, GridFS divides a file into chunks of 255 kB with the exception of the last chunk. The last chunk is only as large as necessary. 
    2. One collection stores the file chunks, and the other stores file metadata.

16. MongoDB Atlas Tutorial:
    https://www.mongodb.com/basics/mongodb-atlas-tutorial

17. MongoDB Atlas Root User:
    Username: diaoenmao-gmailcom
    Password: AI-Apollo
    mongodb+srv://diaoenmao-gmailcom:<password>@synspot-cluster.iqgfk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
    Replace <password> with the password for the diaoenmao-gmailcom user. Replace myFirstDatabase with the name of the database that connections will use by default. Ensure any option params are URL encoded.


