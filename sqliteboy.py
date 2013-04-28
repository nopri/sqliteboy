#!/usr/bin/env python
#
#
# sqliteboy.py
# Simple Web SQLite Manager/Form/Report Application
# (c) Noprianto <nop@tedut.com>
# 2012-2013
# GPL
#
# Please read README.rst
#
# I apologize for:
# - the lack of documentation in source code
# - obsolete codes
# - non-descriptive variable/function names
# - using python builtins as variable (input, type, ...) :(
# - PEP8 violations :)
#
# # pyinstaller 2.0 spec #
# # python <path/to/pyinstaller.py> <spec>
#
#    a = Analysis(['sqliteboy.py'])
#
#    a.datas += [
#                ('sqliteboy.py', 'sqliteboy.py', 'DATA'),
#                ('README.rst', 'README.rst', 'DATA'),
#            ]
#
#    pyz = PYZ(a.pure)
#
#    exe = EXE(
#                pyz, 
#                a.scripts, 
#                a.binaries, 
#                a.datas, 
#                name="sqliteboy.exe",
#                icon="favicon.ico",
#                console=True,
#                debug=False
#            )
#

#----------------------------------------------------------------------#
# APPLICATION                                                          #
#----------------------------------------------------------------------#
NAME = 'sqliteboy'
APP_DESC = 'Simple Web SQLite Manager/Form/Report Application'
VERSION = '0.41'
WSITE = 'https://github.com/nopri/%s' %(NAME)
TITLE = NAME + ' ' + VERSION
DBN = 'sqlite'
CHECK_SAME_THREAD=False
FORM_TBL = '_sqliteboy_'
FORM_URL_INIT = '/sqliteboy/init'
FORM_FIELDS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
FORM_FIELD_TYPE = 'text'
FORM_SPLIT = '.'
FORM_VALID = None
PRECISION = 4
SORT = ('asc', 'desc')
VSORT = ('&#9650;', '&#9660;')
ROWID = 'ROWID'
DEFAULT_PORT = 11738
DEFAULT_ADDR = '0.0.0.0'
DEFAULT_LANG = 'default'
DEFAULT_TABLE = 'sqlite_master'
DEFAULT_LIMIT = 50
DEFAULT_T_BASE = '%s.html' %(NAME)
DEFAULT_ADMIN_USER = 'admin'
DEFAULT_ADMIN_PASSWORD = DEFAULT_ADMIN_USER
DEFAULT_HOSTS_ALLOWED = ['127.0.0.1']
DEFAULT_TEXTAREA_COLS = 40
DEFAULT_TEXTAREA_ROWS = 15
HOST_LOCAL = '0'
HOST_ALL = '1'
HOST_CUSTOM = '2'
DFLT_VALUE = 'dflt_value'
MARK_CURRENT = '&#9658' #unused
NAME_SELECT = 'select'
EXCLUDE_TABLE = []
SIZE_KB = 1024
SIZE_MB = 1024 * SIZE_KB
SIZE_GB = 1024 * SIZE_MB
BLOB_TYPE = ['blob']
TEXT_TYPE = ['text', 'clob']
NOQUOTE_TYPE = ['integer', 'real']
BLOB_VAR = 'rowid'
BLOB_COLUMN = 'column'
BLOB_CTYPE = 'application/octet-stream'
MODE_INSERT = 'insert'
SKT_ROWID = 'rowid'
SKT_M_INSERT = 'insert'
SKT_M_EDIT = 'edit'
SKT_P_EDIT = 'position'
SKT_M_COLUMN = 'column'
SKT_M_RENAME = 'rename'
SKT_M_DROP = 'drop'
SKQ = 'query'
SK_CREATE = 'create'
SK_LOGIN = 'login'
SK_PASSWORD = 'password'
SK_NOTES = 'notes'
SK_USERS = 'users'
SK_HOSTS = 'hosts'
SKF_CREATE = 'form.create'
SKF_RUN = 'form.run'
SKR_CREATE = 'report.create'
SKR_RUN = 'report.run'
COLUMN_TYPES = (
                ('integer primary key', 0),
                ('integer primary key autoincrement', 0),
                ('integer', 1),
                ('real', 1),
                ('char', 1),
                ('varchar', 1),
                ('text', 1),
                ('blob', 1),
                ('null', 1),
            ) #type, used in add column
MAX_COLUMN_ADD = 3
CUSTOM_RT = {
                'query': 4,
            } #command, rt 
PK_SYM = '*'
URL_README = ('/sqliteboy/readme', 'sqliteboy_readme', 'README.rst')
URL_SOURCE = ('/sqliteboy/source', 'sqliteboy_source', 'sqliteboy.py')
PROTECTED_USERS = ['admin']
FORM_ALL = ''
FORM_KEY_TITLE = 'title'
FORM_KEY_INFO = 'info'
FORM_KEY_DATA = 'data'
FORM_KEY_DATA_TABLE = 'table'
FORM_KEY_DATA_COLUMN = 'column'
FORM_KEY_DATA_LABEL = 'label'
FORM_KEY_DATA_REFERENCE = 'reference'
FORM_KEY_DATA_DEFAULT = 'default'
FORM_KEY_DATA_REQUIRED = 'required'
FORM_KEY_DATA_READONLY = 'readonly'
FORM_KEY_DATA_CONSTRAINT = 'constraint'
FORM_KEY_SECURITY = 'security'
FORM_KEY_SECURITY_RUN = 'run'
FORM_KEY_DATA_ONSAVE = 'onsave'
FORM_KEY_SUB = 'sub'
FORM_KEY_MESSAGE = 'message'
FORM_KEY_SQL2 = 'sql2'
FORM_REQ = (FORM_KEY_DATA,)
FORM_REQ_DATA = (FORM_KEY_DATA_TABLE, 
                    FORM_KEY_DATA_COLUMN,
                )
FORM_REFERENCE_SQL_0 = 'a'
FORM_REFERENCE_SQL_1 = 'b'
FORM_ONSAVE_SQL_VALUE = 'value'
FORM_ONSAVE_SQL_RET = 'onsave'
FORM_SUB_ROWS_DEFAULT = [5, 1]#rows, required rows
FORM_MESSAGE_LEN = 3
FORM_MESSAGE_VAR_RESULT = '$result'
#
REPORT_KEY_DATA_TYPES = ['integer']
REPORT_ALL = FORM_ALL
REPORT_KEY_TITLE = FORM_KEY_TITLE
REPORT_KEY_INFO = FORM_KEY_INFO
REPORT_KEY_DATA = FORM_KEY_DATA
REPORT_KEY_DATA_KEY = 'key'
REPORT_KEY_DATA_LABEL = FORM_KEY_DATA_LABEL
REPORT_KEY_DATA_REFERENCE = FORM_KEY_DATA_REFERENCE
REPORT_KEY_DATA_DEFAULT = FORM_KEY_DATA_DEFAULT
REPORT_KEY_DATA_REQUIRED = FORM_KEY_DATA_REQUIRED
REPORT_KEY_DATA_READONLY = FORM_KEY_DATA_READONLY
REPORT_KEY_DATA_CONSTRAINT = FORM_KEY_DATA_CONSTRAINT
REPORT_KEY_DATA_TYPE = 'type'
REPORT_KEY_MESSAGE = 'message'
REPORT_KEY_SECURITY = FORM_KEY_SECURITY
REPORT_KEY_SECURITY_RUN = FORM_KEY_SECURITY_RUN
REPORT_KEY_SQL = 'sql'
REPORT_KEY_HEADER = 'header'
REPORT_REQ = (REPORT_KEY_DATA,
                REPORT_KEY_SQL,
            )
REPORT_REQ_DATA = (REPORT_KEY_DATA_KEY,)
REPORT_REFERENCE_SQL_0 = 'a'
REPORT_REFERENCE_SQL_1 = 'b'
REPORT_MESSAGE_LEN = 3
REPORT_MESSAGE_VAR_RESULT = '$result'
FAVICON_WIDTH = 16
FAVICON_HEIGHT = 16
PYTIME_FORMAT = '%Y-%m-%d %H:%M:%S'
PYTIME_FORMAT_BACKUP = '%Y-%m-%d_%H-%M-%S'
REGEX_EMAIL = r'^[\w\.\+-]+@[\w\.-]+\.[a-zA-Z]+$'
DAYS_IN_YEAR = 365.2425
CSV_SUFFIX = '.csv'
CSV_CTYPE = 'text/csv'
BACKUP_BUFFER = 10 * SIZE_KB


#----------------------------------------------------------------------#
# MODULE                                                               #
#----------------------------------------------------------------------#
import sys
import os
if getattr(sys, 'frozen', None):
    CURDIR = sys._MEIPASS
    CWDIR = os.getcwd()
else:
    CURDIR = os.path.dirname(__file__)
    CWDIR = CURDIR

import time
import decimal
import random
import string
FORM_VALID = [x for x in string.ascii_lowercase] + [x for x in string.digits]
FORM_VALID.append('_')

import socket
DEFAULT_HOSTS_ALLOWED.append(socket.gethostbyname(socket.gethostname()))

try: 
   from hashlib import md5
except ImportError:
   from md5 import md5

import json
import urllib
import hashlib
import base64

import platform
import struct
import sqlite3

import re

import csv
import cStringIO

import web
web.config.debug = False


#----------------------------------------------------------------------#
# WEB                                                                  #
#----------------------------------------------------------------------#
URLS = (
    '/', 'index',
    '/favicon.ico', 'favicon_ico',
    '/table/action', 'table_action',
    '/table/browse/(.*)', 'table_browse',
    '/table/column', 'table_column',
    '/table/rename', 'table_rename',
    '/table/drop', 'table_drop',
    '/table/csv', 'table_csv',
    '/table/create', 'table_create',
    '/query', 'query',
    '/table/row/(.*)', 'table_row',
    '/table/blob/(.*)', 'table_blob',
    '/table/save', 'table_save',
    FORM_URL_INIT, 'sqliteboy_init',
    URL_README[0], URL_README[1],
    URL_SOURCE[0], URL_SOURCE[1],
    '/login', 'login',
    '/logout', 'logout',
    '/password', 'password',
    '/admin/users', 'admin_users',
    '/admin/hosts', 'admin_hosts',
    '/admin/backup', 'admin_backup',
    '/form/action', 'form_action',
    '/form/run/(.*)', 'form_run',
    '/form/edit', 'form_edit',
    '/report/action', 'report_action',
    '/report/run/(.*)', 'report_run',
    '/report/edit', 'report_edit',
    '/notes', 'notes',
    )

app = None
db = None
dbfile = ''
dbfile0 = ''
rendertime = [0, 0]
rowid = '_%s___%s___%s___%s_' %(
        NAME, 
        ROWID, 
        random.randrange(0, 999999999),
        int(time.time()),
        )

#
sess = None
sess_init = {
        'table': {},
        'user': '',
        'admin': 0,
    }


#----------------------------------------------------------------------#
# MEMSESSION                                                           #
#----------------------------------------------------------------------#
class MemSession(web.session.Store):
    data = {}
    def __init__(self):
        self.data = {}
    
    def __contains__(self, key):
        return self.data.has_key(key)
    
    def __getitem__(self, key):
        if not self.data.has_key(key):
            raise KeyError, key
        #
        v = self.data[key]
        v[0] = time.time()
        self.data[key] = v
        return v[1]
    
    def __setitem__(self, key, value):
        v = [time.time(), value]
        self.data[key] = v
        
    def __delitem__(self, key):
        if self.data.has_key(key):
            del self.data[key]
            
    def cleanup(self, timeout):
        kdel = []
        now = time.time()
        #
        for k in self.data.keys():
            v = self.data[k]
            if now - v[0] > timeout:
                kdel.append(k)
        #
        for k in kdel:
            if self.data.has_key(k):
                del self.data[k]
        

#----------------------------------------------------------------------#
# LANG                                                                 #
#----------------------------------------------------------------------#
LANGS = {
    'default': 
        {
            'usage': '<database_file> [port]',
            'pf_b' : 'B',
            'pf_kb': 'KB',
            'pf_mb': 'MB',
            'pf_gb': 'GB',
            'a_local': 'local',
            'a_all': 'all',
            'a_custom': 'custom',
            'x_welcome': 'welcome',
            'x_welcome2': 'welcome to',
            'x_allow': 'allow',
            'x_table': 'table',
            'x_second': 'second(s)',
            'x_row' : 'row(s)',
            'x_limit': 'limit',
            'x_default': 'default',
            'x_name': 'name',
            'x_type': 'type',
            'x_primary_key': 'primary key',
            'x_optional': 'optional',
            'x_rename': 'rename to',
            'x_empty': 'empty',
            'x_column_number': 'number of column',
            'x_table_name': 'table name',
            'x_yes': 'yes',
            'x_no': 'no',
            'x_enabled': 'enabled',
            'x_required': 'required',
            'x_not_enabled': 'not enabled',
            'x_version': 'version',
            'x_sqlite_version': 'SQLite version',
            'x_web_version': 'web.py version',
            'x_python_version': 'Python version',
            'x_extended_features': 'extended features',
            'x_user': 'user',
            'x_delete': 'delete',
            'x_password': 'password',
            'x_admin': 'admin',
            'x_note': 'note',
            'x_password_old': 'old password',
            'x_password_new': 'new password',
            'x_password_new_repeat': 'repeat new password',
            'x_added': 'added',
            'x_deleted': 'deleted',
            'x_password_changed': 'password changed',
            'x_admin_changed': 'admin changed',
            'x_not_applicable': 'not applicable',
            'x_form': 'form',
            'x_code': 'code',
            'x_form_name': 'form name',
            'x_report': 'report',
            'x_report_name': 'report name',
            'x_title': 'title',
            'x_content': 'content',
            'x_action': 'action',
            'tt_insert': 'insert',
            'tt_edit': 'edit',
            'tt_column': 'column',
            'tt_rename': 'rename',
            'tt_drop': 'drop',
            'tt_query': 'query',
            'tt_create': 'create',
            'tt_readme': 'readme',
            'tt_source': 'source',
            'tt_login': 'login',
            'tt_password': 'password',
            'tt_users': 'users',
            'tt_hosts': 'hosts',
            'tt_form_run': 'form run',
            'tt_form_edit': 'form edit',
            'tt_form_create': 'form create',
            'tt_report_run': 'report run',
            'tt_report_edit': 'report edit',
            'tt_report_create': 'report create',
            'tt_report_run_result': 'report run (result)',
            'tt_notes': 'notes',
            'th_error': 'ERROR',
            'th_ok': 'OK',
            'cmd_browse': 'browse',
            'cmd_insert': 'insert',
            'cmd_column': 'column',
            'cmd_rename': 'rename',
            'cmd_table_drop': 'drop',
            'cmd_export_csv': 'csv',
            'cmd_table_create': 'create',
            'cmd_query': 'query',
            'cmd_query_src': 'query',
            'cmd_delete_selected': 'delete selected',
            'cmd_edit_selected': 'edit selected',
            'cmd_download': 'download',
            'cmd_edit': 'edit',
            'cmd_add': 'add',
            'cmd_next': 'next',
            'cmd_enable_sqliteboy': 'create %s table and enable extended features' %(FORM_TBL),
            'cmd_readme': 'readme',
            'cmd_source': 'source',
            'cmd_login': 'login',
            'cmd_logout': 'logout',
            'cmd_password': 'password',
            'cmd_notes': 'notes',
            'cmd_users': 'users',
            'cmd_hosts': 'hosts',
            'cmd_backup': 'backup',
            'cmd_save': 'save',
            'cmd_run': 'run',
            'cmd_form_create': 'create',
            'cmd_report_create': 'create',
            'cmd_report': 'go',
            'cf_delete_selected': 'are you sure you want to delete selected row(s)?',
            'cf_drop': 'confirm drop table',
            'e_access_forbidden': 'access forbidden',
            'e_connect': 'ERROR: unable to connect to',
            'e_insert': 'ERROR: insert into table',
            'e_edit': 'ERROR: update table',
            'e_rename': 'ERROR: alter table (rename)',
            'e_drop': 'ERROR: drop table',
            'e_table_exists': 'ERROR: table already exists',
            'e_open_file': 'ERROR: open file',
            'e_login': 'ERROR: unknown user or incorrect password',
            'e_password_general': 'ERROR: could not change password',
            'e_password_auth': 'ERROR: authentication failed',
            'e_password_mismatch': 'ERROR: passwords mismatch',
            'e_password_blank': 'ERROR: please enter new password',
            'e_hosts': 'ERROR: could not update hosts',
            'e_form_edit_whitespace': 'ERROR: could not handle form with whitespace in name',
            'e_form_edit_exists': 'ERROR: form already exists',
            'e_form_edit_syntax' : 'ERROR: form code error',
            'e_form_edit_name': 'ERROR: invalid form name',
            'e_form_run_syntax_or_required': 'ERROR: form code error or required keys are not set',
            'e_form_run_required': 'ERROR: required',
            'e_form_run_constraint': 'ERROR: constraint',
            'e_form_run_onsave': 'ERROR: onsave',
            'e_form_run_subform': 'ERROR: subform',
            'e_form_insert_general': 'ERROR: processing form',
            'e_report_edit_whitespace': 'ERROR: could not handle report with whitespace in name',
            'e_report_edit_exists': 'ERROR: report already exists',
            'e_report_edit_syntax' : 'ERROR: report code error',
            'e_report_edit_name': 'ERROR: invalid report name',
            'e_report_run_syntax_or_required': 'ERROR: report code error or required keys are not set',
            'e_report_run_required': 'ERROR: required',
            'e_report_run_constraint': 'ERROR: constraint',
            'e_report_select_general': 'ERROR: processing report',
            'o_insert': 'OK: insert into table',
            'o_edit': 'OK: update table',
            'o_column': 'OK: alter table (column)',
            'o_rename': 'OK: alter table (rename)',
            'o_password': 'OK: password changed',
            'o_hosts': 'OK: hosts updated',
            'o_form_run': 'OK: data saved',
            'o_notes': 'OK: notes updated',
            'h_insert': 'hint: leave blank to use default value (if any)',
            'h_edit': 'hint: for blob field, leave blank = do not update',
            'h_column': 'hint: only add column is supported in SQLite. Primary key/unique is not allowed in column addition. Default value(s) must be constant.',
            'h_rename': '',
            'h_drop': '',
            'h_query': 'hint: only one statement at a time is supported',
            'h_create': 'hint: please do not put whitespace in table name',
            'h_create2': 'hint: for multiple primary keys, do not select type contains "primary key", use primary key column instead. For date/time type, please use integer. If date/time default is needed, please use current_time, current_date or current_timestamp. To use non-constant literally, please surround with quote(\'), for example \'current_time\'.',
            'h_users': 'hint: only valid value(s) will be updated. You could not delete yourself or update your admin level. New username must be unique, must not contain whitespace and will be lowercased.',
            'h_hosts': 'hint: for custom hosts, please use whitespace separated format',
            'h_form_create': 'hint: please do not put whitespace in form name. Form name must be alphanumeric/underscore and will be converted to lowercase. Form code in JSON format. Please read <a href="%s">README</a> for form code reference.' %(URL_README[0]),
            'h_form_run': '',
            'h_report_create': 'hint: please do not put whitespace in report name. Report name must be alphanumeric/underscore and will be converted to lowercase. Report code in JSON format. Please read <a href="%s">README</a> for report code reference.' %(URL_README[0]),
            'h_report_run': '',
            'h_notes': '',
            'z_table_whitespace': 'could not handle table with whitespace in name',
            'z_view_blob': '[blob, please use browse menu if applicable]',
        },
    }

