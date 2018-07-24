from project import db

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User %d %s' % (self.id, self.username)

'''class Post():
    __tablename__='posts'
    PostID         = Column(Integer, primary_key=True, autoincrement=True)
    AuthorID       = Column(Integer, ForeignKey('user.UserID'))
    Title          = Column(String(20), nullable=False)
    Text           = Column(String, nullable=False)
    Rating         = Column(Integer)
'''