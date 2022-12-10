from flask import Blueprint,request,render_template,redirect,url_for,session,flash
from .model import User,Inbox
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_required,logout_user,current_user




from . import db 
auth = Blueprint('auth',__name__)
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully',category='success')
                login_user(user,remember=True)

                return redirect(url_for('view.user_dashboard'))
            else:
                flash('Incorrect password',category='error')
        else:
            flash('Email does not exist',category='error')
    return render_template('login.html',boolen=True)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/sighup',methods=['GET','POST'])
def signup():





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

