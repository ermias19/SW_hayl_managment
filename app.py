import os
from flask import Flask ,render_template,request , url_for ,session ,redirect
from add_stud_form import AddstudentForm ,Login

from sqlalchemy import create_engine, Table, MetaData
from PIL import Image

from stud_input import from_name_khnet 
import sqlalchemy




app=Flask(__name__)
app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'

db= create_engine('postgresql://jyjdnpty:DIY0a7-qVNbSCvaGBQUct2aVVR9gxB8G@queenie.db.elephantsql.com:5432/jyjdnpty')
metadata = MetaData(bind=db)
Users= Table('student_info', metadata, autoload=True)




@app.route("/", methods=['GET', 'POST'])
def home():
    desc=True
   
    
    return render_template('layout.html',desc=desc)

@app.route("/add_student", methods=['GET', 'POST'])

def Registration():
    
    username=session["username"]
    image_file=""
    forms=AddstudentForm()
    input_f=from_name_khnet()
    desc=True
    
    if forms.validate_on_submit():
        net_stud_info=list()
        for i in input_f:
            if(i!=""):
                net_stud_info.insert(0,i)
        net_stud_info.reverse()
        net_stud_info=tuple(net_stud_info)
        
        raw_sql="insert into student_info values :net_stud_info_list"
        query=sqlalchemy.text(raw_sql).bindparams(net_stud_info_list=net_stud_info)
        db.execute(query)
        
        
        picture_file = save_picture(forms.picture.data)
        image_file = url_for('static', filename='profile_pics/' +picture_file)
        ermias_check=forms.sebeka_no.data
       
            
        
       
       
    return render_template('add_student.html', forms=forms ,image_file=image_file ,username=username,desc=desc);

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
    forms=AddstudentForm()
    search="search"
    username=""
    general_info=""
    desc=False
    general_info_check=False
    agelgay=False
    carrer=False
    
    general_info_button=request.form.get("general_info")
    if request.method=='POST':
        if request.form.get('general_info') == 'clicked':
            general_info_check=True
            general_info=db.execute("select stud_code,first_name,last_name,middle_name,christnaname,sex,mothername,dateofbirth,meareg,sebeka_gubae,kfl_ketema,kebele,wereda,silk_kutr,lyu_bota,home_num,cell_phone,post,marriage_status from student_info").fetchall()
    if request.method=='POST':
        
        if request.form.get('agelgay_room') == 'clicked':
            agelgay=True
            general_info=db.execute("select stud_code,first_name,first_name	last_name,student_from,course_round,current_duty,senbet_duty_form,current_duty_spec from student_info").fetchall()
    if request.method=='POST':
        if request.form.get('carrer') == 'clicked':
            carrer=True
            general_info=db.execute("select stud_code,first_name,last_name,email,carrer from student_info").fetchall()
            
            username=session["username"]
  
    return render_template('student_viwer.html' ,forms=forms,search=search,username=username,general_info=general_info,general_info_button=general_info_button,general_info_check=general_info_check,agelgay=agelgay,carrer=carrer)





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