def res(all, type, default=DEFAULT_LANG):
    if not all.has_key(type): 
        return all[default]
    #
    ret = all[type]
    for k in all[default].keys():
        if not ret.has_key(k):
            ret[k] = all[default][k]
    #
    return ret

_ = res(LANGS, DEFAULT_LANG)


#----------------------------------------------------------------------#
# SQLITE UDF                                                           #
#----------------------------------------------------------------------#
SQLITE_UDF = []

def sqliteboy_strs(s):
    vt = [type(''), type(u'')]
    if not type(s) in vt:
        s = str(s)
    #
    return s
SQLITE_UDF.append(('sqliteboy_strs', 1, sqliteboy_strs))

def sqliteboy_as_integer(s):
    ret = 0
    #
    try:
        ret = int(s)
    except:
        pass
    #
    return ret
SQLITE_UDF.append(('sqliteboy_as_integer', 1, sqliteboy_as_integer))

def sqliteboy_as_float(s):
    ret = 0
    #
    try:
        ret = float(s)
    except:
        pass
    #
    return ret
SQLITE_UDF.append(('sqliteboy_as_float', 1, sqliteboy_as_float))

def sqliteboy_len(s):
    return len(str(s))
SQLITE_UDF.append(('sqliteboy_len', 1, sqliteboy_len))

def sqliteboy_md5(s):
    return md5(str(s)).hexdigest()
SQLITE_UDF.append(('sqliteboy_md5', 1, sqliteboy_md5))

def sqliteboy_sha1(s):
    return hashlib.sha1(str(s)).hexdigest()
SQLITE_UDF.append(('sqliteboy_sha1', 1, sqliteboy_sha1))

def sqliteboy_sha224(s):
    return hashlib.sha224(str(s)).hexdigest()
SQLITE_UDF.append(('sqliteboy_sha224', 1, sqliteboy_sha224))

def sqliteboy_sha256(s):
    return hashlib.sha256(str(s)).hexdigest()
SQLITE_UDF.append(('sqliteboy_sha256', 1, sqliteboy_sha256))

def sqliteboy_sha384(s):
    return hashlib.sha384(str(s)).hexdigest()
SQLITE_UDF.append(('sqliteboy_sha384', 1, sqliteboy_sha384))

def sqliteboy_sha512(s):
    return hashlib.sha512(str(s)).hexdigest()
SQLITE_UDF.append(('sqliteboy_sha512', 1, sqliteboy_sha512))

def sqliteboy_b64encode(s):
    return base64.b64encode(str(s))
SQLITE_UDF.append(('sqliteboy_b64encode', 1, sqliteboy_b64encode))

def sqliteboy_b64decode(s):
    return base64.b64decode(str(s))
SQLITE_UDF.append(('sqliteboy_b64decode', 1, sqliteboy_b64decode))

def sqliteboy_randrange(a, b):
    vt = [type(1), type(1L)]
    if not type(a) in vt or not type(b) in vt: return 0
    if a == b: return a
    #
    return random.randrange(a, b)
SQLITE_UDF.append(('sqliteboy_randrange', 2, sqliteboy_randrange))

def sqliteboy_time():
    return time.time()
SQLITE_UDF.append(('sqliteboy_time', 0, sqliteboy_time))

def sqliteboy_time2(s):
    try:
        s = s.strip()
        return time.mktime(time.strptime(s, PYTIME_FORMAT))
    except:
        return 0
SQLITE_UDF.append(('sqliteboy_time2', 1, sqliteboy_time2))

def sqliteboy_time3(f):
    try:
        return time.strftime(PYTIME_FORMAT, time.localtime(f))
    except:
        return ''
SQLITE_UDF.append(('sqliteboy_time3', 1, sqliteboy_time3))

def sqliteboy_time4(f):
    try:
        return time.strftime(PYTIME_FORMAT, time.gmtime(f))
    except:
        return ''
SQLITE_UDF.append(('sqliteboy_time4', 1, sqliteboy_time4))

def sqliteboy_time5(s1, s2, mode):
    s1 = str(s1)
    s2 = str(s2)
    if not sqliteboy_is_integer(mode):
        mode = 0
    #
    tnow = sqliteboy_time()
    if not s1.strip():
        s1 = sqliteboy_time3(tnow)
    if not s2.strip():
        s2 = sqliteboy_time3(tnow)
    #
    t1 = sqliteboy_time2(s1)
    t2 = sqliteboy_time2(s2)
    #
    d = t2 - t1
    d = float(d)
    #
    ret = 0
    #
    if mode == 1: #second
        ret = d
    elif mode == 2: #minute
        ret = d / (60)
    elif mode == 3: #hour
        ret = d / (60 * 60)
    elif mode == 4: #day
        ret = d / (60 * 60 * 24)
    elif mode == 5: #year
        ret = d / (60 * 60 * 24 * DAYS_IN_YEAR)
    #
    return ret
SQLITE_UDF.append(('sqliteboy_time5', 3, sqliteboy_time5)) 

def sqliteboy_lower(s):
    s = sqliteboy_strs(s)
    return s.lower()
SQLITE_UDF.append(('sqliteboy_lower', 1, sqliteboy_lower))

def sqliteboy_upper(s):
    s = sqliteboy_strs(s)
    return s.upper()
SQLITE_UDF.append(('sqliteboy_upper', 1, sqliteboy_upper))

def sqliteboy_is_valid_email(s):
    s = sqliteboy_strs(s)
    #
    if re.match(REGEX_EMAIL, s):
        return int(True)
    #
    return int(False)
SQLITE_UDF.append(('sqliteboy_is_valid_email', 1, sqliteboy_is_valid_email))

def sqliteboy_match(s1, s2):
    s1 = sqliteboy_strs(s1)
    s2 = sqliteboy_strs(s2)
    #
    if re.match(s1, s2):
        return int(True)
    #
    return int(False)
SQLITE_UDF.append(('sqliteboy_match', 2, sqliteboy_match))

def sqliteboy_is_number(n):
    if isinstance(n, (float, int, long)):
        return int(True)
    #
    try:
        test = float(n)
    except:
        pass
    else:
        return int(True)
    #
    try:
        test = long(n)
    except:
        pass
    else:
        return int(True)
    #
    try:
        test = int(n)
    except:
        pass
    else:
        return int(True)
    #
    return int(False)
SQLITE_UDF.append(('sqliteboy_is_number', 1, sqliteboy_is_number))

def sqliteboy_is_float(n):
    if isinstance(n, float):
        return int(True)
    #
    return int(False)
SQLITE_UDF.append(('sqliteboy_is_float', 1, sqliteboy_is_float))

def sqliteboy_is_integer(n):
    if isinstance(n, int):
        return int(True)
    #
    return int(False)
SQLITE_UDF.append(('sqliteboy_is_integer', 1, sqliteboy_is_integer))

def sqliteboy_normalize_separator(s, separator, remove_space, unique):
    field = sqliteboy_strs(s)
    #
    strs = field.strip()
    splitted = strs.split(separator)
    splitted2 = [x.strip() for x in splitted]
    if remove_space:
        splitted3 = [x.replace(' ', '') for x in splitted2]
    else:
        splitted3 = splitted2
    
    if unique:
        splitted4 = []
        for i in splitted3:
            if i not in splitted4:
                splitted4.append(i)
    else:
        splitte4 = splitted3

    #
    splitted5 = splitted4
        
    newlist = []
    for part in splitted5:
        if part:
            newlist.append(part)
    #
    ret = separator.join(newlist)
    #
    return ret
SQLITE_UDF.append(('sqliteboy_normalize_separator', 4, sqliteboy_normalize_separator))

def sqliteboy_chunk(s, n, separator, justify, padding):
    s = str(s)
    separator = str(separator)
    padding = str(padding)
    #
    if (not n) or (not s) or (n < 1):
        return s
    #
    if padding: 
        pad = padding[0]
    else:
        pad = ' '
    #
    if not justify:
        justify = 0
    #
    mod = len(s) % n
    if mod:
        ln = len(s) + (n - mod)
        if justify == 0: #left
            s = s.ljust(ln, pad)
        else: #right
            s = s.rjust(ln, pad)
    #
    res = [s[i:i+n] for i in range(0, len(s), n)]
    ret = separator.join(res)
    #
    return ret
SQLITE_UDF.append(('sqliteboy_chunk', 5, sqliteboy_chunk))

def sqliteboy_number_format(n, decimals, decimal_point, thousands_separator):
    n = str(n)
    decimal_point = str(decimal_point)
    thousands_sep = str(thousands_separator)
    #
    neg = False
    try:
        f = float(n)
        if f < 0:
            neg = True
    except:
        return n
    #
    if 'e' in n.lower():
        efmt = '%%.%sf' %len(n)
        n = efmt %float(n)
    #
    dec = decimals
    if not sqliteboy_is_integer(dec) or dec < 0:
        dec = 0
    #
    nn = ''
    dd = ''
    if '.' in n: #float
        nn, dd = n.split('.')
    else:
        nn = n
    nn = nn.replace('-', '')
    nn = nn.replace('+', '')
    nn = nn.strip()
    dd = dd.strip()
    #
    if dd:
        if dec <= len(dd):
            dd = dd[:dec]
        else:
            dd = dd.ljust(dec, '0')
    #
    nn = sqliteboy_chunk(nn, 3, thousands_sep, 1, '').strip()
    dd = dd.strip()
    #
    if neg:
        nn = '-' + nn
    #
    if dd:
        ret = nn + decimal_point + dd
    else:
        ret = nn
    #
    return ret
SQLITE_UDF.append(('sqliteboy_number_format', 4, sqliteboy_number_format))

def sqliteboy_lookup2(table, field, field1, value1, order, default):
    table = str(table)
    field = str(field)
    field1 = str(field1)
    if not sqliteboy_is_number(order) or order < 0:
        order = 0
    #
    if not table in tables():
        return default
    cols = columns(table, True)
    if not field1 in cols or not field in cols:
        return default
    #
    sorder = ' rowid asc'
    if order > 0:
        sorder = ' rowid desc'
    #
    ret = default
    #
    where = [
            '%s=$%s' %(field1, field1), 
            ]
    var = {field1: value1}
    #
    try:
        r = db.select(
            table, 
            where=' and '.join(where),
            order=sorder, 
            vars=var).list()
        r = r[0]
        ret = r[field]
    except:
        pass
    #
    return ret
SQLITE_UDF.append(('sqliteboy_lookup2', 6, sqliteboy_lookup2))
    
def sqliteboy_lookup3(table, field, field1, value1, field2, value2, order, default):
    table = str(table)
    field = str(field)
    field1 = str(field1)
    field2 = str(field2)
    if not sqliteboy_is_number(order) or order < 0:
        order = 0
    #
    if not table in tables():
        return default
    cols = columns(table, True)
    if not field1 in cols or not field2 in cols or not field in cols:
        return default
    #
    sorder = ' rowid asc'
    if order > 0:
        sorder = ' rowid desc'
    #
    ret = default
    #
    where = [
            '%s=$%s' %(field1, field1), 
            '%s=$%s' %(field2, field2),
            ]
    var = {field1: value1, field2: value2}
    #
    try:
        r = db.select(
            table, 
            where=' and '.join(where),
            order=sorder, 
            vars=var).list()
        r = r[0]
        ret = r[field]
    except:
        pass
    #
    return ret
SQLITE_UDF.append(('sqliteboy_lookup3', 8, sqliteboy_lookup3))


#----------------------------------------------------------------------#
# FUNCTION                                                             #
#----------------------------------------------------------------------#
def get_value1(values, default):
    ret = default
    #
    if not values:
        values = ()
    #
    for i in values:
        if i:
            ret = i
            break
    #
    return ret

def gen_d(exclude, a=0, b=999999, separator='-', retry=1000):
    if not exclude:
        exclude = ()
    #
    ret = None
    #
    i = 0
    while True:
        i = i+1
        #
        t = long(time.time())
        r = random.randrange(a, b)
        x = '%s%s%s' %(str(t), separator, str(r))
        if not x in exclude:
            ret = x
            break
        #
        if i > retry:
            break
    #
    return ret

def isstr(s, empty_ok=False):
    ret = False
    #
    if hasattr(s, 'strip'):
        ret = True
        if empty_ok == False:
            if s.strip():
                ret = True
            else:
                ret = False
    #
    return ret

def isadmin():
    try:
        return sess.admin == 1
    except:
        pass
    return False

def s_select(p):
    pr = p.split(FORM_SPLIT)
    st = []
    sd = {}
    for i in range(len(pr)):
        fi = FORM_FIELDS[i]
        s = '%s=$%s' %(fi, fi)
        if pr[i]:
            pri = pr[i]
            sd[fi] = pri
            st.append(s)
    #
    r = db.select(FORM_TBL, where = ' and '.join(st), vars=sd)
    ret = []
    for i in r:
        d = {}
        for k in i.keys(): d[k] = i[k]
        ret.append(d)
    #
    return ret

def canform(key, form, obj='form.code..'):
    ret = False
    #
    if isadmin(): 
        ret = True
    else:
        try:
            fo = s_select('%s%s' %(obj, form))
            fo = fo[0]
            fe = json.loads(fo['e'])
            if fe.has_key(FORM_KEY_SECURITY):
                fes = fe[FORM_KEY_SECURITY]
                if fes.has_key(key):
                    fesr = fes[key]
                    if fesr == FORM_ALL:
                        ret = True
                    else:
                        if sess.user in fesr:
                            ret = True
        except:
            pass
    #
    return ret
    
def canreport(key, report):
    return canform(key, report, 'report.code..')

def proc_access(handle):
    allowed = DEFAULT_HOSTS_ALLOWED
    ip = web.ctx.ip
    #
    if isnosb():
        if ip in allowed:
            return handle()
    else:
        saved = s_select('security.hosts')
        if not saved: 
            db.insert(FORM_TBL, a='security', b='hosts', d=HOST_LOCAL, e=json.dumps([]))
        #
        saved = s_select('security.hosts')
        saved = saved[0]
        #
        if saved['d'] == HOST_ALL: 
            return handle()
        else:
            if saved['d'] == HOST_CUSTOM:
                try:
                    add = saved['e']
                    addh = json.loads(add)
                    allowed = allowed + addh
                except:
                    pass
            #
            if ip in allowed:
                return handle()
    #
    return _['e_access_forbidden']

