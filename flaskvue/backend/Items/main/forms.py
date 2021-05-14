from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[Required()])
    submit = SubmitField('Enter Your Name')

class RoomForm(FlaskForm):
    """Accepts a nickname and a room."""
    room = StringField('Room', validators=[Required()])
    # user = StringField('Connect User', validators=[Required()])
    submit = SubmitField('Enter Chatroom')

# class ConnectUserForm(FlaskForm):
#     """Accepts a nickname and a room."""
#     room = StringField('Connect User', validators=[Required()])
#     submit = SubmitField('Enter User Name')