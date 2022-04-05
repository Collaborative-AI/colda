# -*- coding: utf-8 -*-
from Items import create_app
from config import Config

application = create_app(Config)

@application.route('/')
def hello_world():
    return 'Hello, World!!!!WOW!!!'

@application.cli.command()
def test():
   # flask test
   # flask run
    '''Run the unit tests.'''
    import unittest
    tests = unittest.TestLoader().discover('tests') 
    unittest.TextTestRunner(verbosity=2).run(tests)

@application.shell_context_processor
def make_shell_context():
    pass






# if __name__ == '__main__':
#     # socketio.run(app, debug = True, host="127.0.0.1", port=5000)
#     app.run()
    # app.run(app, debug = True, host="127.0.0.1", port=5000)
    # manager.run()
    # app.run()
    # python manage.py runserver -d -r -h 0.0.0.0 -p 5000 (运行)
