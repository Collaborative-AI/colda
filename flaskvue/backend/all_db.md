1. User:(Store user information)
      __tablename__ = 'users'
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(64), index=True, unique=True)
      email = db.Column(db.String(120), index=True, unique=True)
      password_hash = db.Column(db.String(128))
      name = db.Column(db.String(64))
      location = db.Column(db.String(64))
      about_me = db.Column(db.Text())
      last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
      last_messages_read_time = db.Column(db.DateTime)

      messages_sent = db.relationship('Message', foreign_keys='Message.sender_id',
                                    backref='sender', lazy='dynamic',
                                    cascade='all, delete-orphan')
      # Message User received
      messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic',
                                        cascade='all, delete-orphan')

      # Notification
      notifications = db.relationship('Notification', backref='user',
                                    lazy='dynamic', cascade='all, delete-orphan')


2. Message: (Store single message)
      __tablename__ = 'messages'
      id = db.Column(db.Integer, primary_key=True)
      body = db.Column(db.Text)
      timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
      sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
      recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'))
      task_id = db.Column(db.Integer, index=True, unique=True)
      rounds = db.Column(db.Integer)

3. Notification: (new notification)
      __tablename__ = 'notifications'
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(128), index=True)
      timestamp = db.Column(db.Float, index=True, default=time)
      payload_json = db.Column(db.Text)
      user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

4. User_to_task: (record the relationship)
      __tablename__ = 'user_to_task'
      username = db.Column(db.String(128), primary_key=True)
      task_id = db.Column(db.Integer, index=True, unique=True)


5. Task Record: (record the task (server))
      __tablename__ = 'task'
      id = db.Column(db.Integer, primary_key=True)
      task_id = db.Column(db.Integer, index=True, unique=True)
      starter_initial = db.Column(db.String)
      recipient_initial = db.Column(db.String)
      
      Intersect_initial = db.Column(db.String)
      round: 


6. Local database: (store information locally (local))
      __tablename__ = 'local_database'
      task_id = db.Column(db.Integer, primary_key=True)
      rounds = db.Column(db.Integer)
      sender_id = db.Column(db.Integer)
      recipient_id = db.Column(db.Integer)
      body = db.Column(db.Text)
      timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)



Serverdatabase
    task ID
        match: A, B, Intersect
        UserA_initial:
        UserB_initial:
        Intersect_initial:
        "第几次+(A,B)": url_for(y), intersect
        
db_metadata:
    task ID
        match: A, B, Intersect
        UserA_initial:
        UserB_initial:
        Intersect_initial:
        autoinc: url_for(y)