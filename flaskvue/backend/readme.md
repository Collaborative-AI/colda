1. First time launch:
    1. cd into backend
    2. pip install pipenv
    3. pipenv install
    4. pipenv shell
    5. flask run

2. launch after first time
    1. pipenv install
    2. pipenv shell
    3. flask run


4. Install Package: pipenv install + package name

5. Migrate the database: 
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



.env: 系统环境变量

<!-- python app.py runserver -d -r -h 0.0.0.0 -p 5000 (运行)
python manage.py runserver -d -h 127.0.0.1 -p 5000 -->

<!-- gunicorn: gunicorn --worker-class eventlet -w 1 module:app -->