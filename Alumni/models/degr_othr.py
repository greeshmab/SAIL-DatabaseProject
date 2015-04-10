# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
db.define_table('othr_univ_degree',Field('iitg_webmail_id','string'),
                Field('deg','string'),
                Field('dept','string'),
                Field('univ','string'),
                Field('start_year','date'),
                Field('end_year','date'),
                primarykey=['iitg_webmail_id','deg'])
