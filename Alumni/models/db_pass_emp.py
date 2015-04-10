# -*- coding: utf-8 -*-
db.define_table('past_employment',Field('iitg_webmail_id','string'),
                Field('emp_no','integer'),
                Field('role','string'),
                Field('company_name','string'),
                Field('city','string'),
                Field('industry','string'),
                Field('start_year','date'),
                Field('end_year','date'),
                primarykey=['iitg_webmail_id','emp_no'])