def proc_admin_check(handle):
    path = web.ctx.fullpath.lower()
    if not isnosb():
        if not sess.admin == 1:
            if path.startswith('/query') or path.startswith('/table') or path.startswith('/admin') or path.startswith('/form/edit') or path.startswith('/report/edit'):
                if sess.user:
                    return _['e_access_forbidden']
                else:
                    raise web.seeother('/login')
    #
    return handle()

def proc_login(handle):
    path = web.ctx.fullpath.lower()
    #
    if not isnosb():
        if not sess.user:
            if path == '/favicon.ico': return handle()
            if not path == '/login':
                raise web.seeother('/login')
        else:
            if path == '/login':
                raise web.seeother('/')
    #
    return handle()

def proc_nosb(handle):
    path = web.ctx.fullpath.lower()
    if isnosb():
        if path.startswith('/login') or  \
            path.startswith('/logout') or \
            path.startswith('/password') or \
            path.startswith('/form') or \
            path.startswith('/report') or \
            path.startswith('/notes') or \
            path.startswith('/admin'):
                raise web.seeother('/')
    #
    return handle()

def proc_udf(handle):
    for f in SQLITE_UDF:
        db._db_cursor().connection.create_function(f[0], f[1], f[2])
    #
    return handle()

def proc_misc(handle):
    return handle()

def allows():
    ret = ''
    hosts = {
                HOST_LOCAL: _['a_local'],
                HOST_ALL: _['a_all'],
                HOST_CUSTOM: _['a_custom'],
        }
    if isnosb():
        ret = hosts[HOST_LOCAL]
    else:
        saved = s_select('security.hosts')
        if not saved: 
            return ret
        #
        try:
            saved = saved[0]['d']
            ret = hosts[saved]
        except:
            pass
    #
    return ret

def start():
    rendertime[0] = time.time()

def stop():
    rendertime[1] = time.time()

def notfound():
    raise web.seeother('/')

def dflt():
    notfound()

def nrfloat(snumber, precision=PRECISION, round=decimal.ROUND_UP):
    le = '0' * precision
    if not le:
        dec = '1'
    else:
        dec = '.' + le
    #
    num = str(snumber)
    try:
        d = decimal.Decimal(num)
        ret = d.quantize(decimal.Decimal(dec), rounding=round)
    except:
        ret = None
    #
    return ret

def rt():
    x = rendertime[1] - rendertime[0]
    return '%s %s' %(nrfloat(x), _['x_second'])

def ssort(sort):
    ret = ''
    if not sort in SORT: return ret
    #
    index = SORT.index(sort)
    if index == 0:
        index = 1
    else:
        index = 0
    return SORT[index]
    
def vsort(sort):
    ret = ''
    if not sort in SORT: return ret
    #
    index = SORT.index(sort)
    #
    return VSORT[index]

def log(msg, newline=1, stream=sys.stdout):
    try:
        newline = int(newline)
    except ValueError:
        newline = 0
    #
    end = os.linesep * newline
    #
    if not stream in [sys.stdout, sys.stderr]:
        return 
    #
    stream.write('%s%s' %(msg, end) )

def title(t, link='/'):
    ret = ''
    if not link:
        ret = '[%s] [%s] %s' %(TITLE, dbfile0, t.strip())
    else:
        ret = '<a href="%s">[%s]</a> [%s] %s' %(link, TITLE, dbfile0, t.strip())
    return ret

def link(href, label):
    return '<a href="%s">%s</a>' %(href, label)
    
def size():
    s = os.path.getsize(dbfile)
    s = float(s)
    s2 = 0
    #
    if s >= SIZE_GB:
        s2 = str(nrfloat(s/SIZE_GB)) + ' ' + _['pf_gb']
    elif s >= SIZE_MB:
        s2 = str(nrfloat(s/SIZE_MB)) + ' ' + _['pf_mb']
    elif s >= SIZE_KB:
        s2 = str(nrfloat(s/SIZE_KB)) + ' ' + _['pf_kb']
    else:
        s2 = str(nrfloat(s)) + ' ' + _['pf_b']
    return s2

def validfname(s):
    try:
        if not s.strip(): 
            return False
    except:
        return False
    #
    ret = True
    for i in s:
        if not i in FORM_VALID:
            ret = False
            break
    #
    return ret

def tables(first_blank=False, exclude=EXCLUDE_TABLE):
    ret = []
    if first_blank == True: ret.append('')
    #
    r = db.select('sqlite_master', 
            where='type="table"',
            what='name',
            order="name asc")
    for i in r:
        if hasws(i.name): continue #whitespace in table name
        if not i.name in exclude:
            ret.append(i.name)
    #
    return ret

def columns(table, name_only=False):
    ret = []
    #
    if not table in tables(): return ret
    #
    q = 'pragma table_info(%s)' %(table)
    try:
        r = db.query(q)
    except:
        return ret
    #
    for i in r:
        if name_only == True:
            ret.append(i.name)
        else:
            d = {}
            for k in i.keys(): d[k.lower()] = i[k]
            ret.append(d)
    #
    return ret

def forms(first_blank=False, obj='form.code'):
    ret = []
    if first_blank == True: ret.append('')
    #
    all = s_select(obj)
    for i in all:
        try:
            if validfname(i['d']):
                ret.append(i['d'])
        except:
            pass
    #
    ret.sort()
    return ret
    
def reports(first_blank=False):
    return forms(first_blank, 'report.code')

def smsg(table, key, clear=True):
    ret = ''
    try:
        ret = sess.table[table][key]
        if clear:
            sess.table[table][key] = ''
    except:
        return ret
    #
    return ret

def smsgp(table, key=SKT_M_EDIT, clear=True):
    pos = 0
    try:
        pos = long(sess.table[table][SKT_P_EDIT])
    except:
        pass
    ret = [pos, smsg(table, key)]
    return ret

def smsgq(key, clear=True, default=[]):
    ret = default
    try:
        ret = sess[key]
        if clear:
            sess[key] = default
    except:
        return ret
    #
    return ret

def menugen():
    if not isnosb() and not sess.user: return []
    #
    ret = []
    #
    f = web.form.Dropdown(
        name='table', 
        args=tables(first_blank=True), 
        )
    #
    if (isnosb()) or (not isnosb() and sess.admin == 1):
        ret.append(
            [
                '/table/action',
                'get',
                _['x_table'],
                f, 
                (
                    ['browse', _['cmd_browse']],
                    ['browse/%s' %(DEFAULT_LIMIT), _['cmd_browse'] + ' (%s)' %(DEFAULT_LIMIT)],
                    ['insert', _['cmd_insert']],
                    ['column', _['cmd_column']],
                    ['rename', _['cmd_rename']],
                    ['table_drop', _['cmd_table_drop']],
                    ['export_csv', _['cmd_export_csv']],
                    ['table_create', _['cmd_table_create']],
                    ['query', _['cmd_query']],
                )
            ])
    #
    if not isnosb() and sess.user:
        aform = forms(first_blank=True)
        aform1 = aform[1:]
        #
        formact =  [
                    ['run', _['cmd_run']],
                ]
        for af in aform1:
            if not canform(FORM_KEY_SECURITY_RUN, af):
                aform.remove(af)
        #
        if isadmin(): 
            formact.append(['edit', _['cmd_edit']])
            formact.append(['create', _['cmd_form_create']])
        #
        f2 = web.form.Dropdown(
            name='form', 
            args=aform, 
            )
        #
        ret.append(
            [
                '/form/action',
                'get',
                _['x_form'],
                f2, 
                formact,
            ])
    #
    if not isnosb() and sess.user:
        arep = reports(first_blank=True)
        arep1 = arep[1:]
        #
        repact =  [
                    ['run', _['cmd_run']],
                ]
        for af in arep1:
            if not canreport(REPORT_KEY_SECURITY_RUN, af):
                arep.remove(af)
        #
        if isadmin(): 
            repact.append(['edit', _['cmd_edit']])
            repact.append(['create', _['cmd_report_create']])
        #
        f3 = web.form.Dropdown(
            name='report', 
            args=arep, 
            )
        #
        ret.append(
            [
                '/report/action',
                'get',
                _['x_report'],
                f3, 
                repact,
            ])
    #
    return ret

def hasws(s):
    ret = False
    #
    for w in string.whitespace:
        if w in s:
            ret = True
            break
    #
    return ret

def prepsess():
    for i in sess_init:
        if not sess.has_key(i):
            sess[i] = sess_init[i]
    #
    for t in tables():
        if not sess.table.has_key(t):
            sess.table[t] = {}
    #
    for t in tables():
        if not sess.table[t]: 
            sess.table[t] = {}
    #
    for t in tables():
        if not sess.table[t].has_key(SKT_ROWID):
            sess.table[t][SKT_ROWID] = []

def isblob(s):
    ret = True
    try:
        r = web.safeunicode(s)
        ret = False
    except:
        return ret
    return ret
    
def user():
    return sess.user
    
def isnosb():
    return not FORM_TBL in tables()
    
def sysinfo():
    s_a = '%s %s %s' %(VERSION, link(URL_README[0], _['cmd_readme']), 
        link(URL_SOURCE[0], _['cmd_source']))
    #
    s_sb0 = _['x_extended_features']
    if isnosb():
        s_sb1 = _['x_not_enabled']
        s_sb2 = link(FORM_URL_INIT, _['cmd_enable_sqliteboy'])
    else:
        s_sb1 = _['x_enabled']
        s_sb2 = ''
    s_sb = (s_sb0, '%s %s' %(s_sb1, s_sb2))
    #
    s_adm = _['x_no']
    if isadmin(): 
        s_adm = '%s %s %s %s' %(
            _['x_yes'], 
            link('/admin/users', _['cmd_users']),
            link('/admin/hosts', _['cmd_hosts']),
            link('/admin/backup', _['cmd_backup']),
            )
    if isnosb(): s_adm = _['x_not_applicable']
    #
    ret = [
            (_['x_version'], s_a),
            (_['x_sqlite_version'], db.db_module.sqlite_version),
            (_['x_python_version'], platform.python_version()),
            (_['x_web_version'], web.__version__),
            s_sb,
            (_['x_admin'], s_adm),
            (_['x_allow'], allows()),
        ]
    #
    return ret

def reqform(form):
    try:
        fo = s_select('form.code..%s' %(form))
        fo = fo[0]
        fe = json.loads(fo['e'])
        for k in FORM_REQ:
            if not fe.has_key(k):
                return False
        fed = fe[FORM_KEY_DATA]
        for k in FORM_REQ_DATA:
            for d in fed:
                if not d.has_key(k):
                    return False
    except:
        return False
    #
    return True

def fref(reference):
    reference2 = 0
    if (type(reference) in [type(''), type(u'')]) and reference:#query
        reference2 = []
        try:
            res = db.query(reference)
            for r in res:
                reference2.append(
                    [
                        r.get(FORM_REFERENCE_SQL_0, ''), 
                        r.get(FORM_REFERENCE_SQL_1, '')
                    ]
                )
        except:
            pass
    elif (type(reference) in [type([]), type(())]) and reference: #list
        reference2 = []
        try:
            for r in reference:
                reference2.append([r[0], r[1]])
        except:
            pass
    else:
        reference2 = 0
    #
    return reference2
    
def fdef(default):
    default2 = default
    if not default2:
        default2 = ''
    #
    if (type(default) in [type([])]) and default:
        default2 = ''
        #
        deff = default[0]
        default.pop(0)
        defs = []
        try:
            for dd in default:
                dq = web.sqlquote(dd)
                defs.append(dq)
            #
            if defs:
                defsq = web.sqlquote('').join(defs, ',')
            else:
                defsq = ''
            #
            defq = 'select %s(%s) as f' %(deff, defsq)
            defr = db.query(defq).list()
            if defr:
                default2 = defr[0]['f']
        except:
            pass
    #
    return default2
    
def parseform2(code, table):
    fsub = code
    if not type(fsub) == type([]):
        fsub = []
    #
    try:
        fsub_table = fsub[0]
        fsub_key = fsub[1]
        fsub_rows = fsub[2]
        fsub_data = fsub[3]
        fsub_info = fsub[4]
        #
        if not fsub_table in tables() or fsub_table == table:
            raise Exception
        if not fsub_key in columns(fsub_table, True):
            raise Exception
        if not type(fsub_data) == type([]):
            raise Exception
        if not type(fsub_rows) == type(FORM_SUB_ROWS_DEFAULT):
            raise Exception
        fsub_rows = [int(x) for x in fsub_rows if int(x) > 0 or 0]
        if fsub_rows[1] > fsub_rows[0]:
            raise Exception
        if len(fsub_rows) != len(FORM_SUB_ROWS_DEFAULT):
            raise Exception
    except:
        fsub_table = ''
        fsub_key = ''
        fsub_rows = FORM_SUB_ROWS_DEFAULT
        fsub_data = []
        fsub_info = ''
    #
    fsub2 = []
    fsub2_data = []
    if fsub_table:
        fsub2.append(fsub_table)
        fsub2.append(fsub_key)
        fsub2.append(fsub_rows)
        fsub2_columns = columns(fsub_table, True)
        #
        for d in fsub_data:
            try:
                dc = d[0].strip()
                dl = d[1].strip()
                reference = d[2]
                default = d[3]
                if (not dc) or (not dc in fsub2_columns) or dc == fsub_key:
                    raise Exception
                if not dl: 
                    dl = dc
                #
                reference2 = fref(reference)
                #
                reference3 = None
                if type(reference2) == type([]):
                    dcname = '%s.%s' %(fsub_table, dc)
                    reference3 = web.form.Dropdown(dcname, args=reference2)
                #
                default2 = fdef(default)
                #
                if reference3:
                    reference3.set_value(default2)
                #
                fsub2_data.append([dc, dl, reference3, default2])
            except:
                continue
        #
        fsub2.append(fsub2_data)
        fsub2.append(fsub_info)
    #
    return fsub2

def parseform(form):
    fo = s_select('form.code..%s' %(form))
    try:
        fo = fo[0]['e']
        fo = json.loads(fo)
    except:
        fo = {}
    #
    ftitle = fo.get(FORM_KEY_TITLE, form)
    finfo = fo.get(FORM_KEY_INFO, '')
    #single table
    fdata = fo.get(FORM_KEY_DATA)
    input = []
    colstb = {}
    if fdata:
        try:
            table = fdata[0].get(FORM_KEY_DATA_TABLE, '')
            colstb[table] = []
        except:
            table = ''
        #
        cols = columns(table)
        colsn = columns(table, name_only=True)
        #
        for fd in fdata:
            if not type(fd) == type({}):
                continue
            #
            if fd.get(FORM_KEY_DATA_TABLE,'') == table:
                col = fd.get(FORM_KEY_DATA_COLUMN,'')
                if col and (col in colsn) and (not col in colstb.get(table,[])):
                    label = fd.get(FORM_KEY_DATA_LABEL, col)
                    readonly = fd.get(FORM_KEY_DATA_READONLY, 0)
                    required = fd.get(FORM_KEY_DATA_REQUIRED, 0)
                    reference = fd.get(FORM_KEY_DATA_REFERENCE, 0)
                    default = fd.get(FORM_KEY_DATA_DEFAULT, '')
                    constraint = fd.get(FORM_KEY_DATA_CONSTRAINT, [])
                    onsave = fd.get(FORM_KEY_DATA_ONSAVE, '')
                    ftype = ''
                    for c in cols:
                        if c['name'] == col:
                            ftype = c['type']
                            #
                            if c.get('pk', 0) == 1:
                                label = '%s%s' %(label, PK_SYM)
                    #
                    reference2 = fref(reference)
                    #
                    reference3 = None
                    if type(reference2) == type([]):
                        reference3 = web.form.Dropdown(col, args=reference2)
                    #
                    default2 = fdef(default)
                    #
                    if reference3:
                        try:
                            reference3.set_value(default2)
                        except:
                            pass
                    #
                    constraint2 = []
                    try:
                        constf = constraint[0].strip()
                        consta = constraint[1]
                        constc = constraint[2]
                        conste = constraint[3]
                        constraint2 = constraint
                    except:
                        pass
                    #
                    try:
                        onsave = onsave.strip()
                    except:
                        onsave = ''
                    #
                    colstb.get(table, []).append(col)
                    #
                    input.append(
                        (
                            label, 
                            col, 
                            ftype, 
                            readonly, 
                            required,  
                            reference3, 
                            default2,
                            constraint2,
                            table,
                            onsave,
                        )
                    )
    #
    fsub = fo.get(FORM_KEY_SUB, [])
    fsub2 = parseform2(fsub, table)
    #
    message1 = fo.get(FORM_KEY_MESSAGE, [])  
    if not type(message1) == type([]):
        message1 = []
    message2 = []
    if len(message1) == FORM_MESSAGE_LEN:
        message2 = message1
    message2 = [str(x) for x in message2]        
    #
    sql2 = fo.get(FORM_KEY_SQL2, [])  
    if not type(sql2) == type([]):
        sql2 = []
    sql2 = [str(x) for x in sql2 if isstr(x)]
    #
    return [ftitle, finfo, input, fsub2, message2, sql2]

