from flask import Flask ,Blueprint , render_template , request ,redirect,url_for,session,flash
from flask_login import login_user,login_required,logout_user,current_user
view = Blueprint('view',__name__) 
from .model import Inbox
from . import db
@view.route('/') 
@login_required
def home():
    return 'this is not the right plce to be'

@view.route('/dash',methods=['GET','POST']) 
def user_dashboard():
    if request.method == 'POST':
        id = request.form.get('id')
        inbox = request.form.get('inbox')
        subject = request.form.get('subject')
        massage = request.form.get('massage')   
        category = request.form.get('category')
        new_inbox = Inbox(id=id,inbox=inbox,massage=massage,user_id=current_user.id,subject=subject,mail_form=current_user.email,category=category)
        db.session.add(new_inbox)
        db.session.commit()
        flash('massage sent',category='success')
        return redirect(url_for('view.user_dashboard'))
    inbox = Inbox.query.filter_by(inbox=current_user.email).all()
    #group by catagory and sort by date 
    



    find_all_primary = Inbox.query.filter_by(inbox=current_user.email,category='primary').all()
    find_all_social = Inbox.query.filter_by(inbox=current_user.email,category='social').all()
    find_all_promotion = Inbox.query.filter_by(inbox=current_user.email,category='promotion').all()
 



    return render_template('user_dash.html',inbox=inbox, find_all_primary=find_all_primary,find_all_social=find_all_social,find_all_promotion=find_all_promotion)
