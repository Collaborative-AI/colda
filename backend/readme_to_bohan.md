1. launch procedures
    0. export FLASK_APP=application.py (first time you clone the github)
    1. pipenv install
    2. pipenv shell
    3. flask run

2. Unittest:
    1. flask test (test all files, use this command in top file level)
    2. notes: You could switch the test framework to pytest, which is more convenient
    3. notes: tests/test_unread_test_output.py contains most the logic for your reference

3. Deploy:
    0. Install some dependencies first: https://www.youtube.com/watch?v=D2GLVoiEZyE&ab_channel=ArpanNeupane
    1. heroku login (Use username and pwd in google drive key file)
    2. git add .
    3. git commit -m 'Commit_Name'
    4. git push 
    5. git push heroku Current_branch_name
    6. heroku open (view our app)