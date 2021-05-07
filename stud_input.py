from add_stud_form import AddstudentForm
def from_name_khnet():
    input_data=AddstudentForm()
    stud_code=input_data.stud_code.data
    first_name=input_data.username.data
    last_name=input_data.fathername.data
    middle_name=input_data.ayatname.data
    christnaname=input_data.christnaname.data
    sex=input_data.sex.data
    mothername=input_data.mothername.data
    dateofbirth=input_data.dateofbirth.data
    meareg=input_data.meareg.data


   
    sebeka_yes=input_data.sebeka_yes.data
    sebeka_no=input_data.sebeka_no.data
    kebele=input_data.kebele.data
    kfl_ketema=input_data.kfl_ketema.data
    wereda=input_data.wereda.data
    silk_kutr=input_data.silk_kutr.data
    lyu_bota=input_data.lyu_bota.data
    home_num=input_data.home_num.data
    cell_phone=input_data.cell_phone.data
    post=input_data.post.data
    email=input_data.email.data

     
    yegel=input_data.yegel.data
    mengest=input_data.mengest.data
    begel_derejet=input_data.begel_derejet.data
    felagi=input_data.felagi.data

    yageba_ch=input_data.yageba_ch.data
    yalageba_ch=input_data.yalageba_ch.data
    ag_yefeta=input_data.ag_yefeta.data

    student_from=input_data.student_from.data
    course_round=input_data.course_round.data
    current_duty=input_data.current_duty.data
    senbet_duty_form=input_data.senbet_duty_form.data
    current_duty_spec=input_data.current_duty_spec.data

    return stud_code,first_name ,last_name ,middle_name ,christnaname ,sex ,mothername ,dateofbirth ,meareg ,sebeka_yes,sebeka_no,kebele,kfl_ketema,wereda,silk_kutr,lyu_bota,home_num,cell_phone,post,email ,yegel,mengest,begel_derejet,felagi, yageba_ch,yalageba_ch,ag_yefeta ,student_from ,course_round ,current_duty ,senbet_duty_form ,current_duty_spec
















# create table student_info(
#     stud_code varchar(50) ,
#     first_name varchar(50),
#     last_name varchar(50),
#     middle_name varchar(50),
#     christnaname varchar(50),
#     sex varchar(50),
#     mothername varchar(50),
#     dateofbirth varchar(50),
#     meareg varchar(50),
#     sebeka_gubae varchar(50),
#     kebele varchar(50),
#     kfl_ketema varchar(50),
#     wereda varchar(50),
#     silk_kutr varchar(50),
#     lyu_bota varchar(50),
#     home_num varchar(50),
#     cell_phone varchar(50),
#     post varchar(50),
#     email varchar(50),
#     carrer varchar(50),
#     marriage_status varchar(50),
#     student_from varchar(50),
#     course_round varchar(50),
#     current_duty varchar(50),
#     senbet_duty_form varchar(50),
#     current_duty_spec varchar(50))