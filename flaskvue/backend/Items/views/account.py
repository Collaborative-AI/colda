from flask import Blueprint, render_template, request, session, redirect
from uuid import uuid4

account = Blueprint('account', __name__)
# Same prefix
# account = Blueprint('account', __name__, url_prefix='/admin')

@account.before_request
def bf():
    #g.x = "a"
    print("axxxxx")

@account.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'Apollo' and pwd == '123':
        uid = str(uuid4())
        session.permanent = True
        session['user_info'] = {'id':uid, 'name':user}
        return redirect('/index')
    else:
        return render_template('login.html', msg='user = Apollo, apwd = 123')