def reqreport(report):
    try:
        fo = s_select('report.code..%s' %(report))
        fo = fo[0]
        fe = json.loads(fo['e'])
        for k in REPORT_REQ:
            if not fe.has_key(k):
                return False
        fed = fe[REPORT_KEY_DATA]
        for k in REPORT_REQ_DATA:
            for d in fed:
                if not d.has_key(k):
                    return False
    except:
        return False
    #
    return True

def parsereport(report):
    fo = s_select('report.code..%s' %(report))
    try:
        fo = fo[0]['e']
        fo = json.loads(fo)
    except:
        fo = {}
    #
    ftitle = fo.get(REPORT_KEY_TITLE, report)
    finfo = fo.get(REPORT_KEY_INFO, '')
    rquery = fo.get(REPORT_KEY_SQL, '').strip()
    rheader = fo.get(REPORT_KEY_HEADER, [])
    message1 = fo.get(REPORT_KEY_MESSAGE, [])    
    #
    if not type(rheader) == type([]):
        rheader = []
    #
    if not type(message1) == type([]):
        message1 = []
    message2 = []
    if len(message1) == REPORT_MESSAGE_LEN:
        message2 = message1
    message2 = [str(x) for x in message2]    
    #
    fdata = fo.get(REPORT_KEY_DATA)
    input = []
    #
    keyadd = []
    if fdata and rquery:
        for fd in fdata:
            if not type(fd) == type({}):
                continue
            #
            key = fd.get(REPORT_KEY_DATA_KEY,'').strip()
            if (not key) or (hasws(key)) or (not validfname(key)) or (key in keyadd):
                continue
            #
            label = fd.get(REPORT_KEY_DATA_LABEL, key)
            readonly = fd.get(REPORT_KEY_DATA_READONLY, 0)
            required = fd.get(REPORT_KEY_DATA_REQUIRED, 0)
            reference = fd.get(REPORT_KEY_DATA_REFERENCE, 0)
            default = fd.get(REPORT_KEY_DATA_DEFAULT, '')
            constraint = fd.get(REPORT_KEY_DATA_CONSTRAINT, [])
            type1 = fd.get(REPORT_KEY_DATA_TYPE, '').lower().strip()
            #
            reference2 = fref(reference)
            #
            reference3 = None
            if type(reference2) == type([]):
                reference3 = web.form.Dropdown(key, args=reference2)
            #
            default2 = fdef(default)
            #
            if reference3:
                try:
                    reference3.set_value(default2)
                except:
                    pass
            #
            constraint2 = []
            try:
                constf = constraint[0].strip()
                consta = constraint[1]
                constc = constraint[2]
                conste = constraint[3]
                constraint2 = constraint
            except:
                pass
            #
            type2 = ''
            if type1 in REPORT_KEY_DATA_TYPES:
                type2 = type1
            #
            keyadd.append(key)
            #
            #as of 18-December-2012, required always 1
            required = 1
            #
            input.append(
                (
                    label,
                    key,  
                    readonly, 
                    required,  
                    reference3, 
                    default2,
                    constraint2,
                    type2,
                )
            )
    #
    return [ftitle, finfo, input, rquery, rheader, message2]

def nqtype(ftype):
    ret = False
    ftype = ftype.lower()
    #
    if ftype in NOQUOTE_TYPE or 'int' in ftype:
        ret = True
    #
    return ret 

def s_init():
    af = [x + ' ' + FORM_FIELD_TYPE for x in FORM_FIELDS]
    cmd = 'CREATE TABLE %s(%s)' %(FORM_TBL, ','.join(af))
    db.query(cmd)
    prepsess()
    db.insert(FORM_TBL, a='user', b='account', d=DEFAULT_ADMIN_USER, 
        e=md5(DEFAULT_ADMIN_PASSWORD).hexdigest(), f='1')

def favicon(width=FAVICON_WIDTH, height=FAVICON_HEIGHT, data=None):
    #ref: ico and bmp file format on wikipedia
    #little endian

    #cool chessboard-like (color: from default/builtin theme)

    w_i = width
    h_i = height

    w_b = w_i
    h_b = h_i * 2
    b_h = 40
    bpp = 24
    bxp = 3
    c_p = 1
    x_b = 1
    s_d = 2
    ppm = 2835
    clx = (128, 96, 64)
    clw = (255, 255, 255)
    clk = (0, 0, 0)

    c = ''

    #icondir
    h = (0, 1, x_b)
    s = struct.Struct('< h h h')
    p = s.pack(*h)
    c += p

    #icondirentry 1
    h = (w_i, h_i, 0, 0, c_p, bpp, b_h + (w_b * h_b * bxp), 22)
    s = struct.Struct('< b b b b h h i i')
    p = s.pack(*h)
    c += p

    #bitmapinfoheader
    h = (b_h, w_b, h_b, c_p, bpp, 0, w_b * h_b, ppm, ppm, 0, 0)
    s = struct.Struct('< I i i H H I I i i I I')
    p = s.pack(*h)
    c += p

    #pixel array
    for b in range(h_i):
        for k in range(w_b):
            if k % s_d:
                if b % s_d:
                    h = clx
                else:
                    h = clw
            else:
                if b % s_d:
                    h = clw
                else:
                    h = clx
            s = struct.Struct('< B B B')
            p = s.pack(*h)
            c += p

    #pixel array 2
    for b in range(h_i):
        for k in range(w_b):
            h = clk
            s = struct.Struct('< B B B')
            p = s.pack(*h)
            c += p

    #
    return c

def fdialog_open():
    ret = ()
    #
    if sys.platform.lower() == 'win32': 
        try:
            import win32gui
            res = win32gui.GetOpenFileNameW(
                    InitialDir=CWDIR, 
                    Title=TITLE
                )
            resf = res[0]
            ret = (os.path.basename(resf), resf)
        except:
            ret = ()
    #
    return ret
    
    
#----------------------------------------------------------------------#
# SQLITE UDF (2)                                                       #
#----------------------------------------------------------------------#
def sqliteboy_x_user():
    if isnosb(): 
        return ''
    else:
        return user()
SQLITE_UDF.append(('sqliteboy_x_user', 0, sqliteboy_x_user))


#----------------------------------------------------------------------#
# TEMPLATE                                                             #
#----------------------------------------------------------------------#
T_BASE = '''$def with (data, content)
<!DOCTYPE html>
<html>
<head>
<link rel='SHORTCUT ICON' href='/favicon.ico'>
<title>$title(data['title'], '')</title>
<meta charset='utf-8'>
<style>
*
{
    font-family     : Courier;
    font-size       : 12pt;
}
table
{
    border-collapse : collapse;
    width           : 100%;
}
td
{
    border          : 1px solid grey;
    padding         : 2px;
}
th
{
    background-color: #406080;
    border          : 1px solid grey;
    padding         : 2px;
    color           : white;
}
th a
{
    color           : white;
    text-decoration : none;
}
tr:nth-child(odd)
{
    background-color: #cccccc;
}
tr:nth-child(even)
{
    background-color: #eeeeee;
}
select
{
    width           : 95%;
}
</style>
<script>
function toggle(src, dst)
{
    a = document.getElementsByName(dst);
    for (var i=0; i<a.length; i++)
    {
        a[i].checked = src.checked;
    }
}
</script>
</head>
<body>

<table>
<tr>
<td>$title(data['title'])</td>
<td align='right' width='25%'>
$if user():
    $user() <a href='/password'>$_['cmd_password']</a>
    <a href='/notes'>$_['cmd_notes']</a> 
    <a href='/logout'>$_['cmd_logout']</a>
</td>
<td align='right' width='12%'>$size()</td>
<td align='right' width='18%'>
$if data['command'] in crt.keys():
    $if data['command'] == 'query':
        $ crtq = data['message']
        $if crtq:
            $crtq[crt['query']]
        $else:
            $rt()
$else:
    $rt()
</td>
</tr>
<tr>
<td colspan='4'>
$for i in menugen():
    <form action='$i[0]' method='$i[1]'>
    <table>
    <tr>
    <td width='12%'>
    $i[2].capitalize()
    </td>
    <td width='25%'>
    $if i[0] == '/table/action':
        $if data.has_key('table'):
            $i[3].set_value(data['table'])
    $elif i[0] == '/form/action':
        $if data.has_key('form'):
            $i[3].set_value(data['form'])
    $elif i[0] == '/report/action':
        $if data.has_key('report'):
            $i[3].set_value(data['report'])
    $i[3].render()
    </td>
    <td>
    $for j in i[4]:
        <input type='submit' name='$j[0]' value='$j[1]'>
    </td>
    </tr>
    </table>
    </form>
</td>
</tr>
</table>

<br>
$if data['command'] == 'browse':
    <form action="$data['action_url']" method="$data['action_method']">
    $ hkey = data['hidden_key']
    <input type='hidden' name="$hkey" value="$data[hkey]">
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>
    <br><br>
    <table>
    <th width='50px'><input type='checkbox' name="$data['select']_all" onclick='toggle(this, "$data['select']");'></th>
    $for c in data['columns']:
        $if c['name'] == data['column']:
            <th>
            $c['name']
            $if c['pk']:
                $pk_sym
            &nbsp;
            <a href="$data['url']?$data['column_query']">$data['column_vsort']</a>
            </th>
        $else:
            <th>
            $c['name'] 
            $if c['pk']:
                $pk_sym
            &nbsp;
            $for s in range(len(data['sort'])):
                <a href="$data['url']?$data['ksort']=$data['sort'][s]&$data['klimit']=$data['limit']&$data['korder']=$c['name']">$data['vsort'][s]</a>
            </th>
    
    $ rows = 0
    $for x in content:
        $ rows = rows + 1
        <tr>
        $ rowid = data['rowid']
        <td width='50px' align='center'>
            $if x[rowid] in data['selected']:
                <input type='checkbox' name="$data['select']" value='$x[rowid]' checked="checked">
            $else:
                <input type='checkbox' name="$data['select']" value='$x[rowid]'>
        </td>
            $for c in data['columns']:
            <td>
                $if c['type'] in data['blob_type']:
                    $if x[c['name']]:
                        <a href="$data['blob_url']?$data['blob_var']=$x[rowid]&$data['blob_column']=$c['name']">$data['blob_command']</a>
                $else:
                    $x[c['name']]
            </td>
        </tr>
    </table>
    </form>
    <br>
    $if data['limit']: 
        $_['x_limit'] $data['limit'], $rows $_['x_row']
    $else:
        $rows $_['x_row']
$elif data['command'] == 'insert':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    $if data['message']:
        <div>
            $data['message']
        </div>
    <form action="$data['action_url']" method="$data['action_method']" enctype="$data['action_enctype']">
    $for h in data['hidden']:
        <input type='hidden' name='$h[0]' value='$h[1]'>
    <table>
    $for c in data['columns']:
        <tr>
        <td width='15%'>
            $c['name']
            $if c['dflt_value']:
                <br>
                $_['x_default']: $c['dflt_value']
        </td>
        <td width='10%'>
            $c['type']
        </td>
        <td>
            $if c['type'] in data['blob_type']:
                <input type='file' name="$c['name']">
            $elif c['type'] in data['text_type']:
                <textarea name="$c['name']" rows=5 style='width:100%;'></textarea>
            $else:
                <input type='text' name="$c['name']" style='width:100%;'>
        </td>
        </tr>
    <tr>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'edit':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>

    $ rowid = data['rowid']
    $ msgp = smsgp(data['table'])
    $for x in content:
        <a name='$x[rowid]'></a>
        <form action="$data['action_url']" method="$data['action_method']" enctype="$data['action_enctype']">
        $for h in data['hidden']:
            $if h[1] == '':
                <input type='hidden' name='$h[0]' value='$x[data[h[0]]]'>
            $else:
                <input type='hidden' name='$h[0]' value='$h[1]'>
        
        $if msgp[0] == x[rowid]:
            <div>
                $msgp[1]
            </div>
        <table>
        $for c in data['columns']:
            <tr>
            <td width='15%'>
                $c['name']
                $if c['dflt_value']:
                    <br>
                    $_['x_default']: $c['dflt_value']
            </td>
            <td width='10%'>
                $c['type']
            </td>
            <td>
                $if c['type'] in data['blob_type']:
                    $if x[c['name']]:
                        <a href="$data['blob_url']?$data['blob_var']=$x[rowid]&$data['blob_column']=$c['name']">$data['blob_command']</a>
                        &nbsp;
                    <input type='file' name="$c['name']">
                $elif c['type'] in data['text_type']:
                    <textarea name="$c['name']" rows=5 style='width:100%;'>$x[c['name']]</textarea>
                $else:
                    <input type='text' name="$c['name']" style='width:100%;' value="$x[c['name']]">
            </td>
            </tr>
        <tr>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>
        $for b in data['action_button']:
            $if b[2]:
                <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
            $else:
                <input type='$b[4]' name='$b[0]' value='$b[1]'>    
        </td>
        </tr>
        </table>
        </form>
        <br>
$elif data['command'] == 'column':
    <p>
    $ hint = data['hint'][0].upper() + data['hint'][1:]
    <i>$hint</i>
    </p>
    $if data['message']:
        <div>
            $data['message']
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    $for h in data['hidden']:
        <input type='hidden' name='$h[0]' value='$h[1]'>
    <table>
    $for h in data['column_header']:
        <th>
            $h[0]
            $if h[1] == 1:
                ($_['x_optional'])
        </th>
    $for c in data['columns']:
        <tr>
        <td>
            $c['name']
        </td>
        <td>
            $c['type']
        </td>
        <td>
            $c['dflt_value']
        </td>
        </tr>
    $for m in range(data['column_max']):
        <tr>
        $for a in data['column_add']:
            <td>
                $ a.attrs['style'] = 'width: 100%'
                $a.render()
            </td>
        </tr>
    <tr>
    <td colspan='3'>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'rename':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    $if data['message']:
        <div>
            $data['message']
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    $for h in data['hidden']:
        <input type='hidden' name='$h[0]' value='$h[1]'>
    <table>
    <tr>
    <td>$_['x_rename']</td>
    <td><input type='text' name='name' value="$data['table']"></td>
    </tr>
    <tr>
    <td>&nbsp;</td>
    <td>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'drop':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    $if data['message']:
        <div>
            $data['message']
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    $for h in data['hidden']:
        <input type='hidden' name='$h[0]' value='$h[1]'>
    <table>
    <tr>
    <td>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'query':
    $ query = ''
    $ res = data['message']
    $if res:
        $ query = res[0]
    $else:
        $ query = data['query']
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    <form action="$data['action_url']" method="$data['action_method']">
    <table>
    <tr>
    <td>
    <textarea name='q' style='width: 100%;' rows='6'>$query</textarea>
    </td>
    </tr>
    <tr>
    <td>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
    <br>
    $if res:
        $res[1]<br>
        $if res[2] == 0:
            $res[3]
        $else:
            $if res[3]:
                $ ctr = 0
                $ keys = []
                <table>
                $for re in res[3]:
                    $if ctr == 0:
                        $ keys = re.keys()
                        $for k in keys:
                            <th>$k
                            </th>
                    <tr>
                    $for k in keys:
                        $ rek = re[k]
                        $if isblob(rek):
                            <td>$_['z_view_blob']</td>
                        $else:
                            <td>$rek
                            </td>
                    </tr>
                    $ ctr = ctr + 1
                </table>    
                $ctr $_['x_row']
            $else:
                $_['x_empty']
$elif data['command'] == 'create1':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    $if data['message']:
        <div>
            $data['message']
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    <table>
    $for i in data['input']:
        <tr>
        <td>$i[1]</td>
        <td>$i[0].render()
        </tr>
    <tr>
    <td>&nbsp;</td>
    <td>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'create2':
    <p>
    $ hint = ''
    $if data['hint']:
        $ hint = data['hint'][0].upper() + data['hint'][1:]
    <i>$hint</i>
    </p>
    $if data['message']:
        <div>
            $data['message']
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    $for h in data['hidden']:
        <input type='hidden' name='$h[0]' value='$h[1]'>
    $data['table']<br>
    <table>
    $for h in data['column_header']:
        <th>
            $h[0]
            $if h[1] == 1:
                ($_['x_optional'])
        </th>
    $for m in range(data['count']):
        <tr>
        $for a in data['column_add']:
            <td>
                $ a.attrs['style'] = 'width: 100%'
                $a.render()
            </td>
        </tr>
    <tr>
    <td colspan='4'>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'home':
    <br>
    $:content[0]
    <br>
    <table>
    $for i in content[1]:
        <tr>
        <td width='20%'>$i[0]</td>
        <td>$i[1]</td>
        </tr>
    </table>
$elif data['command'] in ['readme', 'source']:
    <br>
    <textarea style="width: 100%;" rows=20 readonly>
    $:content
    </textarea>
$elif data['command'] == 'login':
    $if data['message']:
        <div>
            $data['message']
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    <table>
    $for i in data['input']:
        <tr>
        <td width='25%'>$i[1]</td>
        <td>$i[0].render()
        </tr>
    <tr>
    <td colspan='2'>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'password':
    $if data['message']:
        <div>
            $data['message']
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    <table>
    $for i in data['input']:
        <tr>
        <td width='25%'>$i[1]</td>
        <td>$i[0].render()
        </tr>
    <tr>
    <td colspan='2'>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'users':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    $if data['message']:
        <div>
            $for m in data['message']:
                $m[0]: $m[1]<br>
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
        &nbsp;
    <br>
    <br>
    <table>
    $for i in data['columns']:
        <th>
            $i
        </th>
    $for u in content:
        <tr>
        <td width='12%' align='center'>
            $if not u['d'] in data['protected']:
                <input type='checkbox' name="$data['select']" value="$u['d']">
            $else:
                &nbsp;
        </td>
        <td>
            <input type='text' name='d' value="$u['d']" readonly>
        </td>
        <td>
            <input type='text' name='e'>
        </td>
        <td>
            $ sel = ''
            $if u['f'] == '1':
                $ sel = ' selected'
            <select name='f'>
                <option value=''>$_['x_no']</option>
                <option value='1'$sel>$_['x_yes']</option>
            </select>
        </td>
        </tr>
    $for u in range(data['max']):
        <tr>
        <td width='12%' align='center'>
            &nbsp;
        </td>
        <td>
            <input type='text' name='d'>
        </td>
        <td>
            <input type='text' name='e'>
        </td>
        <td>
            <select name='f'>
                <option value=''>$_['x_no']</option>
                <option value='1'>$_['x_yes']</option>
            </select>
        </td>
        </tr>
    </table>
    </form>
$elif data['command'] == 'hosts':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>    
    $if data['message']:
        <div>
            $data['message']
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    <table>
    <tr>
    <td>$data['input_host'].render()
    </td>
    </tr>
    <tr>
    <td>
    $ custom = '\\n'.join(data['custom'])
    $data['input_custom'].set_value(custom)
    $data['input_custom'].render()
    </td>
    </tr>
    <tr>
    <td colspan='2'>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'form.edit':
    <p>
    $ hint = data['hint'][0].upper() + data['hint'][1:]
    <i>$hint</i>
    </p>    
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)<br>
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    $for h in data['hidden']:
        <input type='hidden' name='$h[0]' value='$h[1]'>
    <table>
    $for i in data['input']:
        <tr>
        <td width='15%'>$i[1]</td>
        <td>$i[0].render()</td>
        </tr>
    <tr>
    <td colspan='2'>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'form.run':
    <p>
    $ hint = data['hint']
    <i>$hint</i>
    </p>    
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)<br>
        </div>
    $if data['ftitle']:
        <h3>
            $data['ftitle']
        </h3>
    $if data['finfo']:
        <div>
            $data['finfo']
        </div>
    <form action="$data['action_url']" method="$data['action_method']" enctype="$data['action_enctype']">
    $for h in data['hidden']:
        <input type='hidden' name='$h[0]' value='$h[1]'>
    <table>
    $for i in data['input']:
        <tr>
        $ lbl = i[0]
        $if i[4]:
            $ lbl = '<b>' + i[0] + '</b>'
        <td width='15%'>$lbl</td>
        <td>
        $ ro = ''
        $if i[3]:
            $ ro = ' readonly'
        
        $ defv = ''
        $if i[5]:
            $i[5].render()
        $else:
            $if i[6]:
                $ defv = i[6]
            $if i[2] in data['blob_type']:
                <input type='file' name="$i[1]"$ro>
            $elif i[2] in data['text_type']:
                <textarea name="$i[1]" rows=5 style='width:100%;'$ro>$defv</textarea>
            $else:
                <input type='text' value='$defv' name="$i[1]" style='width:100%;'$ro>        
        </td>
        </tr>
    $if data['sub']:
        $ subt = data['sub'][0]
        $ subr = data['sub'][2]
        $ subd = data['sub'][3]
        $ subc = 1
        <tr>
        <td colspan='2'>
        $data['sub'][4]
        <table>
        <th>&nbsp;</th>
        $for sh in subd:
            <th>$sh[1]</th>
        $for sr in range(subr[0]):
            <tr>
            <td align='right'>
            $if subc <= subr[1]:
                <b>$subc</b>
            $else:
                $subc
            </td>
            $for sh in subd:
                <td>
                $if sh[2]:
                    $sh[2].render()
                $else:
                    $ shv = ''
                    $if sh[3]:
                        $ shv = sh[3]
                    <input type='text' name='$subt.$sh[0]' value='$shv'>
                </td>
            </tr>
            $ subc = subc + 1
        </table>
        </td>
        </tr>
    <tr>
    <td colspan='2'>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'report.edit':
    <p>
    $ hint = data['hint'][0].upper() + data['hint'][1:]
    <i>$hint</i>
    </p>    
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)<br>
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    $for h in data['hidden']:
        <input type='hidden' name='$h[0]' value='$h[1]'>
    <table>
    $for i in data['input']:
        <tr>
        <td width='15%'>$i[1]</td>
        <td>$i[0].render()</td>
        </tr>
    <tr>
    <td colspan='2'>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'report.run':
    <p>
    $ hint = data['hint']
    <i>$hint</i>
    </p>    
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)<br>
        </div>
    $if data['ftitle']:
        <h3>
            $data['ftitle']
        </h3>
    $if data['finfo']:
        <div>
            $data['finfo']
        </div>
    <form action="$data['action_url']" method="$data['action_method']" enctype="$data['action_enctype']">
    $for h in data['hidden']:
        <input type='hidden' name='$h[0]' value='$h[1]'>
    <table>
    $for i in data['input']:
        <tr>
        $ lbl = i[0]
        $if i[3]:
            $ lbl = '<b>' + i[0] + '</b>'
        <td width='15%'>$lbl</td>
        <td>
        $ ro = ''
        $if i[2]:
            $ ro = ' readonly'
        
        $ defv = ''
        $if i[4]:
            $i[4].render()
        $else:
            $if i[5]:
                $ defv = i[5]
            <input type='text' value='$defv' name="$i[1]" style='width:100%;'$ro>        
        </td>
        </tr>
    <tr>
    <td colspan='2'>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'report.run.result':
    <h3>
    $data['report2']
    </h3>
    $if data['search']:
        <table>
        $for s in data['search']:
            <tr>
            <td width='30%'>
            $s[0]
            </td>
            <td>
            $s[1]
            </td>
            </tr>
        </table>
    <br>
    $ ctr = 0
    $if data['table']:
        $ keys = []
        <table>
        $for re in content:
            $if ctr == 0:
                $if not data['header']:
                    $ keys = re.keys()
                $else:
                    $ keys = data['header']
                $for k in keys:
                    <th>$k
                    </th>
            <tr>
            $for k in keys:
                $ rek = re.get(k, '')
                $if isblob(rek):
                    <td>$_['z_view_blob']</td>
                $else:
                    <td>$rek
                    </td>
            </tr>
            $ ctr = ctr + 1
        </table>    
        $ctr $_['x_row']
    $else:
        $if data['result_message']:
            $data['result_message']
        $else:
            $content
$elif data['command'] == 'notes':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)
                <br>
        </div>
    <form action="$data['action_url']" method="$data['action_method']">
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
        &nbsp;
    <br>
    <br>
    <table>
    $for i in data['columns']:
        <th>
            $if i == data['select_all']:
                <input type='checkbox' name="$data['select']_all" onclick='toggle(this, "$data['select']");'> $i
            $else:
                $i
        </th>
    $for u in content:
        <tr>
        <td width='12%' align='center'>
            <input type='checkbox' name="$data['select']" value="$u['d']">
        </td>
        <td width='20%'>
            <input type='hidden' name='d' value="$u['d']">
            <input type='text' name='e' value="$u['e']">
        </td>
        <td>
            <textarea name='f' rows='5' style='width: 90%'>$u['f']</textarea>
        </td>
        <td>
            $if data['xaction']:
                $for a in data['xaction']:
                    <a href='$a[1]$u['d']'>$a[0]</a> 
            $else:
                &nbsp;
        </td>
        </tr>
    $for u in range(data['max']):
        <tr>
        <td width='12%' align='center'>
            &nbsp;
        </td>
        <td width='20%'>
            <input type='hidden' name='d' value=''>
            <input type='text' name='e'>
        </td>
        <td>
            <textarea name='f' rows='5' style='width: 90%'></textarea>
        </td>
        <td>
            &nbsp;
        </td>
        </tr>
    </table>
    </form>
$else:
    $:content
</body>
</html>
'''
test_t_base = os.path.join(CWDIR, DEFAULT_T_BASE)
test_t_base = os.path.abspath(test_t_base)
if os.access(test_t_base, os.R_OK):
    T_BASE = open(test_t_base).read()

