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

<!-- python app.py runserver -d -r -h 0.0.0.0 -p 5000 (运行)
python manage.py runserver -d -h 127.0.0.1 -p 5000 -->

<!-- gunicorn: gunicorn --worker-class eventlet -w 1 module:app -->

11. 上服务器:
    注掉create_unittest_user


12. Docker教程:
    0. Basic concept:
        Image（镜像）: 构建和打包 / 菜
        Container（容器）: 执行和启动 / 饭盒
    1. 建立Dockerfile
    2. In Dockerfile, type:
        1. FROM

13. Elastic BeanStalk:
    1. Preparation: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html
    2. navigate to backend file
    3. Freeze requirements:
        pipenv lock -r > requirements.txt 
    4. brew install awsebcli
    5. https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html (follow this or jump to step 6)
    6. eb init -p python-3.8 synspot --region us-east-2
    7. (Optional) If you meet: You have not yet set up your credentials or your credentials are incorrect
        You must provide your credentials.
        (aws-access-id): from step 6 => https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-configuration.html => https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys
        Or you can use this directly:
        aws-access-id: AKIAW7PAIJ4ER2AWJUVR
        aws-secret-key: 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   
    8. eb create synspot-env
    9. Reminder: run flask cli in AWS elastic beanstalk need some operations. (https://stackoverflow.com/questions/65729668/how-to-run-flask-cli-command-in-aws-elastic-beanstalk) 
    10. create .ebextensions
    11. add (https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers-ec2.html#linux-commands):
        commands:
          command1:
            command: flask run
    10. eb open