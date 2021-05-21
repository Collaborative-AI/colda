from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import NameForm, RoomForm
import random


@main.route('/ceshi',methods=['GET'])
def ceshi():
  return "chenggong"

@main.route('/diyi', methods=['GET', 'POST'])
def Login():
    """Login form to enter a room."""
    form = NameForm()
    if form.validate_on_submit():
        
        session['name'] = form.name.data

        random_index = random.randint(0,10000)
        session['random_index'] = random_index

        session['name_to_random_index'] = (form.name.data, random_index)
        # session['room'] = form.room.data
        return redirect(url_for('main.index'))
        # render_template('main_page.html')
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        # form.room.data = session.get('room', '')
    return render_template('login.html', form=form)
    # return render_template('main_page.html')

# @main.route('/main_page', methods=['GET', 'POST'])
# def main_page():
#     # return None
#     render_template('main_page.html')
    

@main.route('/index1', methods=['GET', 'POST'])
def index1():
    """Login form to enter a room."""
    form = RoomForm()
    # form = ConnectUserForm()
    if form.validate_on_submit():
        # session['user'] = form.user.data
        session['room'] = form.room.data
        return redirect(url_for('main.chat'))
    elif request.method == 'GET':
        # form.user.data = session.get('user', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', name=session.get('name', ''), form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    
    name = session.get('name', '')
    room = session.get('room', '')
    print("name",name,"room",room)
    if name == '' or room == '':
        return redirect(url_for('main.index'))
    return render_template('chat.html', name=name, room=room)