#
GLBL = {
    '_'         : _,
    'rt'        : rt,
    'title'     : title,
    'size'      : size,
    'menugen'   : menugen,
    'smsg'      : smsg,
    'smsgp'     : smsgp,
    'crt'       : CUSTOM_RT,
    'isblob'    : isblob,
    'pk_sym'    : PK_SYM,
    'user'      : user,
    }
T = web.template.Template(T_BASE, globals=GLBL)


#----------------------------------------------------------------------#
# CLASS                                                                #
#----------------------------------------------------------------------#
class index:
    def GET(self):
        start()
        #
        input = web.input(form='', report='')
        #
        form = input.form.lower().strip()
        xform = ''
        if not isnosb() and form in forms():
            if canform(FORM_KEY_SECURITY_RUN, form):
                xform = form
        #
        report = input.report.lower().strip()
        xreport = ''
        if not isnosb() and report in reports():
            if canreport(REPORT_KEY_SECURITY_RUN, report):
                xreport = report
        #
        stop()
        data = {'title': '', 'command': 'home', 'form': xform, 'report': xreport}
        content = (
                    '%s <a href="%s">%s</a>' %(_['x_welcome2'], WSITE, NAME),
                    sysinfo(),
                )
        return T(data, content)


class favicon_ico:
    def GET(self):
        content = ''
        #
        try:
            content = favicon()
        except:
            pass
        #
        web.header('Content-Type', 'image/x-icon')
        return content
        

class table_action:
    def GET(self):
        input = web.input()
        if not input.has_key('table'):
            dflt()
        #
        table = input.table.strip()
        redir = (
            ('browse', '/table/browse/' + table),
            ('browse/%s' %(DEFAULT_LIMIT), '/table/browse/' + table + '?limit=%s' %(DEFAULT_LIMIT)),
            ('insert', '/table/row/' + table + '?mode=%s' %(MODE_INSERT)),
            ('column', '/table/column?table=' + table),
            ('rename', '/table/rename?table=' + table),
            ('table_drop', '/table/drop?table=' + table),
            ('export_csv', '/table/csv?table=' + table),
            ('table_create', '/table/create'),
            ('query', '/query'),
        )
        #
        prepsess()
        #
        for i in redir:
            if input.has_key(i[0]):
                raise web.seeother(i[1])
        #
        dflt()
        
    def POST(self):
        input = web.input(select=[])
        if not input.has_key('table'):
            dflt()
        #
        table = input.table.strip()
        #
        select = input.select
        if not len(select):
            raise web.seeother('/table/browse/%s' %(table))
        #
        try:
            select = [int(x) for x in select]
        except:
            dflt()
        #
        if input.has_key('delete'):
            for i in select:
                db.delete(table, where='%s=%s' %(ROWID, i))
            raise web.seeother('/table/browse/%s' %(table))
        #
        elif input.has_key('edit'):
            sess.table[table][SKT_ROWID] = select
            raise web.seeother('/table/row/%s' %(table))
        #
        dflt()
        
class table_row:
    def GET(self, table):
        if not table in tables(): 
            dflt()
        #
        input = web.input(mode='')
        mode = input.mode
        #
        if not mode == MODE_INSERT and not len(sess.table[table][SKT_ROWID]):
            dflt()
        #
        start()
        #
        if mode == MODE_INSERT:
            data = {
                'title': '%s - %s' %(table, _['tt_insert']),
                'command': 'insert',
                'table': table,
                'columns': columns(table),
                'hidden': (('table', table), ('mode', MODE_INSERT)),
                'action_url': '/table/save',
                'action_method': 'post',
                'action_enctype': 'multipart/form-data',
                'action_button': (
                                    ('insert', _['cmd_insert'], False, '', 'submit'),
                                ),
                'blob_type': BLOB_TYPE,
                'text_type': TEXT_TYPE,
                'message': smsg(table, SKT_M_INSERT),
                'hint': _['h_insert'],
            }
            content = ''
        else:
            data = {
                'title': '%s - %s' %(table, _['tt_edit']),
                'command': 'edit',
                'table': table,
                'columns': columns(table),
                'hidden': (('table', table), ('rowid', '')),
                'action_url': '/table/save',
                'action_method': 'post',
                'action_enctype': 'multipart/form-data',
                'action_button': (
                                    ('edit', _['cmd_edit'], False, '', 'submit'),
                                ),
                'blob_type': BLOB_TYPE,
                'blob_url': '/table/blob/%s' %(table),
                'blob_var': BLOB_VAR,
                'blob_column': BLOB_COLUMN,
                'blob_command': _['cmd_download'],
                'text_type': TEXT_TYPE,
                'rowid': rowid,
                'rowid_key': 'rowid',
                'hint': _['h_edit'],
            }
            multi = '(%s)' %(','.join([str(x) for x in sess.table[table][SKT_ROWID] ]))
            content = db.select(table, what='%s as %s, *' %(ROWID, rowid), where="%s in %s" %(ROWID, multi) )
        #
        stop()
        return T(data, content)


class table_save:
    def POST(self):
        input = web.input(mode='', table='', rowid='')
        mode = input.mode.strip()
        table = input.table.strip()
        rowid = input.rowid
        #
        if not table in tables():
            dflt()
        #
        cols = columns(table)
        #
        if mode == MODE_INSERT:
            vars = {}
            defs = []
            for c in cols:
                cn = c['name']
                if input.has_key(cn):
                    v = input[cn]
                    if c['type'] in BLOB_TYPE:
                        vr = db.db_module.Binary(v)
                    else:
                        vr = v
                    if len(v) > 0:
                        vars[cn] = vr
                    else:
                        if c[DFLT_VALUE] is not None:
                            defs.append(cn)
            #
            vk = vars.keys()
            if not vk and len(defs) < 1:
                raise web.seeother('/table/row/%s?mode=insert' %(table))
            #
            if not vk and len(defs) > 0: #no user, has defaults
                q = 'insert into %s default values' %(table)
            elif vk:
                vv = ['$'+v for v in vk]
                q = 'insert into %s(%s) values(%s)' %(table, ','.join(vk), ','.join(vv))
            #
            try:
                db.query(q, vars=vars)
                sess.table[table][SKT_M_INSERT] = _['o_insert']
            except Exception, e:
                sess.table[table][SKT_M_INSERT] = '%s: %s' %(_['e_insert'], e.message) 
            raise web.seeother('/table/row/%s?mode=insert' %(table))
        else:
            if not rowid:
                dflt()
            #
            vars = {}
            for c in cols:
                cn = c['name']
                if input.has_key(cn):
                    v = input[cn]
                    if c['type'] in BLOB_TYPE:
                        if len(v) < 1:
                            continue
                        vr = db.db_module.Binary(v)
                    else:
                        vr = v
                    vars[cn] = vr
            #
            vk = vars.keys()
            if not vk:
                raise web.seeother('/table/row/%s' %(table))
            #
            va = ['%s=$%s' %(v, v) for v in vk] 
            q = 'update %s set %s where rowid=%s' %(table, ','.join(va), rowid)
            sess.table[table][SKT_P_EDIT] = rowid
            try:
                db.query(q, vars=vars)
                sess.table[table][SKT_M_EDIT] = _['o_edit']
            except Exception, e:
                sess.table[table][SKT_M_EDIT] = '%s: %s' %(_['e_edit'], e.message) 
            raise web.seeother('/table/row/%s#%s' %(table, rowid))
        

class table_blob:
    def GET(self, table):
        if not table in tables(): 
            dflt()
        #
        input = web.input(column='', rowid=0)
        column = input.column
        rowid = input.rowid
        #
        if not column in columns(table, True): 
            dflt()
        #
        d = None
        try:
            d = db.select(table, what=column, where='%s=%s' %(ROWID, rowid))
        except:
            dflt()
        #
        r = list(d)
        if not r:
            dflt()
        else:
            disposition = 'attachment; filename=' + '%s_%s_%s' %(table, column, rowid)
            web.header('Content-Type', BLOB_CTYPE)
            web.header('Content-Disposition', disposition)
            return r[0][column]
        

