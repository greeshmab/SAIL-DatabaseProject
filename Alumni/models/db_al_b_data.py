# -*- coding: utf-8 -*-
db.define_table('alumni_basic_data',Field('iitg_webmail_id','string'),
               Field('name_title','string'),
               Field('name_first','string'),
               Field('name_last','string'),
               Field('alternate_email_id','string'),
               Field('phone_no','string'),
               Field('dob','date'),
               Field('curr_addr_line1','string'),
               Field('curr_addr_line2','string'),
               Field('curr_addr_city','string'),
               Field('curr_addr_state','string'),
               Field('curr_addr_country','string'),
               Field('curr_emp_role','string'),
               Field('curr_emp_comp','string'),
               Field('curr_emp_industry','string'),
               Field('cur_emp_start','date'),
               primarykey=['iitg_webmail_id'])