from flask import Blueprint , render_template , request ,redirect,url_for,flash
from flask_login import login_required,current_user
view = Blueprint('view',__name__) 
from sqlalchemy import desc
from .model import Inbox
from . import db





@view.route('/')  # home page route 
def home():
    '''
    summary : this is the home page of the website

    
    '''
    return render_template('home.html')







@view.route('/dash',methods=['GET','POST'])  # user dashboard route
def user_dashboard():
    '''
    summary : this is the user dashboard where the user can see all the massages
        he/she has received and also send a new massage to another user
     
     args : none 


    return : the user dashboard page
     
     '''
    if request.method == 'POST':
        id = request.form.get('id')
        inbox = request.form.get('inbox')
        subject = request.form.get('subject')
        massage = request.form.get('massage')   
        category = request.form.get('category')
      


        if inbox==current_user.email:                # if the user try to send a massage to himself flash a message and redirect him to the dashboard
            flash('you cant send a massage to yourself',category='error')
            return redirect(url_for('view.user_dashboard'))
        else:                                       # if the user try to send a massage to another user add the massage to the database and redirect him to the dashboard
            new_inbox = Inbox(id=id,inbox=inbox,massage=massage,user_id=current_user.id,subject=subject,mail_form=current_user.email,category=category)
            db.session.add(new_inbox)
            db.session.commit()
            flash('massage sent',category='success')
        return redirect(url_for('view.user_dashboard'))
  
    



    find_all_primary = Inbox.query.filter_by(inbox=current_user.email,category='primary').order_by(desc(Inbox.date_created))        # find all the email where category is primary and order them by the date they were created 
    find_all_social = Inbox.query.filter_by(inbox=current_user.email,category='social').order_by(desc(Inbox.date_created))          # find all the email where category is SOCIAL
    find_all_promotion = Inbox.query.filter_by(inbox=current_user.email,category='promotion').order_by(desc(Inbox.date_created))    # find all the email where category is PROMOTION
    find_all_forums = Inbox.query.filter_by(inbox=current_user.email,category='foram').order_by(desc(Inbox.date_created))          # find all the email where category is FORUMS  


    return render_template('user_dash.html', find_all_primary=find_all_primary,find_all_social=find_all_social,find_all_promotion=find_all_promotion,find_all_forums=find_all_forums)
