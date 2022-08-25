1. launch procedures
    0. export FLASK_APP=application.py (first time you clone the github)
    1. pipenv install
    2. pipenv shell
    3. flask run

2. Unittest:
    1. cd tests
    2. flask test (test all files) or python -m unittest test_filename.py (test single file)
    3. notes: You could switch the test framework to pytest, which is more convenient