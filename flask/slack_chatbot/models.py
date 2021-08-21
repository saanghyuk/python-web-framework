from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(256))
    tstamp = db.Column(db.DateTime, server_default=db.func.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user': self.user.userid,
            # 아래서 입력한 Relationship 때문에 이렇게 입력이 가능한 것.
            'title': self.title,
            'tstamp': self.tstamp
        }


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(128))
    userid = db.Column(db.String(128))

    todos = db.relationship('Todo', backref='user', lazy=True)
