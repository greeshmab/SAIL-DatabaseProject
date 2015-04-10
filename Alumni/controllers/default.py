# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))
    
    form1 = XML("<select><option value=\"volvo\">Volvo</option><option value=\"saab\">Saab</option><option value=\"mercedes\">Mercedes</option></select>")
    form1=FORM(INPUT(_type='select',_name='user',_value='Professor'),'Professor',_action=URL('checking'))
    """
    form = SQLFORM.factory(Field('username',requires=IS_EMAIL()),
                           Field('password','password',
                                 requires=IS_NOT_EMPTY()),
                           submit_button='Login').process()
    if form.accepted:
        response.flash = 'Accepted IT'
        session.b = form.vars.username
        session.a = form.vars.password
        redirect(URL('login_verify'))
        return locals()

    elif form.errors:
        session.flash = 'Errors..!'
    else:
        response.flash = 'welcome bro'
    return locals()
def login():
    form = SQLFORM.factory(Field('username',requires=IS_EMAIL()),
                             Field('password','password'),
                             submit_button='Login').process()
    return locals()
def login_verify():
    if(session.b=='admin@gmail.com'):
        user_type = 'admin'
    else:
        user_type='alumni'
    if(user_type=='admin'):
        if db.admin_log_in(admin_id=session.b)==None:
            redirect(URL('index'))
        else:
            pas = db.admin_log_in(admin_id=session.b).password
            if pas == session.a:
                session.flash = 'welcome.!'
                redirect(URL('admin_r'))
            else:
                session.flash='Invalid Credentials'
                redirect(URL('index'))

    if(user_type=='alumni'):
        session.flash = 'welcome mike batio.!'
        if db.user_log_in(iitg_webmail_id=session.b)==None:
            redirect(URL('index'))
        else:
            pas = db.user_log_in(iitg_webmail_id=session.b).password
            if pas == session.a:
                session.flash = 'welcome.!'
                redirect(URL('alumni'))
            else:
                session.flash='Invalid Credentials'
                redirect(URL('index'))


def alumni():
    if db.alumni_basic_data(iitg_webmail_id=session.b)==None:
        session.c=1
    else:
        session.c=2
        session.flash='Invalid Credentials'
        """
        intermediate page
        """
    if db.othr_univ_degree(iitg_webmail_id=session.b)==None:
        session.d=1
    else:
        session.d=2
        session.flash='Invalid Credentials'
    if db.iitg_deg(iitg_webmail_id=session.b)==None:
        session.e=1
    else:
        session.e=2
        session.flash='Invalid Credentials'
    if db.past_employment(iitg_webmail_id=session.b)==None:
        session.f=1
    else:
        session.f=2
        session.flash='Invalid Credentials'
    redirect(URL('alumni_intm_page'))
    return locals()
def alumni_intm_page():
    if db.alumni_basic_data(iitg_webmail_id=session.b)==None:
        session.flash='yoyo'
    else:
        redirect(URL('prin'))
        
    return locals()
    
    
def admin_r():
    Alumni_id = SQLFORM.grid(db.user_log_in,user_signature=False)
    Admin_id = SQLFORM.grid(db.admin_log_in,user_signature=False)
    return locals()

def alumni_edit():
    Details = FORM(TABLE(TR("Title",SELECT('Dr','Mr','Ms','Mrs',_name="title",requires=IS_IN_SET(['yeas','no']))),
                   TR("First Name:",INPUT(_type="text",_name="first_name",requires=IS_NOT_EMPTY())),
                   TR("Last Name:",INPUT(_type="text",_name="last_name",requires=IS_NOT_EMPTY())),
                   TR("Email id:",INPUT(_type="text",_name="email",requires=IS_EMAIL())),
                   TR("Alternate Email:",INPUT(_type="text",_name="email",requires=IS_EMAIL())),
                   TR("Phone No:",INPUT(_type="text",_name="phno",requires=IS_NOT_EMPTY())),
                   TR("Date Of Birth:",INPUT(_type="string",_name="dob",_class="date")),
                   TR("Current_Address_Line_1:",INPUT(_type="text",_name="Current_Address_Line_1",requires=IS_NOT_EMPTY())),
                   TR("Current_Address_Line_2:",INPUT(_type="text",_name="Current_Address_Line_2",requires=IS_NOT_EMPTY())),
                   TR("Current_City:",INPUT(_type="text",_name="Current_City",requires=IS_NOT_EMPTY())),
                   TR("Current_State:",INPUT(_type="text",_name="Current_State",requires=IS_NOT_EMPTY())),
                   TR("Current_Country:",INPUT(_type="text",_name="Current_Country",requires=IS_NOT_EMPTY())),
                   TR("Current Emp Role:",INPUT(_type="text",_name="Current_Emp_Role",requires=IS_NOT_EMPTY())),
                   TR("Current Comp/Org:",INPUT(_type="text",_name="Current_Company",requires=IS_NOT_EMPTY())),
                   TR("Current Industry:",INPUT(_type="text",_name="Current_Industry",requires=IS_NOT_EMPTY())),
                   TR("Current emp started from:",INPUT(_type="string",_name="Current_Emp_Started_From",_class="date"))),
                   INPUT(_type='submit',value='Submit'),_action=URL('insert'))
    IITG_Degree1=FORM(TABLE(
                    TR("Degree",INPUT(_type="text",_name="deg",requires=IS_NOT_EMPTY())),
                    TR("Department",INPUT(_type="text",_name="dept",requires=IS_NOT_EMPTY())),
                    TR("Started_On",INPUT(_type="string",_name="start_year",_class="date")),
                    TR("Graduated_On",INPUT(_type="string",_name="end_year",_class="date"))),
                    INPUT(_type='submit',value='Submit'),_action=URL('update1'))
    IITG_Degree2=FORM(TABLE(
            TR("Degree",INPUT(_type="text",_name="deg",requires=IS_NOT_EMPTY())), 
            TR("Department",INPUT(_type="text",_name="dept",requires=IS_NOT_EMPTY())),
            TR("Started_On",INPUT(_type="string",_name="start_year",_class="date")),
            TR("Graduated_On",INPUT(_type="string",_name="end_year",_class="date"))),
                      INPUT(_type='submit',value='Submit'),_action=URL('update1'))
    IITG_Degree3=FORM(TABLE(
            TR("Degree",INPUT(_type="text",_name="deg",requires=IS_NOT_EMPTY())), 
            TR("Department",INPUT(_type="text",_name="dept",requires=IS_NOT_EMPTY())),
            TR("Started_On",INPUT(_type="string",_name="start_year",_class="date")),
            TR("Graduated_On",INPUT(_type="string",_name="end_year",_class="date"))),
                      INPUT(_type='submit',value='Submit'),_action=URL('update1'))
    Other_School_Degree1=FORM(TABLE(
            TR("Degree",INPUT(_type="text",_name="deg",requires=IS_NOT_EMPTY())), 
            TR("Department",INPUT(_type="text",_name="dept",requires=IS_NOT_EMPTY())),
            TR("University",INPUT(_type="text",_name="univ",requires=IS_NOT_EMPTY())),
            TR("Started_On",INPUT(_type="string",_name="start_year",_class="date")),
            TR("Graduated_On",INPUT(_type="string",_name="end_year",_class="date"))),
                      INPUT(_type='submit',value='Submit'),_action=URL('update2'))
    Other_School_Degree2=FORM(TABLE(
            TR("Degree",INPUT(_type="text",_name="deg",requires=IS_NOT_EMPTY())), 
            TR("Department",INPUT(_type="text",_name="dept",requires=IS_NOT_EMPTY())),
            TR("University",INPUT(_type="text",_name="univ",requires=IS_NOT_EMPTY())),
            TR("Started_On",INPUT(_type="string",_name="start_year",_class="date")),
            TR("Graduated_On",INPUT(_type="string",_name="end_year",_class="date"))),
                      INPUT(_type='submit',value='Submit'),_action=URL('update2'))
    Other_School_Degree3=FORM(TABLE(
            TR("Degree",INPUT(_type="text",_name="deg",requires=IS_NOT_EMPTY())), 
            TR("Department",INPUT(_type="text",_name="dept",requires=IS_NOT_EMPTY())),
            TR("University",INPUT(_type="text",_name="univ",requires=IS_NOT_EMPTY())),
            TR("Started_On",INPUT(_type="string",_name="start_year",_class="date")),
            TR("Graduated_On",INPUT(_type="string",_name="end_year",_class="date"))),
                      INPUT(_type='submit',value='Submit'),_action=URL('update2'))
    Other_School_Degree4=FORM(TABLE(
            TR("Degree",INPUT(_type="text",_name="deg",requires=IS_NOT_EMPTY())),
            TR("Department",INPUT(_type="text",_name="dept",requires=IS_NOT_EMPTY())),
            TR("University",INPUT(_type="text",_name="univ",requires=IS_NOT_EMPTY())),
            TR("Started_On",INPUT(_type="string",_name="start_year",_class="date")),
            TR("Graduated_On",INPUT(_type="string",_name="end_year",_class="date"))),
                      INPUT(_type='submit',value='Submit'),_action=URL('update2'))
    return locals()

def insert():
    row=request.vars
    if db.alumni_basic_data(iitg_webmail_id=session.b)==None:
        db.alumni_basic_data.insert(iitg_webmail_id=session.b,name_title=row.title,
                                                                                name_first=row.first_name,name_last=row.last_name,
                                                                                alternate_email_id=row.email,phone_no=row.phno,
                                                                                dob=row.dob,curr_addr_line1=row.Current_Address_Line_1,
                                                                                curr_addr_line2=row.Current_Address_Line_2,curr_addr_city=row.Current_City,
                                                                                curr_addr_state=row.Current_State,curr_addr_country=row.Current_Country,
                                                                                curr_emp_role=row.Current_Emp_Role, curr_emp_comp=row.Current_Company,
                                                                                curr_emp_industry=row.Current_Industry,
                                                                                cur_emp_start=row.Current_Emp_Started_From)
        
    else:
        row2 = db(db.alumni_basic_data.iitg_webmail_id==session.b).update(name_title=row.title,
                                                                                name_first=row.first_name,name_last=row.last_name,
                                                                                alternate_email_id=row.email,phone_no=row.phno,
                                                                                dob=row.dob,curr_addr_line1=row.Current_Address_Line_1,
                                                                                curr_addr_line2=row.Current_Address_Line_2,curr_addr_city=row.Current_City,
                                                                                curr_addr_state=row.Current_State,curr_addr_country=row.Current_Country,
                                                                                curr_emp_role=row.Current_Emp_Role, curr_emp_comp=row.Current_Company,
                                                                                curr_emp_industry=row.Current_Industry,
                                                                                cur_emp_start=row.Current_Emp_Started_From)
    form6=FORM(INPUT(_type='submit',_value='Login'))
    return dict(form6=form6)

def update1():
    row=request.vars
    a1=0
    x = db(db.iitg_deg.iitg_webmail_id==session.b).select()
    for y in x:
        if(y.deg==row.deg):
            a1 = 10
    if a1!=10:
        session.flash='Invdadsdals'
        db.iitg_deg.insert(iitg_webmail_id=session.b,deg=row.deg,dept=row.dept,start_year=row.start_year,end_year=row.end_year)
    else:
        row2 = db(db.iitg_deg.iitg_webmail_id==session.b).select()
        """
           row2 = db(db.iitg_deg.iitg_webmail_id==session.b).update(dept=row.dept,start_year=row.start_year,end_year=row.end_year)
        """
        for rows in row2:
            if (rows.deg==row.deg):
                db((db.iitg_deg.iitg_webmail_id==session.b)&(db.iitg_deg.deg==row.deg)).update(dept=row.dept,start_year=row.start_year,end_year=row.end_year)
    
    form0=FORM(INPUT(_type='submit',_value='update1'))
    return dict(form0=form0)


def update2():
    row=request.vars
    a1=0
    x = db(db.othr_univ_degree.iitg_webmail_id==session.b).select()
    for y in x:
        if(y.deg==row.deg):
            a1 = 10
    if a1!=10:
        session.flash='Invdadsdals'
        db.othr_univ_degree.insert(iitg_webmail_id=session.b,deg=row.deg,dept=row.dept,univ=row.univ,start_year=row.start_year,end_year=row.end_year)
    else:
        row2 = db(db.othr_univ_degree.iitg_webmail_id==session.b).select()
        """
           row2 = db(db.iitg_deg.iitg_webmail_id==session.b).update(dept=row.dept,start_year=row.start_year,end_year=row.end_year)
        """
        for rows in row2:
            if (rows.deg==row.deg):
                db((db.othr_univ_degree.iitg_webmail_id==session.b)&(db.othr_univ_degree.deg==row.deg)).update(dept=row.dept,univ=row.univ,start_year=row.start_year,end_year=row.end_year)
    
    form0=FORM(INPUT(_type='submit',_value='update1'))
    return dict(form0=form0)

def alumni_search():
    Details = FORM(TABLE(TR("Search By",SELECT('name','place','university','firm',_name="search_by")),
                   TR("Search For:",INPUT(_type="text",_name="search",requires=IS_NOT_EMPTY()))),
                    TR("",INPUT(_type="submit",_value="Search")))
    if Details.accepts(request,session):
        response.flash="form accepted"
        session.x = Details.vars.search
        session.y= Details.vars.search_by
        if session.y=='name':
            redirect(URL('search_name'))
        if session.y=='place':
            redirect(URL('search_place'))
        if session.y=='university':
            redirect(URL('search_university'))
        if session.y=='firm':
            redirect(URL('search_firm'))
    elif Details.errors:
        response.flash="form is invalid"
    return locals()
def search_name():
    rows=db(db.alumni_basic_data.name_first==session.x).select(db.alumni_basic_data.ALL)
    return locals()
def search_place():
    rows=db(db.alumni_basic_data.curr_addr_city==session.x).select(db.alumni_basic_data.ALL)
    return locals()
def search_university():
    rows=db(db.othr_univ_degree.univ==session.x).select(db.othr_univ_degree.ALL)
    return locals()
def search_firm():
    rows=db(db.alumni_basic_data.curr_emp_industry==session.x).select(db.alumni_basic_data.ALL)
    return locals()
def show():
    post = db(db.alumni_basic_data.iitg_webmail_id==request.args(0)).select(db.alumni_basic_data.ALL)
    return locals()
def form():
    form=FORM(TABLE(TR("Your name:",INPUT(_type="text",_name="name",requires=IS_NOT_EMPTY())),
                    TR("Your email:",INPUT(_type="text",_name="email",requires=IS_EMAIL())),
                    TR("Admin",INPUT(_type="checkbox",_name="admin")),
                    TR("Sure?",SELECT('yes','no',_name="sure",requires=IS_IN_SET(['yes','no']))),
                    TR("Profile",TEXTAREA(_name="profile",value="write something here")),
                    TR("",INPUT(_type="submit",_value="SUBMIT"))))
    if form.accepts(request,session):
        response.flash="form accepted"
    elif form.errors:
        response.flash="form is invalid"
    else:
        response.flash="please fill the form"
    return dict(form=form,vars=form.vars)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    redirect(URL('index'))


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)

def prin():
    row2 = db(db.alumni_basic_data.iitg_webmail_id==session.b).select().first()
    return locals()
