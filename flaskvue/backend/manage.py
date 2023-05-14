# -*- coding: utf-8 -*-
from Items import create_app
from Items.extensions import db
from Items.models import User, Notification, Message, Matched
from setting import Config

app = create_app(Config)

@app.cli.command()
def test():
   # flask test
   # flask run
    '''Run the unit tests.'''
    import unittest
    tests = unittest.TestLoader().discover('tests') 
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Notification': Notification, 'Message': Message, 'Matched': Matched}







# if __name__ == '__main__':
#     # socketio.run(app, debug = True, host="127.0.0.1", port=5000)
#     app.run()
    # app.run(app, debug = True, host="127.0.0.1", port=5000)
    # manager.run()
    # app.run()
    # python manage.py runserver -d -r -h 0.0.0.0 -p 5000 (运行)