class table_browse:
    def GET(self, table):
        if not table in tables(): 
            dflt()
        #
        start()
        #
        prepsess()
        #
        input = web.input(limit=0, order='', sort='')
        #
        try:
            limit = int(input.limit)
        except:
            limit = 0
        #
        order = input.order
        qorder = None
        sort = input.sort
        column_query = ''
        column_sort = ''
        if not limit:
            limit = None
        if not order:
            order = None
        else:
            if not order in columns(table, True):
                order = None
            else:
                if not sort in SORT: sort = SORT[0]
                #
                if not limit:
                    column_query = 'order=%s&sort=%s' %(order, ssort(sort))
                else:
                    column_query = 'order=%s&sort=%s&limit=%s' %(order, ssort(sort), limit)
                #
                column_sort = vsort(sort) #current, not next
                qorder = '%s %s' %(order, sort)
        #
        glimit = ''
        if limit: glimit = str(limit)
        #
        r = db.select(table, what='%s as %s, *' %(ROWID, rowid), order=qorder, limit=limit)
        #
        data = {
            'title': table, 
            'command': 'browse',
            'table': table,
            'columns': columns(table),
            'url': '/table/browse/%s' %(table),
            'column': order,
            'column_vsort': column_sort,
            'column_query': column_query,
            'vsort': VSORT,
            'sort': SORT,
            'ksort': 'sort',
            'korder': 'order',
            'klimit': 'limit',
            'limit': glimit, 
            'select': NAME_SELECT,
            'action_url': '/table/action',
            'action_method': 'post',
            'action_button': (
                                ('delete', _['cmd_delete_selected'], True, _['cf_delete_selected'], 'submit'), 
                                ('edit', _['cmd_edit_selected'], False, '', 'submit'),
                            ),
            'hidden_key': 'table',
            'rowid' : rowid,
            'blob_type': BLOB_TYPE,
            'blob_url': '/table/blob/%s' %(table),
            'blob_var': BLOB_VAR,
            'blob_column': BLOB_COLUMN,
            'blob_command': _['cmd_download'],
            'selected': sess.table[table][SKT_ROWID],
            }
        #
        stop()
        return T(data, r)


class table_column:
    def GET(self):
        table = web.input(table='').table
        if not table in tables(): 
            dflt()
        #
        start()
        #
        data = {
            'title': '%s - %s' %(table, _['tt_column']),
            'command': 'column',
            'table': table,
            'columns': columns(table),
            'hidden': (('table', table),),
            'action_url': '/table/column',
            'action_method': 'post',
            'action_button': (
                                ('add', _['cmd_add'], False, '', 'submit'),
                            ),
            'message': smsg(table, SKT_M_COLUMN),
            'hint': _['h_column'],
            'column_max': MAX_COLUMN_ADD,
            'column_header': (
                                (_['x_name'], 0), 
                                (_['x_type'], 0),
                                (_['x_default'], 1),
                            ),
            'column_add': (
                            web.form.Textbox('name'),
                            web.form.Dropdown('type', args=[x[0] for x in COLUMN_TYPES if x[1]]),
                            web.form.Textbox('default'),
                        ),
        }
        content = ''
        stop()
        return T(data, content)
        
    def POST(self):
        input = web.input(table='', name=[], type=[], default=[])
        table = input.table
        name = input.name
        type = input.type
        default = input.default
        if not table in tables(): 
            dflt()
        #
        name = [x.strip() for x in name]
        type = [x.strip() for x in type]
        #
        if not len(name):
            raise web.seeother('/table/column?table=%s' %(table))
        #
        st = []
        for i in range(len(name)):
            if not name[i] or not type[i]: 
                continue
            #
            if default[i]:
                defs = default[i]
                if hasws(defs):
                    defs = web.db.sqlquote(defs)
                q = 'alter table %s add column %s %s default %s' %(
                    table, name[i], type[i], defs)
            else:
                q = 'alter table %s add column %s %s' %(
                    table, name[i], type[i])
            #
            st.append([q, name[i]])
        #
        if not st:
            raise web.seeother('/table/column?table=%s' %(table))
        #
        err = []
        for s in st:
            try:
                db.query(s[0])#FIXME: security sql injection?
            except Exception, e:
                err.append('(%s) %s' %(s[1], e.message) )
        #
        if err:
            msg = '%s: ' %(_['th_error']) +  ', '.join(err)
        else:
            msg = _['o_column']
        sess.table[table][SKT_M_COLUMN] = msg
        #
        raise web.seeother('/table/column?table=%s' %(table))
        

class table_rename:
    def GET(self):
        table = web.input(table='').table
        if not table in tables(): 
            dflt()
        #
        start()
        #
        data = {
            'title': '%s - %s' %(table, _['tt_rename']),
            'command': 'rename',
            'table': table,
            'hidden': (('table', table),),
            'action_url': '/table/rename',
            'action_method': 'post',
            'action_button': (
                                ('rename', _['cmd_rename'], False, '', 'submit'),
                            ),
            'message': smsg(table, SKT_M_RENAME),
            'hint': _['h_rename'],
        }
        content = ''
        stop()
        return T(data, content)
        
    def POST(self):
        input = web.input(table='', name='')
        table = input.table.strip()
        name = input.name.strip()
        if not table in tables() or not name: 
            dflt()
        #
        if name == table:
            raise web.seeother('/table/rename?table=%s' %(table))
        #
        if hasws(name):
            sess.table[table][SKT_M_RENAME] = _['z_table_whitespace']
            raise web.seeother('/table/rename?table=%s' %(table))
        #
        q = 'alter table %s rename to %s' %(table, name) #FIXME: security sql injection?
        try:
            db.query(q)
            msg = _['o_rename']
            new = name
            sess.table[new] = sess.table[table]
            del sess.table[table]
        except Exception, e:
            msg = '%s: %s' %(_['e_rename'], e.message)
            new = table
        #
        sess.table[new][SKT_M_RENAME] = msg
        #
        redir = '/table/rename?table=%s' %(new)
        raise web.seeother(redir)


class table_drop:
    def GET(self):
        table = web.input(table='').table
        if not table in tables(): 
            dflt()
        #
        start()
        #
        data = {
            'title': '%s - %s' %(table, _['tt_drop']),
            'command': 'drop',
            'table': table,
            'hidden': (('table', table), ('confirm', '1')),
            'action_url': '/table/drop',
            'action_method': 'post',
            'action_button': (
                                ('drop', _['cf_drop'], False, '', 'submit'),
                            ),
            'message': smsg(table, SKT_M_DROP),
            'hint': _['h_drop'],
        }
        content = ''
        stop()
        return T(data, content)
        
    def POST(self):
        input = web.input(table='', confirm='')
        table = input.table.strip()
        confirm = input.confirm.strip()
        if not table in tables() or not confirm: 
            dflt()
        #
        q = 'drop table %s' %(table) #FIXME: security sql injection?
        try:
            db.query(q)
            del sess.table[table]
        except Exception, e:
            msg = '%s: %s' %(_['e_drop'], e.message)
            sess.table[table][SKT_M_DROP] = msg
            redir = '/table/drop?table=%s' %(table)
            raise web.seeother(redir)
        #
        dflt()        


class table_csv:
    def GET(self):
        table = web.input(table='').table
        if not table in tables(): 
            dflt()
        #
        cols = columns(table)
        if not cols:
            dflt()
        #
        try:
            res = db.select(table, what='*', order='rowid asc')
        except:
            res = None
        #
        fout = cStringIO.StringIO()
        writer = csv.writer(fout)
        #
        header = [c['name'] for c in cols]
        writer.writerow(header)
        #
        types = {}
        for c in cols:
            types[c['name']] = c['type']
        #
        if res:
            for r in res:
                line = []
                for h in header:
                    data = r.get(h, '')
                    if data and types.get(h, '') in BLOB_TYPE:
                        data = base64.b64encode(data)
                    line.append(data)
                #
                writer.writerow(line)
        #
        content = fout.getvalue()
        #
        disposition = 'attachment; filename=' + '%s%s' %(table, CSV_SUFFIX)
        web.header('Content-Type', CSV_CTYPE)
        web.header('Content-Disposition', disposition)
        return content
        

class query:
    def GET(self):
        start()
        #
        inp = web.input(src='', sid='')
        q = ''
        #
        if not isnosb():
            notes = s_select('my.notes.%s' %(user()))
            alld = [x['d'] for x in notes]
            if inp.src == 'notes' and inp.sid in alld:
                for n in notes:
                    if n['d'] == inp.sid:
                        q = n['f']
                        break
        #
        data = {
            'title': '%s' %(_['tt_query']),
            'command': 'query',
            'action_url': '/query',
            'action_method': 'post',
            'action_button': (
                                ('query', _['cmd_query'], False, '', 'submit'),
                            ),
            'hint': _['h_query'],
            'message': smsgq('query'),
            'blob_type': BLOB_TYPE,
            'query': q,
        }
        content = ''
        stop()
        return T(data, content)
        
    def POST(self):
        q = web.input(q='').q.strip()
        if not q:
            raise web.seeother('/query')
        #
        start()
        try:
            msg = db.query(q)
            err = _['th_ok']
            multi = 1
            if type(msg) == type(1):
                multi = 0 
        except Exception, e:
            msg = e.message
            err = _['th_error']
            multi = 0
        #
        stop()
        t = rt()
        #
        prepsess()
        sess.query = [q, err, multi, msg, t]
        raise web.seeother('/query')


class table_create:
    def GET(self):
        input = web.input(count='', table='', step='')
        count = input.count
        table = input.table.strip()
        step = input.step.strip()
        try:
            count = int(count)
        except:
            count = 0
        scount = ''
        if count: scount = '%s' %(count)
        start()
        #
        if step == 'b' and count and table and not table in tables() and not hasws(table):
            data = {
                'title': '%s' %(_['tt_create']),
                'command': 'create2',
                'count': count,
                'table': table,
                'hidden': (('count', count), ('table', table), ('step', 'b'),),
                'action_url': '/table/create',
                'action_method': 'post',
                'action_button': (
                                    ('create', _['cmd_table_create'], False, '', 'submit'),
                                ),
                'message': smsgq(SK_CREATE, default=''),
                'hint': _['h_create2'],
                'column_header': (
                                    (_['x_name'], 0), 
                                    (_['x_type'], 0),
                                    (_['x_primary_key'], 1),
                                    (_['x_default'], 1),
                                ),
                'column_add': (
                                web.form.Textbox('name'),
                                web.form.Dropdown('type', args=[x[0] for x in COLUMN_TYPES]),
                                web.form.Dropdown('pk', args=('', _['x_yes'])),
                                web.form.Textbox('default'),
                            ),
            }
        else:
            data = {
                'title': '%s' %(_['tt_create']),
                'command': 'create1',
                'action_url': '/table/create',
                'action_method': 'post',
                'action_button': (
                                    ('next', _['cmd_next'], False, '', 'submit'),
                                ),
                'input': (
                            (web.form.Textbox('count', value=scount), _['x_column_number'],),
                            (web.form.Textbox('table', value=table), _['x_table_name'],),
                        ),
                'message': smsgq(SK_CREATE, default=''),
                'hint': _['h_create'],
            }

        content = ''
        stop()
        return T(data, content)

    def POST(self):
        input = web.input(count=0, table='', step='', name=[], type=[], pk=[], default=[])
        count = input.count
        table = input.table.strip()
        step = input.step.strip()
        name = [x.strip() for x in input.name]
        type = [x.strip() for x in input.type]
        pk = [x.strip() for x in input.pk]
        default = input.default
        try:
            count = int(count)
        except:
            count = 0
        #
        if step == 'b':
            if not table or table in tables() or hasws(table):
                raise web.seeother('/table/create')
            #
            url = '/table/create?step=b&table=%s&count=%s' %(table, count)
            #
            if not len(name):
                raise web.seeother(url)
            #
            st = []
            pkeys = []
            for i in range(len(name)):
                if not name[i] or not type[i]: 
                    continue
                #
                if pk[i] and not 'primary' in type[i]:
                    pkeys.append(name[i])
                #
                defs2 = ''
                if default[i]:
                    defs = default[i]
                    if hasws(defs):
                        defs = web.db.sqlquote(defs)
                    else:
                        defs = web.sqlliteral(defs)
                    if defs:
                        defs2 = 'default %s' %(defs)
                #
                qc = '%s %s %s' %(name[i], type[i], defs2)
                st.append(qc)
            #
            if not st:
                raise web.seeother(url)
            #
            if pkeys:
                q = 'create table %s(%s, primary key(%s))' %(table, ','.join(st), ','.join(pkeys))
            else:
                q = 'create table %s(%s)' %(table, ','.join(st))
            try:
                db.query(q)#FIXME: security sql injection?
            except Exception, e:
                msg = '%s: %s' %(_['th_error'], e.message)
                sess[SK_CREATE] = msg
                raise web.seeother(url)
            #
            prepsess()
            raise web.seeother('/table/browse/%s' %(table))
        else:
            if not count or not table or table in tables() or hasws(table):
                t = 'table=%s' %(table)
                if table in tables():
                    sess[SK_CREATE] = _['e_table_exists']
                if hasws(table):
                    t = ''
                    sess[SK_CREATE] = _['z_table_whitespace']
                raise web.seeother('/table/create?count=%s&%s' %(count, t))
            else:
                raise web.seeother('/table/create?step=b&count=%s&table=%s' %(count, table))
        #
        dflt()


class sqliteboy_init:
    def GET(self):
        if isnosb():
            s_init()
        #
        dflt()
     
        
class sqliteboy_readme:
    def GET(self):
        start()
        data = {
                'title': _['tt_readme'],
                'command': 'readme',
            }
        #
        try:
            content = open(os.path.join(CURDIR, URL_README[2])).read()
        except:
            content = _['e_open_file']
        #
        stop()
        return T(data, content)


class sqliteboy_source:
    def GET(self):
        start()
        data = {
                'title': _['tt_source'],
                'command': 'source',
            }
        #
        try:
            content = web.htmlquote(open(os.path.join(CURDIR, URL_SOURCE[2])).read())
        except:
            content = _['e_open_file'] 
        #
        stop()
        return T(data, content)


class login:
    def GET(self):
        start()
        #
        data = {
                'title': _['tt_login'],
                'command': 'login',
                'action_url': '/login',
                'action_method': 'post',
                'action_button': (
                                    ('login', _['cmd_login'], False, '', 'submit'),
                                ),
                'input': (
                            (web.form.Textbox('user'), _['x_user'],),
                            (web.form.Password('password'), _['x_password'],),
                        ),
                'message': smsgq(SK_LOGIN, default=''),
            }
        content = ''
        #
        stop()
        return T(data, content)
    
    def POST(self):
        input = web.input(user='', password='')
        user = input.user.strip()
        password = input.password.strip()
        if not user or not password:
            raise web.seeother('/login')
        #
        all = s_select('user.account')
        for a in all:
            if a['d'] == user and a['e'] == md5(password).hexdigest():
                sess.user = user
                if a['f'] == '1': 
                    sess.admin = 1
        #
        if not sess.user:
            sess[SK_LOGIN] = _['e_login']
            raise web.seeother('/login')
        #
        dflt()
        

class logout:
    def GET(self):
        sess.user = ''
        sess.admin = 0
        dflt()


class password:
    def GET(self):
        start()
        #
        data = {
                'title': _['tt_password'],
                'command': 'password',
                'action_url': '/password',
                'action_method': 'post',
                'action_button': (
                                    ('password', _['cmd_password'], False, '', 'submit'),
                                ),
                'input': (
                            (web.form.Password('old'), _['x_password_old'],),
                            (web.form.Password('password1'), _['x_password_new'],),
                            (web.form.Password('password2'), _['x_password_new_repeat'],),
                        ),
                'message': smsgq(SK_PASSWORD, default=''),
            }
        content = ''
        #
        stop()
        return T(data, content)
    
    def POST(self):
        input = web.input(old='', password1='', password2='')
        old = input.old.strip()
        password1 = input.password1.strip()
        password2 = input.password2.strip()
        q = 'user.account..%s' %(sess.user)
        me = s_select(q)
        #
        if not len(me) == 1:
            raise web.seeother('/password')
        #
        me0 = me[0]
        if me0['e'] == md5(old).hexdigest():
            if password1 != password2:
                sess[SK_PASSWORD] = _['e_password_mismatch']
            else:
                if not password1:
                    sess[SK_PASSWORD] = _['e_password_blank']
                else:
                    try:
                        db.update(FORM_TBL, where='a=$a and b=$b and d=$d', 
                            e = md5(password1).hexdigest(), 
                            vars = {'a': 'user', 'b': 'account', 'd': sess.user}
                        )
                        sess[SK_PASSWORD] = _['o_password']
                    except:
                        sess[SK_PASSWORD] = _['e_password_general']
        else:
            sess[SK_PASSWORD] = _['e_password_auth']
        #
        raise web.seeother('/password')


