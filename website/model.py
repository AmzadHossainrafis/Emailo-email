from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func 


class Inbox(db.Model):
    """
    summary :   this is the Inbox table where all the massages are stored
                columns : id , inbox , subject , date_created , massage , mail_form , category , user_id
                primary key : id
                foreign key : user_id
    args : none 
    return : none 
                
    """
    id = db.Column(db.Integer,primary_key=True)
    inbox = db.Column(db.String(150))
    subject = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True),default=func.now())
    massage = db.Column(db.String(1500))
    mail_form= db.Column(db.String(150)) 
    category = db.Column(db.String(50)) 
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
   
class User(db.Model,UserMixin):
    """
    summary :   this is the User table where all the users are stored
                columns : id , email , first_name , last_name , password , date_created , inbox
                primary key : id
                foreign key : inbox

    args : none
    return : none

    
    """
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True),default=func.now())
    inbox = db.relationship('Inbox',backref='user')