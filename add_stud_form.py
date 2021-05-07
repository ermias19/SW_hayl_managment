
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy

class AddstudentForm(FlaskForm):
    picture = FileField(' Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    stud_code=StringField('ተራ ቁጥር')
    username=StringField('1. ስም')
    fathername=StringField('የአባት ስም')
    ayatname=StringField('የአያት ስም')
    christnaname=StringField('2.የክርስትና ስም')
    sex=StringField('ፆታ')
    mothername=StringField('የእናት ሙሉ ስም')
    dateofbirth=StringField('3.የትውልድ ዘመን ወር')
    meareg=StringField('ማእረግ:-ዲያቆን/መሪጌታ/(ወሮ/ሪት)/አቶ')
    sebeka_yes=StringField('አዎ')
    sebeka_no=StringField('አይ')
# 
    kebele=StringField('ቀበሌ')
    kfl_ketema=StringField('ክ/ከተማ')
    wereda=StringField('ወረዳ')
    silk_kutr=StringField('ስልክ ቁጥር')
    lyu_bota=StringField('ልዩ ቦታ')
    home_num=StringField('የቤት ቁጥር')
    cell_phone=StringField('ሞባይል')
    post=StringField('ፖስታ')
    email=StringField('ኢሜል')

    yegel=StringField('የግል')
    mengest=StringField('የመንግስት ተቀጣሪ')
    begel_derejet=StringField('በግ/ድርጅት')
    felagi=StringField('ፈላጊ')

    yageba_ch=StringField('ያገባ/ች ')
    yalageba_ch=StringField('ያላገባ/ች')
    ag_yefeta=StringField('የፈታች የሞተበት ባት')

    student_from=StringField('የሰንበት ት/ቤቱ አባል የሆኑበት ዓ.ም')
    course_round=StringField('የኮርስ ዙር')
    current_duty=StringField('አሁን የሚያገለግሉብት ክፍል ስም')
    senbet_duty_form=StringField('አገልግሎቱን የጀመሉበት ዓ.ም')
    current_duty_spec=StringField('አሁን የሚያገለግሉብት ክፍል ውስጥ ያልዎት የስራ ድርሻ')
    
    
    submit=SubmitField('ፎቶ ምስል አስገባ')


class Login(FlaskForm):
    username=StringField('username',validators=[DataRequired()])
   
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('log in')

    

