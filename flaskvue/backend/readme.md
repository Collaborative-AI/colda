1. pipenv install

2. pipenv shell

3. flask run

4. Install Package: pipenv install + package name

5. Migrate the database: 
     1. flask db migrate -m "comment"
     2. flask db upgrade (flask db downgrade => rollback)
            
6. Test: 
    
        1. modify the python code in Test files
        2. Running: flask test
    
7. 2 users:
      1. id=4 username=testa email=126@gmail.com password=123
      2. id=5 username=testb email=127@gmail.com password=123


Second way:
1. configure the make_shell_context() in manage.py (Start a python interpreter containing the context of the application)

2. Execution:
        Use HTTPie to test the API (need 2 terminals)
            1. run the flask in one terminal (1-3 steps) (must run the server)
            2. Do 1-2 steps in another terminal, then command. Example: 
            http POST http://localhost:5000/users username=test1 password=123



.env: 系统环境变量

<!-- python app.py runserver -d -r -h 0.0.0.0 -p 5000 (运行)
python manage.py runserver -d -h 127.0.0.1 -p 5000 -->

<!-- gunicorn: gunicorn --worker-class eventlet -w 1 module:app -->