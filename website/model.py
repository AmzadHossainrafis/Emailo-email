from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func 


class Inbox(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    inbox = db.Column(db.String(150))
    subject = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True),default=func.now())
    massage = db.Column(db.String(1500))
    mail_form= db.Column(db.String(150)) 
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
   
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True),default=func.now())
    inbox = db.relationship('Inbox',backref='user')