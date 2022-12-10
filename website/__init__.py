from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os 
from flask_login import LoginManager


db=SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    """
    summary : this function create the server instance and register the blueprints

    args : none
    return : the server instance

    """

    app = Flask(__name__) # server instance
    app.config['SECRET_KEY'] = 'asdf1234'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .view import view 
    from .auth import auth


    app.register_blueprint(view,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    from . import model 
    from .model import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    with app.app_context():
        db.create_all()



    return app



def create_database(apps):
    """
    summary : this function create the database if it doesn't exist 

    args : app --> the server instance
    return : none
    
    """
    if not os.path.exists('website/'+DB_NAME):
        db.create_all(app=apps)
        print('created database')