class admin_users:
    def GET(self):
        start()
        #
        protected = PROTECTED_USERS + [sess.user]
        data = {
                'title': _['tt_users'],
                'command': 'users',
                'action_url': '/admin/users',
                'action_method': 'post',
                'action_button': (
                                    ('save', _['cmd_save'], False, '', 'submit'),
                                ),
                'columns': (
                            _['x_delete'], 
                            _['x_user'], 
                            _['x_password_new'], 
                            _['x_admin'],
                        ),
                'protected': protected,
                'select': 'select',
                'max': 3,
                'message': smsgq(SK_USERS),
                'hint': _['h_users'],
            }
        content = s_select('user.account')
        #
        stop()
        return T(data, content)
    
    def POST(self):
        protected = PROTECTED_USERS + [sess.user]
        input = web.input(select=[], d=[], e=[], f=[])
        select = input.select
        d = input.d
        e = input.e
        f = input.f
        msg = []
        #
        #delete
        all = s_select('user.account')
        alld = [x['d'] for x in all]
        for s in select:
            if s in alld and not s in protected:
                try:
                    db.delete(FORM_TBL, where='a=$a and b=$b and d=$d', 
                        vars={'a': 'user', 'b': 'account', 'd': s}
                    )
                    m = (_['x_deleted'], s)
                    msg.append(m)
                except:
                    pass
        #password
        all = s_select('user.account')
        alld = [x['d'] for x in all]
        for i in range(len(d)):
            di = d[i]
            ei = e[i].strip()
            if (di in alld) and (not di in select) and ei:
                try:
                    db.update(FORM_TBL, where='a=$a and b=$b and d=$d',
                        e=md5(ei).hexdigest(),
                        vars = {'a': 'user', 'b': 'account', 'd': di}
                    )
                    m = (_['x_password_changed'], di)
                    msg.append(m)
                except:
                    pass
        #admin
        all = s_select('user.account')
        alld = [x['d'] for x in all]
        for i in range(len(d)):
            di = d[i]
            fi = f[i].strip()
            old = {}
            for o in all:
                if o['d'] == di:
                    old = o
                    break
            if (di in alld) and (not di in select) and (not di in protected) and (fi in ['', '1']):
                oldfi = old['f']
                if fi == oldfi: continue
                try:
                    db.update(FORM_TBL, where='a=$a and b=$b and d=$d',
                        f=fi,
                        vars = {'a': 'user', 'b': 'account', 'd': di}
                    )
                    m = (_['x_admin_changed'], di)
                    msg.append(m)
                except:
                    pass
        #new
        all = s_select('user.account')
        alld = [x['d'] for x in all]
        for i in range(len(d)):
            di = d[i].strip().lower()
            ei = e[i]
            fi = f[i].strip()
            if (di) and (not di in alld) and (not di in select) and (not di in protected) and (not hasws(di)) and (ei) and (fi in ['', '1']):
                try:
                    db.insert(FORM_TBL, a='user', b='account', d=di, 
                        e=md5(ei).hexdigest(), f=fi
                    )
                    m = (_['x_added'], di)
                    msg.append(m)
                except:
                    pass
        #
        sess[SK_USERS] = msg
        raise web.seeother('/admin/users')
                

class admin_hosts:
    def GET(self):
        start()
        #
        saved = s_select('security.hosts')
        saved = saved[0]
        hosts = (
                    (HOST_LOCAL, _['a_local']),
                    (HOST_ALL, _['a_all']),
                    (HOST_CUSTOM, _['a_custom']),
                )
        custom = json.loads(saved['e'])
        data = {
                'title': _['tt_hosts'],
                'command': 'hosts',
                'action_url': '/admin/hosts',
                'action_method': 'post',
                'action_button': (
                                    ('save', _['cmd_save'], False, '', 'submit'),
                                ),
                'custom': custom,
                'input_host': web.form.Radio('host', args=hosts, value=saved['d']),
                'input_custom': web.form.Textarea('custom', 
                                    cols=DEFAULT_TEXTAREA_COLS, 
                                    rows=DEFAULT_TEXTAREA_ROWS
                                ),
                'message': smsgq(SK_HOSTS, default=''),
                'hint': _['h_hosts'],
            }
        content = ''
        #
        stop()
        return T(data, content)
    
    def POST(self):
        input = web.input(host='', custom='')
        host = input.host.strip()
        custom = input.custom.strip()
        #
        shost = HOST_LOCAL
        #
        if host in [HOST_LOCAL, HOST_ALL, HOST_CUSTOM]:
           shost = host
        #
        scustom = custom.split()
        if not scustom:
            scustom = []
        scustom = [x.strip() for x in scustom if x.strip()]
        scustom = json.dumps(scustom)
        #
        try:
            saved = s_select('security.hosts')
            if not saved:
                db.insert(FORM_TBL, a='security', b='hosts', d=shost, e=scustom)
            else:
                db.update(FORM_TBL, where='a=$a and b=$b', d=shost, e=scustom,
                    vars = {'a': 'security', 'b': 'hosts'}
                )
            sess[SK_HOSTS] = _['o_hosts']
        except:
            sess[SK_HOSTS] = _['e_hosts']
        #
        raise web.seeother('/admin/hosts')


class admin_backup:
    def GET(self):
        bf = '%s_%s' %(
            time.strftime(PYTIME_FORMAT_BACKUP), 
            os.path.basename(dbfile0),
            )
        #
        disposition = 'attachment; filename=' + '%s' %(bf)
        web.header('Content-Type', BLOB_CTYPE)
        web.header('Content-Disposition', disposition)
        web.header('Transfer-Encoding', 'chunked')
        #
        try:
            f = open(dbfile0, 'rb')
        except:
            f = None
        #
        if f:
            while True:
                read = f.read(BACKUP_BUFFER)
                #
                if not read:
                    break
                #
                yield read
            #
            f.close()
        else:
            yield ''


class form_action:
    def GET(self):
        input = web.input()
        if not input.has_key('form'):
            dflt()
        #
        form = input.form.strip()
        redir = (
            ('run', '/form/run/' + form),
            ('edit', '/form/edit?form=' + form),
            ('create', '/form/edit?mode=' + MODE_INSERT),
        )
        for i in redir:
            if input.has_key(i[0]):
                raise web.seeother(i[1])
        #
        dflt()


class form_run:
    def GET(self, form):
        start()
        #
        if not form.strip() or not form.strip() in forms():
            dflt()
        #
        if not canform(FORM_KEY_SECURITY_RUN, form):
            dflt()
        #
        if not validfname(form):
            dflt()
        #
        input = ()
        sub = ()
        action_button = (
                            ('save', _['cmd_save'], False, '', 'submit'),
                        )
        ftitle = ''
        finfo = ''
        if not reqform(form):
            input = ()
            sub = ()
            action_button = ()
            sess[SKF_RUN] = [
                                [_['e_form_run_syntax_or_required']],
                            ]
        else:
            try:
                pform = parseform(form)
            except:
                pform = [ftitle, finfo, input, sub]
            #
            ftitle = pform[0]
            finfo = pform[1]
            input = pform[2]
            sub = pform[3]
        #
        message = smsgq(SKF_RUN, default=[])
        #
        data = {
                'title': '%s - %s' %(_['tt_form_run'], form), 
                'command': 'form.run',
                'form': form,
                'message': message,
                'input': input,
                'hidden': (('hform', form),),
                'action_url': '/form/run/%s' %(form),
                'action_method': 'post',
                'action_enctype': 'multipart/form-data',
                'action_button': action_button,
                'hint': _['h_form_run'],
                'ftitle': ftitle,
                'finfo': finfo,
                'blob_type': BLOB_TYPE,
                'text_type': TEXT_TYPE,
                'sub': sub,
                }
        content = ''
        stop()
        return T(data, content)
        
    def POST(self, unused):
        input = web.input(hform='')
        form = input.hform.strip()
        #
        if not form:
            dflt()
        #
        if not canform(FORM_KEY_SECURITY_RUN, form):
            dflt()
        #
        if not validfname(form):
            dflt()
        #
        finput = None
        fsub = None
        message2 = None
        fsql2 = None
        try:
            pform = parseform(form)
            finput = pform[2]
            fsub = pform[3]
            message2 = pform[4]
            fsql2 = pform[5]
        except:
            pform = None
            fsub = None
            message2 = None
        #
        if not pform or not finput:
            dflt()
        #
        errors = []
        ecols = []
        ocols = {}
        stable = ''
        #
        for f in finput:
            try:
                label = f[0] 
                col = f[1]
                ftype = f[2]
                readonly = f[3]
                required = f[4]
                reference3 = f[5]
                default2 = f[6]
                constraint2 = f[7]
                table = f[8]
                stable = table
                onsave = f[9]
                #
                cv_test = input.get(col)
                cv = ''
                if cv_test and hasattr(cv_test, 'strip'):
                    cv = cv_test.strip()
            except Exception, e:
                sess[SKF_RUN] = [ [_['e_form_insert_general'], str(e)] ]
                raise web.seeother('/form/run/%s' %(form))
            #
            if required == 1 and not cv:
                ecols.append(col)
                errors.append( [ _['e_form_run_required'], label] )
            #
            if onsave:
                try:
                    onsaver = db.query(
                                    onsave,
                                    vars = {FORM_ONSAVE_SQL_VALUE: cv}
                                ).list()
                    cv = onsaver[0][FORM_ONSAVE_SQL_RET]
                except Exception, e:
                    ecols.append(col)
                    errors.append( [ _['e_form_run_onsave'], label, str(e)] )                    
            #            
            if constraint2:
                try:
                    constf = constraint2[0].strip()
                    consta = constraint2[1]
                    constc = constraint2[2]
                    conste = constraint2[3].strip()
                    #
                    if not conste:
                        constm = [
                                    _['e_form_run_constraint'], 
                                    label, 
                                    constf, 
                                    constc
                                ]
                    else:
                        constm = [
                                    _['e_form_run_constraint'],
                                    label,
                                    conste,
                                ]
                    #
                    if (consta == 1) or hasws(cv):
                        cvq = web.sqlquote(cv)
                    else:
                        if cv:
                            cvq = cv
                        else:
                            cvq = 0
                    #
                    if constf:
                        constq = 'select %s(%s) %s as c' %(constf, cvq, constc)
                    else:
                        constq = 'select %s %s as c' %(cvq, constc)
                    #
                    constr = db.query(constq).list()
                    if constr[0]['c'] != 1:
                        ecols.append(col)
                        errors.append(constm)
                except:
                    ecols.append(col)
                    errors.append( [ _['e_form_run_constraint'], label] )
            #
            if ftype in BLOB_TYPE:
                cvv = db.db_module.Binary(cv)
            elif nqtype(ftype) and not hasws(cv):
                cvv = cv
            else:
                cvv = cv #nqtype above is no longer needed
            ocols[col] = cvv
            #
        #
        if not stable:
            dflt()
        #
        #subform
        fsub_table = ''
        fsub_all2 = []
        fsub_ref = ''
        try:
            fsub_all = {}
            fsub_rows = 0
            fsub_req = 0
            fsub_info = ''
            if fsub:
                fsub_table = fsub[0]
                fsub_ref = fsub[1]
                fsub_rows = fsub[2][0]
                fsub_req = fsub[2][1]
                fsub_info = fsub[4]
                for f in fsub[3]:
                    fsub_col = f[0]
                    fsub_k = '%s.%s' %(fsub_table, fsub_col)
                    fsub_i = web.webapi.rawinput().get(fsub_k)
                    if not isinstance(fsub_i, list): 
                        fsub_i = [fsub_i]
                    fsub_all[fsub_col] = fsub_i
            #
            fsub_keys = fsub_all.keys()
            for i in range(fsub_rows):
                fsub_t = {}
                try:
                    for k in fsub_keys:
                        fsub_t[k] = fsub_all[k][i]
                        if not fsub_t[k] or not fsub_t[k].strip(): 
                            fsub_t = {}
                            break
                except:
                    fsub_t = {}
                if fsub_t.keys():
                    fsub_all2.append(fsub_t)
            #
            if len(fsub_all2) < fsub_req:
                fsub_all2 = []
                raise Exception, '%s %s %s %s' %(
                        fsub_info,
                        fsub_req,
                        _['x_row'],
                        _['x_required']
                        )
        except Exception, e:
            errors.append( [ _['e_form_run_subform'], str(e)] )
        #        
        if errors:
            sess[SKF_RUN] = errors
        else:
            form_trans = db.transaction()
            #
            try:
                okeys = ocols.keys()
                okeys2 = ['$'+x for x in okeys]
                q = 'insert into %s(%s) values(%s)' %(
                        table,
                        ','.join(okeys),
                        ','.join(okeys2),
                    )
                form_res = db.query(q, vars=ocols)
                #
                form_last = db.query('select last_insert_rowid() as x')[0]['x']
                #
                #subform save
                if (fsub_table in tables()) and (fsub_all2) and (fsub_ref in columns(fsub_table, True)):
                    for f in fsub_all2:
                        f[fsub_ref] = form_last
                        fkeys = f.keys()
                        fkeys2 = ['$'+x for x in fkeys]
                        fq = 'insert into %s(%s) values(%s)' %(
                                fsub_table,
                                ','.join(fkeys),
                                ','.join(fkeys2)
                            )
                        db.query(fq, f)
                #
                #custom SQL (sql2)
                ocols['last_insert_rowid'] = form_last
                if fsql2 and type(fsql2) == type([]):
                    for fsql in fsql2:
                        if fsql and hasattr(fsql, 'strip'):
                            if fsql.strip():
                                db.query(fsql, vars=ocols)
                #
                #custom message
                message3 = _['o_form_run']
                if message2 and len(message2) == FORM_MESSAGE_LEN:
                    message2b = ''
                    if form_res < 0:
                        message2b = message2[0]
                    elif form_res == 0:
                        message2b = message2[1]
                    elif form_res > 0:
                        message2b = message2[2]
                    message2b = str(message2b)
                    message3 = message2b.replace(FORM_MESSAGE_VAR_RESULT, 
                        str(form_res))
                #
                sess[SKF_RUN] = [ [message3] ]
            except Exception, e:
                form_trans.rollback()
                sess[SKF_RUN] = [ [_['e_form_insert_general'], str(e)] ]
                raise web.seeother('/form/run/%s' %(form))
            else:
                form_trans.commit()
        #
        raise web.seeother('/form/run/%s' %(form))
        

class form_edit:
    def GET(self):
        start()
        input = web.input(name='', code='', mode='', form='')
        name = input.name
        code = input.code
        code = urllib.unquote(code)
        mode = input.mode
        form = input.form
        #
        dform = ''
        title = _['tt_form_edit']
        if mode == MODE_INSERT:
            title = _['tt_form_create']
        else:
            #
            if not form.strip():
                dflt()
            #
            dform = form
            #
            fo = s_select('form.code..%s' %(form))
            if not fo:
                dflt()
            #
            fo = fo[0]
            if not name:
                name = fo['d']
            if not code:
                code = fo['e']
        #
        data = {
                'title': title,
                'command': 'form.edit',
                'action_url': '/form/edit',
                'action_method': 'post',
                'action_button': (
                                    ('save', _['cmd_save'], False, '', 'submit'),
                                ),
                'input': (
                            (web.form.Textbox('name', value=name), _['x_form_name']),
                            (web.form.Textarea('code', value=code, 
                                    cols=DEFAULT_TEXTAREA_COLS*2, 
                                    rows=DEFAULT_TEXTAREA_ROWS
                                ), _['x_code']),
                        ),
                'form': dform,
                'message': smsgq(SKF_CREATE, default=''),
                'hint': _['h_form_create'],
            }
        #
        if mode == MODE_INSERT:
            data['hidden'] = (('mode', mode),)
        else:
            data['hidden'] = (('form', form),)
        #
        content = ''
        #
        stop()
        return T(data, content)
    
    def POST(self):
        input = web.input(name='', code='', mode='', form='')
        name = input.name.lower().strip()
        code = input.code.strip()
        mode = input.mode.strip()
        form = input.form.lower().strip()
        #
        xform = ''
        if mode == MODE_INSERT:
            if not validfname(name):
                sess[SKF_CREATE] = [[_['e_form_edit_name']]]
                raise web.seeother('/form/edit?name=%s&code=%s&mode=%s' %(
                        name, urllib.quote(code), MODE_INSERT))
            #
            if hasws(name):
                sess[SKF_CREATE] = [[_['e_form_edit_whitespace']]]
                raise web.seeother('/form/edit?name=%s&code=%s&mode=%s' %(
                        name, urllib.quote(code), MODE_INSERT))
            #
            if not name or not code:
                raise web.seeother('/form/edit?name=%s&code=%s&mode=%s' %(
                        name, urllib.quote(code), MODE_INSERT))
            #
            all = s_select('form.code')
            allf = [x['d'] for x in all]
            if name in allf:
                sess[SKF_CREATE] = [[_['e_form_edit_exists']]]
                raise web.seeother('/form/edit?name=%s&code=%s&mode=%s' %(
                        name, urllib.quote(code), MODE_INSERT))
            #
            ocode = code
            try:
                xform = name
                code = json.loads(code)
                code = json.dumps(code)
                db.insert(FORM_TBL, a='form', b='code', d=name, e=ocode)
            except Exception, e:
                sess[SKF_CREATE] = [[_['e_form_edit_syntax'], str(e)]]
                raise web.seeother('/form/edit?name=%s&code=%s&mode=%s' %(
                        name, urllib.quote(ocode), MODE_INSERT))
        else:
            if not validfname(name):
                sess[SKF_CREATE] = [[_['e_form_edit_name']]]
                raise web.seeother('/form/edit?name=%s&code=%s&form=%s' %(
                        name, urllib.quote(code), form))
            #
            if hasws(name):
                sess[SKF_CREATE] = [[_['e_form_edit_whitespace']]]
                raise web.seeother('/form/edit?name=%s&code=%s&form=%s' %(
                        name, urllib.quote(code), form))
            #
            if not name or not code:
                raise web.seeother('/form/edit?name=%s&code=%s&form=%s' %(
                        name, urllib.quote(code), form))
            #
            all = s_select('form.code')
            allf = [x['d'] for x in all]
            if (name != form) and (name in allf):
                sess[SKF_CREATE] = [[_['e_form_edit_exists']]]
                raise web.seeother('/form/edit?name=%s&code=%s&form=%s' %(
                        name, urllib.quote(code), form))
            #
            ocode = code
            try:
                xform = form
                if form != name:
                    xform = name
                code = json.loads(code)
                code = json.dumps(code)
                db.update(FORM_TBL, where='a=$a and b=$b and d=$d',
                    vars={'a': 'form', 'b': 'code', 'd': form}, d=name, e=ocode)
            except Exception, e:
                sess[SKF_CREATE] = [[_['e_form_edit_syntax'], str(e)]]
                raise web.seeother('/form/edit?name=%s&code=%s&form=%s' %(
                        name, urllib.quote(ocode), form))
        #
        if xform:
            raise web.seeother('/?form=%s' %(xform))
        #
        dflt()


