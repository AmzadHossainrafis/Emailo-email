#import flask , render_template , request , redirect , url_for , session , flash,user login 
from flask import Flask , render_template , request ,redirect,url_for,session,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from website import create_app 


app = create_app() 

    
if __name__ == '__main__':
    app.run(debug=True)
