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
        new_inbox = Inbox(id=id,inbox=inbox,massage=massage,user_id=current_user.id,subject=subject)
        db.session.add(new_inbox)
        db.session.commit()
        flash('massage sent',category='success')
        return redirect(url_for('view.user_dashboard'))

    return render_template('user_dash.html') 