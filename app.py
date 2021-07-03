import os
from flask import Flask ,render_template,request , url_for ,session ,redirect
from add_stud_form import AddstudentForm ,Login ,RequestResetForm,ResetPasswordForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Table, MetaData
from PIL import Image
import secrets
from stud_input import from_name_khnet 
import sqlalchemy
from  flask_mail import Mail,Message
from datetime import datetime



from itsdangerous import URLSafeTimedSerializer as Serializer , SignatureExpired




app=Flask(__name__)
app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME']='swhayl19@gmail.com'
app.config['MAIL_PASSWORD']='swhaylsenbet'
app.run(threaded=True)
mail=Mail(app)



db= create_engine('postgresql://jyjdnpty:DIY0a7-qVNbSCvaGBQUct2aVVR9gxB8G@queenie.db.elephantsql.com:5432/jyjdnpty')
metadata = MetaData(bind=db)
Users= Table('student_info', metadata, autoload=True)
admin_login=Table('sw_hayl_login', metadata, autoload=True)
print(admin_login)


# for password recovery


def ermias():
    data_apreensaoe = datetime.strptime(request.form['data_apreensao'], '%Y-%m-%d')
    print(data_apreensaoe)
    return data_apreensaoe

@app.route("/", methods=['GET', 'POST'])
def home():
    # desc=True
   
    
    return render_template('home.html')


@app.route("/add_student", methods=['GET', 'POST'])


def Registration():
    
    username=""
    # session["username"]
    image_file=""
   
  
    forms=AddstudentForm()
    input_f=from_name_khnet()
    ermias=forms.picture.label
    desc=True
    print(ermias)
    
   
    
        
                
    if forms.validate_on_submit():
       
        net_stud_info=list()
        for i in input_f:
            if(i!=""):
                net_stud_info.insert(0,i)
        net_stud_info.reverse()
        net_stud_info=tuple(net_stud_info)
        print(net_stud_info)
        
        raw_sql="insert into student_info values :net_stud_info_list"
        query=sqlalchemy.text(raw_sql).bindparams(net_stud_info_list=net_stud_info)
        db.execute(query)
   
        
    
        
        
        picture_file = save_picture(forms.picture.data)
        image_file = url_for('static', filename='profile_pics/' +picture_file)
        ermias_check=forms.sebeka_no.data
        
            
        
       
       
    return  render_template('add_student.html', forms=forms ,image_file=image_file ,username=username,desc=desc);

@app.route("/login" , methods=['GET', 'POST'])
def login():
    desc=True
    forms=Login()
    username=""
    if forms.validate_on_submit():
        username=forms.username.data
        password=forms.password.data

        session["username"]=username
        username=session["username"]
        print(username)
        
        ermias=db.execute("select * from sw_hayl_login where admin_username=%(username)s and admin_password=%(password)s",{"username":username,"password":password}).fetchall()
        if ermias:
            return redirect(url_for('Registration'))
        
        
   
    return render_template('login.html', forms=forms ,username=username,desc=desc)
@app.route("/logout")
def logout():
    username=session["username"]
    session.pop("username",None)
    return redirect(url_for("home"))
@app.route("/student_viewer", methods=['GET', 'POST'])
def student_viewer():
    # username=session["username"]
    forms=AddstudentForm()
    search="search"
    username=""
    select_info=""
    desc=False
    general_info_check=False
    agelgay=False
    carrer=False
    
    
    if request.method=='POST':
        if request.form.get('general_info') == 'clicked':
            general_info_check=True
            select_info=db.execute("select stud_code,first_name,last_name,middle_name,christnaname,sex,mothername,dateofbirth,meareg,sebeka_gubae,kfl_ketema,kebele,wereda,lyu_bota,home_num,cell_phone,post,marriage_status from student_info").fetchall()
    if request.method=='POST':
        
        if request.form.get('agelgay_room') == 'clicked':
            agelgay=True
            select_info=db.execute("select stud_code,first_name,first_name	last_name,student_from,course_round,current_duty,senbet_duty_form,current_duty_spec from student_info").fetchall()
    if request.method=='POST':
        if request.form.get('carrer') == 'clicked':
            carrer=True
            select_info=db.execute("select stud_code,first_name,last_name,email,carrer from student_info").fetchall()
            
            username=session["username"]
  
    return render_template('student_viwer.html' ,forms=forms,search=search,username=username,select_info=select_info,general_info_check=general_info_check,agelgay=agelgay,carrer=carrer)
s=Serializer('Thisisascret!')
@app.route("/resetrequest", methods=['GET', 'POST'])
def reset_request():
    token=""
    forms=RequestResetForm()
    if forms.validate_on_submit():
        email=forms.email.data
        swhayl_email="swhayl19@gmail.com"
        if email==swhayl_email:
            changer_name=forms.changer_name.data
            token=s.dumps(email,salt='email-confirm')
            msg=Message('Confirm Email', sender='swhayl19@gmail.com', recipients=[email])
            link=url_for('reset_token',token=token, _external=True)
            msg.body=f'''አቶ {changer_name}  '፤በጠየቁት መሰረት የ ይለፍ ቃሉን ለመቀየር ሊንክ ይጫኑ {link}'''
            mail.send(msg)
    return render_template('reset_request.html',forms=forms,token=token)

@app.route("/resetpassword/<token>", methods=['GET', 'POST'])
def reset_token(token):
    forms=ResetPasswordForm()
    try:
        email=s.loads(token, salt='email-confirm' , max_age=3000)
    except SignatureExpired:
        return '<h2> the token is expired</h2>'
    return render_template('reset_token.html',forms=forms)



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


if __name__ == '__main__':
    app.run(debug=True)
    











#     def get_reset_token(expires_sec=1800):
#     s=Serializer(app.config['SECRET_KEY'],expires_sec)
#     return s.dumps({'user_id':1}).decode('utf-8')

# def verify_reset_token(token):
#     s=Serializer(app.config['SECRET_KEY'])
#     try:
#         user_id=s.loads(token)['userid']
#     except:
#         return None
#     return user_id


# def send_reset_email(user):
#     token=user.get_reset_token()
#     msg=Message('Password reset request',
#     sender='swhayl19@gmail.com', 
#     recipients='swhayl19@gmail.com')
#     msg.body = f'''To reset your password, visit the following link:
#     {url_for('reset_token')}
#     If you did not make this request then simply ignore this email and no changes will be made.
#     '''

# @app.route("/resetrequest", methods=['GET', 'POST'])
# def reset_request():
#     forms=RequestResetForm()
#     if forms.validate_on_submit():
#         admin_email="swhayl19@gmail.com"
#         print(forms.email.data)
#         send_reset_email(admin_email)
#         return redirect(url_for('login'))

#     return render_template('reset_request.html',forms=forms)



# @app.route("/resetpassword/<token>", methods=['GET', 'POST'])
# def reset_token(token):
#     forms=ResetPasswordForm()
      
#     admin=user_id.verify_reset_token(token)
#     if user is None:
#         print("that is invalid token")
#         return redirect(url_for('reset_request'))
    
#     if form.validate_on_submit():
#         Password =(form.password.data)
#         admin.password = Password
#         db.session.commit()
#         print('Your password has been updated! You are now able to log in', 'success')
#         return redirect(url_for('login'))
    
#     return render_template('reset_token.html',forms=forms)

