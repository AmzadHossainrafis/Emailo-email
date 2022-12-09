from flask import Blueprint , render_template , request ,redirect,url_for,flash
from flask_login import login_required,current_user
view = Blueprint('view',__name__) 
from sqlalchemy import desc
from .model import Inbox
from . import db
@view.route('/') 
@login_required
def home():
    return render_template('home.html')

@view.route('/dash',methods=['GET','POST']) 
def user_dashboard():
    if request.method == 'POST':
        id = request.form.get('id')
        inbox = request.form.get('inbox')
        subject = request.form.get('subject')
        massage = request.form.get('massage')   
        category = request.form.get('category')
      


        if inbox==current_user.email: 
            flash('you cant send a massage to yourself',category='error')
            return redirect(url_for('view.user_dashboard'))
        else: 
            new_inbox = Inbox(id=id,inbox=inbox,massage=massage,user_id=current_user.id,subject=subject,mail_form=current_user.email,category=category)
            db.session.add(new_inbox)
            db.session.commit()
            flash('massage sent',category='success')
        return redirect(url_for('view.user_dashboard'))
  
    



    find_all_primary = Inbox.query.filter_by(inbox=current_user.email,category='primary').order_by(desc(Inbox.date_created))
    find_all_social = Inbox.query.filter_by(inbox=current_user.email,category='social').order_by(desc(Inbox.date_created))
    find_all_promotion = Inbox.query.filter_by(inbox=current_user.email,category='promotion').order_by(desc(Inbox.date_created))


    return render_template('user_dash.html', find_all_primary=find_all_primary,find_all_social=find_all_social,find_all_promotion=find_all_promotion)
