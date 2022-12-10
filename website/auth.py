from flask import Blueprint,request,render_template,redirect,url_for,flash
from .model import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_required,logout_user
from . import db 




auth = Blueprint('auth',__name__) # auth blueprint
@auth.route('/login',methods=['GET','POST']) # login route with methods get and post 
def login():
    """
    summary : this is the login page where the user can login to his account , if the user try to login with a wrong email or password flash
    a message and redirect him to the dashboard, this section of code also check if the password is correct or not

    args : none 
    return : the login page

    """
    if request.method == 'POST': 
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:                                            # if the user exist check the password
            if check_password_hash(user.password,password):
                flash('Logged in successfully',category='success')
                login_user(user,remember=True)

                return redirect(url_for('view.user_dashboard'))
            else:
                flash('Incorrect password',category='error')
        else:
            flash('Email does not exist',category='error')
    return render_template('login.html',boolen=True)



@auth.route('/logout') # logout route
@login_required # login required decorator , the user must be logged in to access this route
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/sighup',methods=['GET','POST']) # sighup route with methods get and post
def signup():
    """
    summary : this is the sighup page where the user can create a new account , if the user try to create an account with an email that already exist
    flash a message and redirect him to the dashboard, this section of code also check if the password  is valid or not , inclodig the email and the first name len 
    and the password len . 

    args : none
    return : the sighup page
    """




    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first() 


        if user :
            flash('Email already exists',category='error')
        elif len(email) < 4:
            flash('email must be greater than 3 characters.',category='error')
        elif len(first_name) < 2:
            flash('first name must be greater than 1 character.',category='error')
       
        elif len(password) < 7:
            flash('password must be at least 7 characters.',category='error')
        else:
            #add user to database
            new_user = User(email=email,first_name=first_name,last_name =last_name,password=generate_password_hash(password,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('account created!',category='success')
            return redirect(url_for('auth.login'))
    return render_template('sighup.html',boolean=True)