class report_action:
    def GET(self):
        input = web.input()
        if not input.has_key('report'):
            dflt()
        #
        report = input.report.strip()
        redir = (
            ('run', '/report/run/' + report),
            ('edit', '/report/edit?report=' + report),
            ('create', '/report/edit?mode=' + MODE_INSERT),
        )
        for i in redir:
            if input.has_key(i[0]):
                raise web.seeother(i[1])
        #
        dflt()


class report_edit:
    def GET(self):
        start()
        input = web.input(name='', code='', mode='', report='')
        name = input.name
        code = input.code
        code = urllib.unquote(code)
        mode = input.mode
        report = input.report
        #
        dreport = ''
        title = _['tt_report_edit']
        if mode == MODE_INSERT:
            title = _['tt_report_create']
        else:
            #
            if not report.strip():
                dflt()
            #
            dreport = report
            #
            fo = s_select('report.code..%s' %(report))
            if not fo:
                dflt()
            #
            fo = fo[0]
            if not name:
                name = fo['d']
            if not code:
                code = fo['e']
        #
        data = {
                'title': title,
                'command': 'report.edit',
                'action_url': '/report/edit',
                'action_method': 'post',
                'action_button': (
                                    ('save', _['cmd_save'], False, '', 'submit'),
                                ),
                'input': (
                            (web.form.Textbox('name', value=name), _['x_report_name']),
                            (web.form.Textarea('code', value=code, 
                                    cols=DEFAULT_TEXTAREA_COLS*2, 
                                    rows=DEFAULT_TEXTAREA_ROWS
                                ), _['x_code']),
                        ),
                'report': dreport,
                'message': smsgq(SKR_CREATE, default=''),
                'hint': _['h_report_create'],
            }
        #
        if mode == MODE_INSERT:
            data['hidden'] = (('mode', mode),)
        else:
            data['hidden'] = (('report', report),)
        #
        content = ''
        #
        stop()
        return T(data, content)
    
    def POST(self):
        input = web.input(name='', code='', mode='', report='')
        name = input.name.lower().strip()
        code = input.code.strip()
        mode = input.mode.strip()
        report = input.report.lower().strip()
        #
        xreport = ''
        if mode == MODE_INSERT:
            if not validfname(name):
                sess[SKR_CREATE] = [[_['e_report_edit_name']]]
                raise web.seeother('/report/edit?name=%s&code=%s&mode=%s' %(
                        name, urllib.quote(code), MODE_INSERT))
            #
            if hasws(name):
                sess[SKR_CREATE] = [[_['e_report_edit_whitespace']]]
                raise web.seeother('/report/edit?name=%s&code=%s&mode=%s' %(
                        name, urllib.quote(code), MODE_INSERT))
            #
            if not name or not code:
                raise web.seeother('/report/edit?name=%s&code=%s&mode=%s' %(
                        name, urllib.quote(code), MODE_INSERT))
            #
            all = s_select('report.code')
            allf = [x['d'] for x in all]
            if name in allf:
                sess[SKR_CREATE] = [[_['e_report_edit_exists']]]
                raise web.seeother('/report/edit?name=%s&code=%s&mode=%s' %(
                        name, urllib.quote(code), MODE_INSERT))
            #
            ocode = code
            try:
                xreport = name
                code = json.loads(code)
                code = json.dumps(code)
                db.insert(FORM_TBL, a='report', b='code', d=name, e=ocode)
            except Exception, e:
                sess[SKR_CREATE] = [[_['e_report_edit_syntax'], str(e)]]
                raise web.seeother('/report/edit?name=%s&code=%s&mode=%s' %(
                        name, urllib.quote(ocode), MODE_INSERT))
        else:
            if not validfname(name):
                sess[SKR_CREATE] = [[_['e_report_edit_name']]]
                raise web.seeother('/report/edit?name=%s&code=%s&report=%s' %(
                        name, urllib.quote(code), report))
            #
            if hasws(name):
                sess[SKR_CREATE] = [[_['e_report_edit_whitespace']]]
                raise web.seeother('/report/edit?name=%s&code=%s&report=%s' %(
                        name, urllib.quote(code), report))
            #
            if not name or not code:
                raise web.seeother('/report/edit?name=%s&code=%s&report=%s' %(
                        name, urllib.quote(code), report))
            #
            all = s_select('report.code')
            allf = [x['d'] for x in all]
            if (name != report) and (name in allf):
                sess[SKR_CREATE] = [[_['e_report_edit_exists']]]
                raise web.seeother('/report/edit?name=%s&code=%s&report=%s' %(
                        name, urllib.quote(code), report))
            #
            ocode = code
            try:
                xreport = report
                if report != name:
                    xreport = name
                code = json.loads(code)
                code = json.dumps(code)
                db.update(FORM_TBL, where='a=$a and b=$b and d=$d',
                    vars={'a': 'report', 'b': 'code', 'd': report}, d=name, e=ocode)
            except Exception, e:
                sess[SKR_CREATE] = [[_['e_report_edit_syntax'], str(e)]]
                raise web.seeother('/report/edit?name=%s&code=%s&report=%s' %(
                        name, urllib.quote(ocode), report))
        #
        if xreport:
            raise web.seeother('/?report=%s' %(xreport))
        #
        dflt()
        
        
class report_run:
    def GET(self, report):
        start()
        #
        if not report.strip() or not report.strip() in reports():
            dflt()
        #
        if not canreport(REPORT_KEY_SECURITY_RUN, report):
            dflt()
        #
        if not validfname(report):
            dflt()
        #
        input = ()
        action_button = (
                            ('report', _['cmd_report'], False, '', 'submit'),
                        )
        ftitle = ''
        finfo = ''
        if not reqreport(report):
            input = ()
            action_button = ()
            sess[SKR_RUN] = [
                                [_['e_report_run_syntax_or_required']],
                            ]
        else:
            try:
                preport = parsereport(report)
            except:
                preport = [ftitle, finfo, input]
            #
            ftitle = preport[0]
            finfo = preport[1]
            input = preport[2]
        #
        message = smsgq(SKR_RUN, default=[])
        #
        data = {
                'title': '%s - %s' %(_['tt_report_run'], report), 
                'command': 'report.run',
                'report': report,
                'message': message,
                'input': input,
                'hidden': (('hreport', report),),
                'action_url': '/report/run/%s' %(report),
                'action_method': 'post',
                'action_enctype': 'multipart/form-data',
                'action_button': action_button,
                'hint': _['h_report_run'],
                'ftitle': ftitle,
                'finfo': finfo,
                'blob_type': BLOB_TYPE,
                'text_type': TEXT_TYPE,
                }
        content = ''
        stop()
        return T(data, content)
        
    def POST(self, unused):
        input = web.input(hreport='')
        report = input.hreport.strip()
        #
        if not report:
            dflt()
        #
        if not canreport(REPORT_KEY_SECURITY_RUN, report):
            dflt()
        #
        if not validfname(report):
            dflt()
        #
        freport = report
        finput = None
        rquery = None
        rheader = []
        message2 = []
        try:
            preport = parsereport(report)
            freport = preport[0]
            finput = preport[2]
            rquery = preport[3]
            rheader = preport[4]
            message2 = preport[5]
        except:
            preport = None
        #
        if not preport or not finput:
            dflt()
        #
        start()
        #
        errors = []
        ecols = []
        ocols = {}
        rreport = []
        rsearch = []
        #
        for f in finput:
            try:
                label = f[0] 
                key = f[1]
                readonly = f[2]
                required = f[3]
                reference3 = f[4]
                default2 = f[5]
                constraint2 = f[6]
                type2 = f[7]
                #
                cv_test = input.get(key)
                cv = ''
                if cv_test and hasattr(cv_test, 'strip'):
                    cv = cv_test.strip()
            except Exception, e:
                sess[SKR_RUN] = [ [_['e_report_select_general'], str(e)] ]
                raise web.seeother('/report/run/%s' %(report))
            #
            if required == 1 and not cv:
                ecols.append(key)
                errors.append( [ _['e_report_run_required'], label] )
            #
            if constraint2:
                try:
                    constf = constraint2[0].strip()
                    consta = constraint2[1]
                    constc = constraint2[2]
                    conste = constraint2[3].strip()
                    #
                    if not conste:
                        constm = [
                                    _['e_report_run_constraint'], 
                                    label, 
                                    constf, 
                                    constc
                                ]
                    else:
                        constm = [
                                    _['e_report_run_constraint'],
                                    label,
                                    conste,
                                ]
                    #
                    if (consta == 1) or hasws(cv):
                        cvq = web.sqlquote(cv)
                    else:
                        if cv:
                            cvq = cv
                        else:
                            cvq = 0
                    #
                    if constf:
                        constq = 'select %s(%s) %s as c' %(constf, cvq, constc)
                    else:
                        constq = 'select %s %s as c' %(cvq, constc)
                    #
                    constr = db.query(constq).list()
                    if constr[0]['c'] != 1:
                        ecols.append(key)
                        errors.append(constm)
                except:
                    ecols.append(key)
                    errors.append( [ _['e_report_run_constraint'], label] )
            #
            if (cv) and (not hasws(cv)) and (type2 == 'integer'):
                try:
                    cvv = int(cv)
                except:
                    cvv = 0
            else:
                cvv = cv
            #
            ocols[key] = cvv
            #
            rsearch.append( [label, cvv] )
            #
        #
        if errors:
            sess[SKR_RUN] = errors
            raise web.seeother('/report/run/%s' %(report))
        else:
            try:
                rreport = db.query(rquery, vars=ocols)
            except Exception, e:
                sess[SKR_RUN] = [ [_['e_report_select_general'], str(e)] ]
                raise web.seeother('/report/run/%s' %(report))
        #
        data = {
                'title': '%s - %s' %(_['tt_report_run_result'], report), 
                'command': 'report.run.result',
                'report': report,
                'header': rheader,
                'search': rsearch,
                'report2': freport,
                }
        content = rreport
        #
        xtable = hasattr(content, '__iter__')
        data['table'] = xtable
        #
        message3 = ''
        message2b = ''
        if xtable == False:
            try:
                if content < 0:
                    message2b = message2[0]
                elif content == 0:
                    message2b = message2[1]
                elif content > 0:
                    message2b = message2[2]
                #
                message3 = message2b.replace(REPORT_MESSAGE_VAR_RESULT, 
                    str(content))
            except:
                pass
        data['result_message'] = message3
        #
        stop()
        #
        return T(data, content)


class notes:
    def GET(self):
        start()
        #
        xaction = ()
        if isadmin():
            xaction = (
                        (_['cmd_query_src'], '/query?src=notes&sid='),
                    )
        #
        data = {
                'title': _['tt_notes'],
                'command': 'notes',
                'action_url': '/notes',
                'action_method': 'post',
                'action_button': (
                                    ('save', _['cmd_save'], False, '', 'submit'),
                                ),
                'columns': (
                            _['x_delete'], 
                            _['x_title'], 
                            _['x_content'], 
                            _['x_action'],
                        ),
                'select': 'select',
                'select_all': _['x_delete'],
                'max': 3,
                'xaction': xaction,
                'message': smsgq(SK_NOTES),
                'hint': _['h_notes'],
            }
        #
        q = 'my.notes.%s' %(user())
        content = s_select(q)
        #
        stop()
        return T(data, content)
    
    def POST(self):
        inp = web.input(select=[], d=[], e=[], f=[])
        select = inp.select
        d = inp.d
        e = inp.e
        f = inp.f
        msg = []
        #
        updated = 0
        #
        #delete
        allx = s_select('my.notes.%s' %(user()))
        alld = [x['d'] for x in allx]
        for i in range(len(d)):
            di = d[i]
            ei = e[i]
            fi = f[i]
            if (di in alld) and (not di in select):
                if not ei.strip() and not fi.strip():
                    select.append(di)       
        for s in select:
            if s in alld:
                try:
                    db.delete(FORM_TBL, 
                        where='a=$a and b=$b and c=$c and d=$d', 
                        vars={
                            'a': 'my', 
                            'b': 'notes', 
                            'c': user(), 
                            'd': s
                        }
                    )
                    sev = ()
                    for a in allx:
                        if a['d'] == s:
                            sev = [
                                        a['e'].strip(),
                                        a['f'].strip(),
                                    ]
                            break
                    se = get_value1(sev, s)
                    m = (_['x_deleted'], se)
                    msg.append(m)
                except:
                    pass
        #update
        allx = s_select('my.notes.%s' %(user()))
        alld = [x['d'] for x in allx]
        for i in range(len(d)):
            di = d[i]
            ei = e[i]
            fi = f[i]
            if (di in alld) and (not di in select) and (ei.strip() or fi.strip()):
                try:
                    db.update(FORM_TBL, where='a=$a and b=$b and c=$c and d=$d',
                        e=ei,
                        f=fi,
                        vars = {
                            'a': 'my', 
                            'b': 'notes', 
                            'c': user(),
                            'd': di
                        }
                    )
                    updated += 1
                except:
                    pass
        #new
        allx = s_select('my.notes.%s' %(user()))
        alld = [x['d'] for x in allx]
        for i in range(len(e)):
            dn = gen_d(alld)
            di = d[i]
            ei = e[i]
            fi = f[i]
            #
            if (dn) and (not di) and (not dn in select) and (ei.strip() or fi.strip()):
                try:
                    db.insert(FORM_TBL, a='my', b='notes', c=user(),  
                        d=dn, e=ei, f=fi
                    )
                    ex = get_value1([ei.strip(), fi.strip()], dn)
                    m = (_['x_added'], ex)
                    msg.append(m)
                except:
                    pass
        #
        if updated:
            m = (_['o_notes'],)
            msg.append(m)
        #
        sess[SK_NOTES] = msg
        raise web.seeother('/notes')


#----------------------------------------------------------------------#
# MAIN                                                                 #
#----------------------------------------------------------------------#
if __name__ == '__main__':
    log(TITLE)
    log(APP_DESC)
    log('')
    #
    wtest = ()
    #
    if len(sys.argv) < 2:
        log('%s %s' %(sys.argv[0], _['usage']))
        #
        wtest = fdialog_open()
        if not wtest:
            sys.exit(1)
    #
    if wtest:
        dbfile0 = wtest[0]
        dbfile = wtest[1]        
    else:
        dbfile0 = sys.argv[1]
        dbfile = os.path.abspath(dbfile0)
    #
    try:
        port = int(sys.argv[2])
    except:
        port = DEFAULT_PORT
    #
    try:
        db = web.database(
                dbn=DBN, 
                db=dbfile, 
                check_same_thread=CHECK_SAME_THREAD
            )
        db.select(DEFAULT_TABLE)
    except:
        log('%s %s' %(_['e_connect'], dbfile), stream=sys.stderr)
        sys.exit(2)
    #
    log(dbfile)
    #
    app = web.application(URLS, globals())
    app.notfound = notfound
    #
    sess = web.session.Session(app, MemSession(), initializer = sess_init)
    prepsess()
    #
    app.add_processor(proc_access)
    app.add_processor(proc_admin_check)
    app.add_processor(proc_login)
    app.add_processor(proc_nosb)
    app.add_processor(proc_udf)
    app.add_processor(proc_misc)
    #
    web.httpserver.runsimple(app.wsgifunc(), (DEFAULT_ADDR, port))
    
