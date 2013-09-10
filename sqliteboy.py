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
# - bare except:
# - PEP8 violations :)
#


#----------------------------------------------------------------------#
# APPLICATION                                                          #
#----------------------------------------------------------------------#
NAME = 'sqliteboy'
APP_DESC = 'Simple Web SQLite Manager/Form/Report Application'
VERSION = '1.31'
WSITE = 'https://github.com/nopri/%s' %(NAME)
TITLE = NAME + ' ' + VERSION
DBN = 'sqlite'
CHECK_SAME_THREAD=False
FORM_TBL = '_sqliteboy_'
FORM_URL_INIT = '/sqliteboy/init'
FORM_FIELDS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
FORM_FIELDS_R1 = ['rowid', 'rowtime']
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
DEFAULT_PY_HANDLER = '%s_user' %(NAME)
DEFAULT_PY_FORM = 'form_'
DEFAULT_PY_REPORT = 'report_'
DEFAULT_ADMIN_USER = 'admin'
DEFAULT_ADMIN_PASSWORD = DEFAULT_ADMIN_USER
DEFAULT_HOSTS_ALLOWED = ['127.0.0.1']
DEFAULT_TEXTAREA_COLS = 40
DEFAULT_TEXTAREA_ROWS = 15
DEFAULT_ERROR_INT = -1
DEFAULT_ERROR_STR = ''
DEFAULT_WIN_EXE = '%s.exe' %(NAME)
DEFAULT_WIN_EXE_VERSION = '%s.version' %(DEFAULT_WIN_EXE)
DEFAULT_WIN_MD5 = '%s.md5' %(DEFAULT_WIN_EXE)
DEFAULT_FAVICON = '%s.ico' %(NAME)
DEFAULT_SPEC = '%s.spec' %(NAME)
DEFAULT_VERSION = '%s.version' %(NAME)
DEFAULT_WEBPY_STATIC = ['static']
DEFAULT_QUERY_EXPORT = 'query.csv'
DEFAULT_VAR_MAX = 3
APPLICATION_TITLE_MAX = 32
BROWSE_LIMIT_ALL = [10, 25, DEFAULT_LIMIT, 100, 250, 500, 1000]
SEQUENCE_TABLE = 'sqlite_sequence'
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
SKT_M_COPY = 'copy'
SKT_M_EMPTY = 'empty'
SKT_M_IMPORT = 'import'
SKQ = 'query'
SKV = 'vacuum'
SK_CREATE = 'create'
SK_LOGIN = 'login'
SK_PASSWORD = 'password'
SK_NOTES = 'notes'
SK_FILES = 'files'
SK_PAGES = 'pages'
SK_CALCULATOR = 'calculator'
SK_USERS = 'users'
SK_HOSTS = 'hosts'
SK_SYSTEM = 'system'
SK_SCRIPTS = 'scripts'
SK_SCRIPT = 'script'
SK_PROFILE = 'profile'
SK_SCHEMA = 'schema'
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
COLUMN_CONVERT = {
                    'integer': 'sqliteboy_as_integer',
                    'real': 'sqliteboy_as_float',
                    'char': 'sqliteboy_strs',
                    'varchar': 'sqliteboy_strs',
                    'text': 'sqliteboy_strs',
                    'blob': 'sqliteboy_strs',
                }
COLUMN_CONVERT_DEFAULT = 'sqliteboy_strs'
MAX_COLUMN_ADD = 3
CUSTOM_RT = {
                'query': 4,
                'calculator': 3,
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
FORM_KEY_INSERT = 'insert'
FORM_KEY_CONFIRM = 'confirm'
FORM_REQ = (FORM_KEY_DATA,)
FORM_REQ_X = (2,) #parsed index
FORM_REQ_DATA = (FORM_KEY_DATA_TABLE, 
                    FORM_KEY_DATA_COLUMN,
                )
FORM_REFERENCE_SQL_0 = 'a'
FORM_REFERENCE_SQL_1 = 'b'
FORM_ONSAVE_SQL_VALUE = 'value'
FORM_ONSAVE_SQL_RET = 'onsave'
FORM_SUB_ROWS_DEFAULT = [5, 1]#rows, required rows
FORM_MESSAGE_LEN = 3
FORM_MESSAGE_VAR_RESULT = 'result'
FORM_MESSAGE_VAR_PYTHON_HANDLER = 'python_handler'
FORM_INSERT_DEFAULT = 1
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
REPORT_KEY_HEADERS = 'headers'
REPORT_KEY_FOOTERS = 'footers'
REPORT_KEY_PAPER = 'paper'
REPORT_KEY_MARGINS = 'margins'
REPORT_KEY_CONFIRM = 'confirm'
REPORT_REQ = (REPORT_KEY_DATA,
                REPORT_KEY_SQL,
            )
REPORT_REQ_X = (3,) #parsed index
REPORT_REQ_DATA = (REPORT_KEY_DATA_KEY,)
REPORT_REFERENCE_SQL_0 = 'a'
REPORT_REFERENCE_SQL_1 = 'b'
REPORT_MESSAGE_LEN = 3
REPORT_MESSAGE_VAR_RESULT = 'result'
REPORT_HEADERS_CELL_LEN = 3
REPORT_FOOTERS_CELL_LEN = 3
REPORT_HEADERS_CELL_TYPES = [
                                (str, unicode, ), 
                                (str, unicode, int, ),
                                (dict, ),
                            ]
REPORT_FOOTERS_CELL_TYPES = REPORT_HEADERS_CELL_TYPES
REPORT_CELL_TYPE_TEXT = ''
REPORT_CELL_TYPE_FILES_IMAGE = 'files.image'
REPORT_CELL_TYPE_SQL = 'sql'
REPORT_CELL_TYPE_SQL_RESULT = REPORT_REFERENCE_SQL_0
REPORT_RESULT_ROW_COUNT = 'result_row_count'
REPORT_RESULT_MESSAGE = 'result_message'
REPORT_FORMAT_DEFAULT = ''
REPORT_FORMAT_CSV = 'csv'
REPORT_FORMAT_PDF = 'pdf'
REPORT_FORMAT_ALL = [
                        REPORT_FORMAT_DEFAULT,
                        REPORT_FORMAT_CSV,
                        REPORT_FORMAT_PDF,
                    ]
REFERENCE_FLAG_PASSWORD = 2
FAVICON_WIDTH = 16
FAVICON_HEIGHT = 16
PYTIME_FORMAT = '%Y-%m-%d %H:%M:%S'
PYTIME_FORMAT_BACKUP = '%Y-%m-%d_%H-%M-%S'
REGEX_EMAIL = r'^[\w\.\+-]+@[\w\.-]+\.[a-zA-Z]+$'
DAYS_IN_YEAR = 365.2425
DAYS_IN_MONTH_AVERAGE = round( (DAYS_IN_YEAR / float(12)), 2)
DAYS_IN_MONTH_30 = 30
DAYS_IN_MONTH_31 = 31
CSV_SUFFIX = '.csv'
CSV_CTYPE = 'text/csv'
BACKUP_BUFFER = 10 * SIZE_KB
FILES_MAX_NUMBER = 10
FILES_MAX_SIZE = 1 * SIZE_MB
SCRIPTS_MAX_SIZE = 32 * SIZE_KB
SYSTEM_CONFIG_MAXSPLIT = 3
SYSTEM_CONFIG = (
                    (
                        'x_application',
                        'x_application_title',
                        'application.title.',
                        'application.title..%s' %(''),
                        '',
                        'striphtml',
                        0,
                    ),                    
                    (
                        'x_files',
                        'x_max_files_number',
                        'files.max_number.',
                        'files.max_number..%s' %(FILES_MAX_NUMBER),
                        FILES_MAX_NUMBER,
                        int,
                        0,
                    ),
                    (
                        'x_files',
                        'x_max_file_size',
                        'files.max_size.',
                        'files.max_size..%s' %(FILES_MAX_SIZE),
                        FILES_MAX_SIZE,
                        int,
                        0,
                    ),
                    (
                        'x_scripts',
                        'x_max_script_size',
                        'scripts.max_size.',
                        'scripts.max_size..%s' %(SCRIPTS_MAX_SIZE),
                        SCRIPTS_MAX_SIZE,
                        int,
                        0,
                    ),
                    (
                        'x_users',
                        'x_user_defined_profile',
                        'users.profile.',
                        'users.profile..%s' %(''),
                        '',
                        str,
                        1,
                    ),
                    (
                        'x_messages',
                        'x_messages_all',
                        'messages.all.',
                        'messages.all..%s' %(''),
                        '',
                        'striphtml',
                        1,
                    ),                    
                )
NOTFOUND_CHECK = [
                    '/fs',
                ]
REGEX_PAGE = (
                (
                    r'~([^~]+)~', 
                    r'<em>\1</em>',
                    True,
                    '~text~ -> <em>text</em>',
                ),
                (
                    r'\*([^\*]+)\*', 
                    r'<strong>\1</strong>',
                    True,
                    '*text* -> <strong>text</strong>',
                ),
                (
                    r'_([^_]+)_', 
                    r'<u>\1</u>',
                    True,
                    '_text_ -> <u>text</u>',
                ),
                (
                    r'\[([^\|]+)\|(\S+)\]', 
                    r'<a href="\2">\1</a>',
                    True,
                    '[text|url] -> <a href="url">text</a>',
                ),
            )
SAMPLE_PAGE = ', '.join([x[3] for x in REGEX_PAGE])
CALCULATOR_MAX_INPUT = 36
CALCULATOR_ALLOWED = ''
PLAIN_CTYPE = 'text/plain'
SCRIPT_KEY_NAME = 'name'
SCRIPT_KEY_INFO = 'info'
SCRIPT_KEY_AUTHOR = 'author'
SCRIPT_KEY_LICENSE = 'license'
SCRIPT_KEY_TABLES = 'tables'
SCRIPT_KEY_FORMS = 'forms'
SCRIPT_KEY_REPORTS = 'reports'
SCRIPT_KEY_PROFILES = 'profiles'
SCRIPT_REQ = (
                SCRIPT_KEY_NAME,
                SCRIPT_KEY_TABLES,
                SCRIPT_KEY_FORMS,
                SCRIPT_KEY_REPORTS,
            )
SCRIPT_TABLE_COLUMN_LEN = 3
SCRIPT_TABLE_ERROR = -1
SCRIPT_TABLE_COLUMN_CONFLICT = -2
SCRIPT_TABLE_OK = 0
SCRIPT_TABLE_EXISTS = 1
SCRIPT_FORM_ERROR = -1
SCRIPT_FORM_OK = 0
SCRIPT_FORM_EXISTS = -2
SCRIPT_REPORT_ERROR = -1
SCRIPT_REPORT_OK = 0
SCRIPT_REPORT_EXISTS = -2
SCRIPT_VALID_COLUMN_FLAG = (
                            ([], 0, ''), #none
                            ([], 1, ''), #primary key
                            (['integer'], 2, 'primary key autoincrement'), 
                        )
JSON_INDENT = 4
COPY_TARGET_EXCLUDE = [
                    FORM_TBL,
                    DEFAULT_TABLE,
                    SEQUENCE_TABLE,
            ]
EMPTY_EXCLUDE = [
                    FORM_TBL,
                    DEFAULT_TABLE,
                    SEQUENCE_TABLE,
            ]            
IMPORT_EXCLUDE = [
                    FORM_TBL,
                    DEFAULT_TABLE,
                    SEQUENCE_TABLE,
            ]            
PRAGMA_FREELIST_COUNT = 'freelist_count'
SERVER_COMMAND_SEPARATOR = '-'
SERVER_COMMAND_ALL = {
                        'generate_favicon': 'scmd_favicon',
                        'generate_pyinstaller': 'scmd_pyinstaller',
                        'generate_build': 'scmd_build',    
                        'generate_version': 'scmd_version',    
                    }
SHORTCUT_TYPE_FORM = 'form'
SHORTCUT_TYPE_REPORT = 'report'
SHORTCUT_ALL = [
                    SHORTCUT_TYPE_FORM,
                    SHORTCUT_TYPE_REPORT,
                ]
PRINT_DATA_KEY = 'output_printer'
PRINT_DATA_VALUE = 1
IMPORT_ERROR_CODE = 255

PYINSTALLER_SPEC = '''
# $title $command
# $datetime

a = Analysis([r'$source_path'])

a.datas += [
            ('$source', r'$source_path', 'DATA'),
            ('$readme', r'$readme_path', 'DATA'),
        ]

pyz = PYZ(a.pure)

exe = EXE(
            pyz, 
            a.scripts, 
            a.binaries, 
            a.datas, 
            name=r'$output',
            icon=r'$icon',
            console=True,
            debug=False
        )

#
import sys
import os 
try: 
   from hashlib import md5
except ImportError:
   from md5 import md5

#
content_version = """
$title $command
$datetime
"""
file_version = open(r'$output_version', 'w')
file_version.write(content_version)
file_version.close()

#
content = open(r'$output', 'rb').read()
content_md5 = md5(content).hexdigest()
content_lines = [
            '%s  %s' %(content_md5, r'$output'),
        ]
file_md5 = open(r'$output_md5', 'w')
for i in content_lines:
    line = '%s' %(i)
    file_md5.write(line)
file_md5.close()

#
try:
    content_check = open(r'$output_md5', 'r').readlines()
    content_check = [x.strip() for x in content_check if not x.startswith('#')]
    content_check = [x for x in content_check if x]
    content_check_md5 = content_check[0].split()[0].strip()
    if content_check_md5 == content_md5:
        sys.stdout.write('OK' + os.linesep)
except:
    pass
    

'''

VERSION_SPEC = '''
$title $command
$datetime
'''

PROFILE_STYLE_PRINT = '''
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
                                    border          : 1px solid #000000;
                                    padding         : 2px;
                                }
                                th
                                {
                                    border          : 1px solid #000000;
                                    padding         : 2px;
                                }
                                select
                                {
                                    width           : 95%;
                                }
                                .main_menu
                                {
                                    display         : none;
                                }                                
                                .messages
                                {
                                    display         : none;
                                }                                
                    '''
PROFILE_ITEM_STYLE = [
                        [
                            PROFILE_STYLE_PRINT,
                            '''
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
                                    border          : 1px solid #808080;
                                    padding         : 2px;
                                }
                                th
                                {
                                    background-color: #406080;
                                    border          : 1px solid #808080;
                                    padding         : 2px;
                                    color           : #ffffff;
                                }
                                th a
                                {
                                    color           : #ffffff;
                                    text-decoration : none;
                                }
                                tr:nth-child(odd)
                                {
                                    background-color: #cccccc;
                                }
                                tr:nth-child(even)
                                {
                                    background-color: #ffffff;
                                }
                                select
                                {
                                    width           : 95%;
                                }
                                .main_menu
                                {
                                }                            
                                a
                                {
                                    color           : #406080;                                
                                }
                                .messages
                                {
                                    padding         : 2px;
                                    background-color: #cccccc;
                                    border          : 1px solid #808080;
                                }                                
                            '''
                        ],
                        [
                            PROFILE_STYLE_PRINT,
                            '''
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
                                    border          : 1px solid #ffcc66;
                                    padding         : 2px;
                                }
                                th
                                {
                                    background-color: #996600;
                                    border          : 1px solid #ffcc66;
                                    padding         : 2px;
                                    color           : #ffffff;
                                }
                                th a
                                {
                                    color           : #ffffff;
                                    text-decoration : none;
                                }
                                tr:nth-child(odd)
                                {
                                    background-color: #f3e3c3;
                                }
                                tr:nth-child(even)
                                {
                                    background-color: #ffffff;
                                }
                                select
                                {
                                    width           : 95%;
                                }
                                .main_menu
                                {
                                }                            
                                input, select, textarea
                                {
                                    background-color: #ffffff;
                                    color           : #996600;
                                    border          : 1px solid #ffcc66;
                                    margin          : 2px;
                                }
                                a
                                {
                                    color           : #996600;                                
                                }
                                .messages
                                {
                                    padding         : 2px;
                                    background-color: #f3e3c3;
                                    border          : 1px solid #ffcc66;
                                }                                
                            '''
                        ],
                        [
                            PROFILE_STYLE_PRINT,
                            '''
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
                                    border          : 1px solid #4169e1;
                                    padding         : 2px;
                                }
                                th
                                {
                                    background-color: #00008b;
                                    border          : 1px solid #4169e1;
                                    padding         : 2px;
                                    color           : #ffffff;
                                }
                                th a
                                {
                                    color           : #ffffff;
                                    text-decoration : none;
                                }
                                tr:nth-child(odd)
                                {
                                    background-color: #b0e0e6;
                                }
                                tr:nth-child(even)
                                {
                                    background-color: #ffffff;
                                }
                                select
                                {
                                    width           : 95%;
                                }
                                .main_menu
                                {
                                }                            
                                a
                                {
                                    color           : #00008b;                                
                                }
                                .messages
                                {
                                    padding         : 2px;
                                    background-color: #b0e0e6;
                                    border          : 1px solid #4169e1;
                                }                                
                            '''
                        ],
                    ]
PROFILE_ALL = [
                [
                    'style',
                    'x_style',
                    [
                        [0, 'A'],
                        [1, 'B'],
                        [2, 'C'],
                    ],
                    2,
                    'pr_style',
                    int,
                    0,
                ],
            ]
PROFILE_USER_DEFINED_LEN = 4
PROFILE_USER_DEFINED_HANDLER = 'pr_user'
PROFILE_USER_DEFINED_TYPE = str
PROFILE_USER_DEFINED_LEVEL = 1
ENV_VAR_MAX = DEFAULT_VAR_MAX
QUERY_STRING_MAX = 1 * SIZE_KB
PDF_CTYPE = 'application/pdf'
PDF_SUFFIX = '.pdf'


#----------------------------------------------------------------------#
# MODULE                                                               #
#----------------------------------------------------------------------#
import sys
import os
if getattr(sys, 'frozen', None):
    CURDIR = sys._MEIPASS
    CWDIR = os.getcwd()
    SCURDIR = CWDIR
else:
    CURDIR = os.path.dirname(__file__)
    CWDIR = CURDIR
    SCURDIR = os.getcwd()

for i in [CWDIR, SCURDIR]:
    if not i in sys.path:
        sys.path.append(i)

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)

import time
import decimal
import random
import string
FORM_VALID = [x for x in string.ascii_lowercase] + [x for x in string.digits]
FORM_VALID.append('_')
CALCULATOR_ALLOWED = string.digits + '.-+*/()'

import socket
try:
    DEFAULT_HOSTS_ALLOWED.append(socket.gethostbyname(socket.gethostname()))
except:
    pass

try: 
   from hashlib import md5
except ImportError:
   from md5 import md5

import urllib
import hashlib
import base64

import platform
import struct

import re

import csv

try:
    import cStringIO
except ImportError:
    import StringIO as cStringIO

from HTMLParser import HTMLParser

import calendar

import copy

try:
    import reportlab
    from reportlab.lib.colors import black as PDF_DEFAULT_BORDER_COLOR
    from reportlab.lib.styles import getSampleStyleSheet as PDF_STYLE_SHEET
    from reportlab.platypus import SimpleDocTemplate as PDF_TEMPLATE
    from reportlab.platypus import Table as PDF_TABLE
    from reportlab.platypus import Image as PDF_IMAGE
    from reportlab.platypus import Spacer as PDF_SPACER
    from reportlab.platypus import Paragraph as PDF_PARAGRAPH
    from reportlab.lib.pagesizes import A4 as PDF_DEFAULT_PAGE_SIZE
    from reportlab.lib.units import inch as PDF_UNIT_INCH
    #
    PDF_DEFAULT_BORDER_STYLE = [
                                    (
                                        'GRID', 
                                        (0, 0), 
                                        (-1, -1), 
                                        1, 
                                        PDF_DEFAULT_BORDER_COLOR,
                                    ),
                                ]
    PDF_DEFAULT_SPACER_WIDTH = 1
    PDF_DEFAULT_SPACER_HEIGHT = 36
    PDF_DEFAULT_PARAGRAPH_STYLE = PDF_STYLE_SHEET()['BodyText']
except ImportError:
    reportlab = None

if reportlab:
    try:
        from reportlab.pdfbase import _fontdata_enc_winansi
        from reportlab.pdfbase import _fontdata_enc_macroman
        from reportlab.pdfbase import _fontdata_enc_standard
        from reportlab.pdfbase import _fontdata_enc_symbol
        from reportlab.pdfbase import _fontdata_enc_zapfdingbats
        from reportlab.pdfbase import _fontdata_enc_pdfdoc
        from reportlab.pdfbase import _fontdata_enc_macexpert
        from reportlab.pdfbase import _fontdata_widths_courier
        from reportlab.pdfbase import _fontdata_widths_courierbold
        from reportlab.pdfbase import _fontdata_widths_courieroblique
        from reportlab.pdfbase import _fontdata_widths_courierboldoblique
        from reportlab.pdfbase import _fontdata_widths_helvetica
        from reportlab.pdfbase import _fontdata_widths_helveticabold
        from reportlab.pdfbase import _fontdata_widths_helveticaoblique
        from reportlab.pdfbase import _fontdata_widths_helveticaboldoblique
        from reportlab.pdfbase import _fontdata_widths_timesroman
        from reportlab.pdfbase import _fontdata_widths_timesbold
        from reportlab.pdfbase import _fontdata_widths_timesitalic
        from reportlab.pdfbase import _fontdata_widths_timesbolditalic
        from reportlab.pdfbase import _fontdata_widths_symbol
        from reportlab.pdfbase import _fontdata_widths_zapfdingbats        
    except:
        pass

try:
    import sqlite3    
    
    import json

    import web
    web.config.debug = False
    
except Exception, e:
    lsep = os.linesep
    emsg = '%s%s%s%s%s%s%s' %(
                TITLE,
                lsep,
                APP_DESC,
                lsep,
                lsep,
                str(e),
                lsep
            )
    sys.stderr.write(emsg)
    sys.exit(IMPORT_ERROR_CODE)


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
    '/table/empty', 'table_empty',
    '/table/drop', 'table_drop',
    '/table/export/csv', 'table_export_csv',
    '/table/import/csv', 'table_import_csv',
    '/table/schema', 'table_schema',
    '/table/copy', 'table_copy',
    '/table/create', 'table_create',
    '/query', 'query',
    '/vacuum', 'vacuum',
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
    '/admin/system', 'admin_system',
    '/admin/backup', 'admin_backup',
    '/form/action', 'form_action',
    '/form/run/(.*)', 'form_run',
    '/form/shortcut/(.*)', 'form_shortcut',
    '/form/edit', 'form_edit',
    '/report/action', 'report_action',
    '/report/run/(.*)', 'report_run',
    '/report/shortcut/(.*)', 'report_shortcut',
    '/report/edit', 'report_edit',
    '/notes', 'notes',
    '/files', 'files',
    '/fs', 'fs',
    '/pages', 'pages',
    '/page/(.*)', 'page',
    '/calculator', 'calculator',
    '/admin/scripts', 'admin_scripts',
    '/admin/script/(.*)', 'admin_script',
    '/profile', 'profile',
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
        'var': {},
        'table': {},
        'user': '',
        'admin': 0,
    }


#----------------------------------------------------------------------#
# STRIPHTMLPARSER                                                      #
#----------------------------------------------------------------------#
class StripHTMLParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.text = []
    
    def handle_data(self, data):
        self.text.append(data)


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
# NUMBER TO WORDS                                                      #
#----------------------------------------------------------------------#
NUMBER_TO_WORDS = {}

class NumberToWords:
    def __init__(self):
        self.word = {}
        self.name1 = {}
        self.name2 = {}
        self.sign = {}
        self.replace = {}
        self.style = {}
        self.data = {}
        #
        self.chunk_size = 3
        
    def maxlength(self):
        ret = 0
        #
        ln1 = len(self.name1.keys())
        #
        if ln1:
            ret = ( ( 2 * ln1 ) - 1) * self.chunk_size
        #
        return ret
        
    def separator(self):
        return self.style.get('separator', ' ')
        
    def decimal_separator(self):
        return self.style.get('decimal_separator', ' ')
    
    def is_number(self, s, check_length=True):
        s = str(s)
        #
        ret = False
        #
        if check_length:
            if len(s) > self.maxlength():
                return False
        #
        try:
            test = float(s)
            ret = True
        except:
            pass
        #
        return ret
    
    def is_negative(self, s):
        ret = False
        #
        try:
            test = float(s)
            if test < 0:
                ret = True
        except:
            pass
        #
        return ret
        
    def split(self, s):
        s = str(s).lower()
        #
        ret = ()
        #
        if not self.is_number(s, False):
            return ret
        #
        if 'e' in s:
            return ret
        #    
        P1 = ''
        P2 = ''
        if '.' in s:
            P1, P2 = s.split('.')
        else:
            P1 = s
        P1 = P1.strip()
        P2 = P2.strip()
        #
        P1 = P1.replace('+', '')
        P1 = P1.replace('-', '')
        #
        if not self.is_number(P1):
            return ret
        #
        ret = (P1, P2)
        return ret

    def chunk(self, s):
        s = str(s)
        #
        n = self.chunk_size
        #
        mod = len(s) % n
        if mod:
            ln = len(s) + (n - mod)
            s = s.rjust(ln, ' ')
        #
        ret = [s[i:i+n] for i in range(0, len(s), n)]
        ret = [s.strip() for s in ret]
        #
        return ret

    def get_single(self, s):
        s = str(s)
        #
        res = []
        #
        for i in s:
            x = self.word.get(i, '')
            if x and i == '0':
                x = x[0]
            res.append(x)
        #
        ret = self.separator().join(res)
        return ret
    
    def get_1d(self, s):
        s = str(s)
        #
        ret = ''
        #
        if not len(s) == 1: 
            return ret
        #
        r = self.word.get(s, '')
        if r and s == '0':
            r = r[1]
        #
        ret = r
        return ret    

    def get_2d(self, s):
        '''
        override this
        '''
        s = str(s)
        #        
        ret = ''
        #
        if not len(s) == 2: 
            return ret
        #
        return ret    

    def get_3d(self, s):
        '''
        override this
        '''        
        s = str(s)
        #        
        ret = ''
        #
        if not len(s) == 3: 
            return ret
        #
        return ret    

    def get_d(self, s):
        s = str(s)
        #        
        ls = len(s)
        #
        ret = ''
        #
        if ls == 1:
            ret = self.get_1d(s)
        elif ls == 2:
            ret = self.get_2d(s)
        elif ls == 3:
            ret = self.get_3d(s)
        #
        return ret        
        
    def get_x1(self, c, s, separator):
        '''
        override this if needed
        '''        
        s = str(s)
        separator = str(separator)
        #
        ret = (s, separator)
        return ret
        
    def get_p1(self, p):
        p = str(p)
        #
        nk = self.name1.keys()
        mx = max(nk)
        mxt = ''
        if self.is_number(p) and long(p) > 0:
            mxt = self.name1.get(mx, '')
        #
        lp1 = self.chunk(p)
        if len(lp1) > mx:
            ret = [
                        lp1[:-mx],
                        mxt,
                        lp1[-mx:],
                    ]
        else:
            ret = [ 
                        lp1, 
                    ]
        #
        return ret
    
    def words_p1(self, p):
        ret = []
        #
        if not isinstance(p, list):
            p = []
        #
        p = reversed(p)
        for rp in p:
            if isinstance(rp, str):
                ret.append(rp)
                continue
            #
            rp = reversed(rp)
            c = 0
            for i in rp:
                rsep = self.separator()
                #
                r = self.get_d(i).strip()
                r, rsep = self.get_x1(c, r, rsep)
                #
                x = self.name1.get(c, '')
                if not int(i) == 0:
                    if not r or not x:
                        rsep = ''
                    z = rsep.join([r, x])
                    ret.append(z)
                c += 1
        #
        return ret
        
    def words_p2(self, p):
        p = str(p)
        #
        return self.get_single(p)
        
    def get_words(self, s):
        ret = ''
        #
        neg = self.is_negative(s)
        #
        parts = self.split(s)
        if not parts and len(parts) != 2:
            return ret
        #
        p1 = parts[0]
        p2 = parts[1]
        #
        c1 = self.get_p1(p1)
        w1 = self.words_p1(c1)
        w2 = self.words_p2(p2)
        #
        r1 = reversed(w1)
        ss = self.sign.get(neg, '')
        sr = self.separator().join(r1)
        if not sr.strip():
            sr = self.get_single('0')
        #
        z1 = self.separator().join([ss, sr])
        z1 = z1.strip()
        #
        if w2:
            ret = self.decimal_separator().join([z1, w2])
        else:
            ret = z1
        #
        return ret


class NumberToWordsId(NumberToWords):
    def __init__(self):
        NumberToWords.__init__(self)
        #
        self.word = {
                        '0': ('nol', ''),
                        '1': 'satu',
                        '2': 'dua',
                        '3': 'tiga',
                        '4': 'empat',
                        '5': 'lima',
                        '6': 'enam',
                        '7': 'tujuh',
                        '8': 'delapan',
                        '9': 'sembilan',
                        '10': 'sepuluh',
                        '11': 'sebelas',
                    }
        #
        self.name1 = {
                        0: '',
                        1: 'ribu',
                        2: 'juta',
                        3: 'milyar',
                        4: 'triliun',        
                    }
        #
        self.name2 = {
                        1: '',
                        2: ('belas', 'puluh'),
                        3: ('ratus', 'seratus'),        
                    }
        #
        self.sign = {
                        True: 'min',
                        False: '',        
                    }
        #
        self.replace = {
                        1: ('satu', 'se'),
                    }
        #
        self.style = {
                        'separator': ' ', 
                        'decimal_separator': ' koma ',
                    }
        #

    def get_2d(self, s):
        s = str(s)
        #
        ret = ''
        if not len(s) == 2: 
            return ret
        #
        res = []
        rn = ''
        r = self.word.get(s, '')
        #
        if r:
            res = [r]
        else:
            res2 = []
            rx = self.name2.get(2, ())
            if s[0] == '1':
                rn = rx[0]
                r = self.get_1d(s[1])
                res2 = [r, '']
            elif s[0] == '0':
                rn = ''
                r = self.get_1d(s[1])
                res2 = [r, '']
            else:
                rn = rx[1]
                for i in s:
                    r = self.get_1d(i)
                    res2.append(r)
            res = []
            res.append(res2[0])
            res.append(rn)
            res.append(res2[1])
        #
        ret = self.separator().join(res)
        return ret

    def get_3d(self, s):
        s = str(s)
        #
        ret = ''
        if not len(s) == 3: 
            return ret
        #
        res = []
        rn = ''
        r = self.word.get(s, '')
        #
        if r:
            res = [r]
        else:
            res2 = []
            rx = self.name2.get(3, ())
            if s[0] == '1':
                rn = rx[1]
                r = self.get_2d(s[1:])
                res2 = [rn , r]
            elif s[0] == '0':
                rn = ''
                r = self.get_2d(s[1:])
                res2 = [r, rn]
            else:
                rn = rx[0]
                r1 = self.get_1d(s[0])
                r2 = self.get_2d(s[1:])
                res2 = [r1, rn, r2]
            res = [self.separator().join(res2)]
        #
        ret = self.separator().join(res)
        return ret
        
    def get_x1(self, c, s, separator):
        for k in self.replace.keys():
            if c == k:
                xk = self.replace.get(k)
                if s == xk[0]:
                    s = xk[1]
                    separator = ''
                    break
        #
        return [s, separator]


class NumberToWordsEn1(NumberToWords):
    def __init__(self):
        NumberToWords.__init__(self)
        #
        self.word = {
                        '0': ('zero', ''),
                        '1': 'one',
                        '2': 'two',
                        '3': 'three',
                        '4': 'four',
                        '5': 'five',
                        '6': 'six',
                        '7': 'seven',
                        '8': 'eight',
                        '9': 'nine',
                        '10': 'ten',
                        '11': 'eleven',
                        '12': 'twelve',
                        '13': 'thirteen',
                        '15': 'fifteen',
                        '18': 'eighteen',
                        '20': 'twenty',
                        '30': 'thirty',
                        '40': 'forty',
                        '50': 'fifty',
                        '60': 'sixty',
                        '70': 'seventy',
                        '80': 'eighty',
                        '90': 'ninety',
                    }
        #
        self.name1 = {
                        0: '',
                        1: 'thousand',
                        2: 'million',
                        3: 'billion',
                        4: 'trillion',        
                    }
        #
        self.name2 = {
                        1: '',
                        2: ('teen', 'ty'),
                        3: 'hundred',
                    }
        #
        self.sign = {
                        True: 'minus',
                        False: '',        
                    }
        #
        self.replace = {}
        #
        self.style = {
                        'separator': ' ', 
                        'decimal_separator': ' point ',
                        'dash_separator': '-',
                    }
        #

    def get_2d(self, s):
        s = str(s)
        #
        ret = ''
        if not len(s) == 2: 
            return ret
        #
        res = []
        rn = ''
        r = self.word.get(s, '')
        #
        if r:
            res = [r]
        else:
            rx = self.name2.get(2, ())
            if s[0] == '1':
                rn = rx[0]
                r = self.get_1d(s[1])
                res = [r, rn]
                ret = ''.join(res)
            elif s[0] == '0':
                rn = ''
                r = self.get_1d(s[1])
                res = [r, '']
            else:
                rn = self.word.get(s[0] + '0')
                r = self.get_1d(s[1])
                res = []
                res.append(rn)
                res.append(self.style.get('dash_separator', ''))
                res.append(r)
                ret = ''.join(res)
        #
        if not ret:
            ret = self.separator().join(res)
        return ret

    def get_3d(self, s):
        s = str(s)
        #
        ret = ''
        if not len(s) == 3: 
            return ret
        #
        res = []
        rn = ''
        r = self.word.get(s, '')
        #
        if r:
            res = [r]
        else:
            res2 = []
            if s[0] == '0':
                rn = ''
                r = self.get_2d(s[1:])
                res2 = [r, rn]
            else:
                rn = self.name2.get(3, '')
                r1 = self.get_1d(s[0])
                r2 = self.get_2d(s[1:])
                res2 = [r1, rn, r2]
            res = [self.separator().join(res2)]
        #
        ret = self.separator().join(res)
        return ret


NUMBER_TO_WORDS['id'] = NumberToWordsId
NUMBER_TO_WORDS['en1'] = NumberToWordsEn1
    

#----------------------------------------------------------------------#
# SIMPLEDROPDOWN                                                       #
#----------------------------------------------------------------------#
class SimpleDropdown(web.form.Dropdown):
    def __init__(self, name, args, *validators, **attrs):
        self.args = args
        super(SimpleDropdown, self).__init__(name, args, *validators, **attrs)
    
    def _render_option(self, arg, indent='  '):
        if isinstance(arg, (tuple, list)):
            value, desc= arg
        else:
            value, desc = arg, arg 

        #lines below are modified by sqliteboy author: 
        #- convert to str
        #- web.net 
        if str(self.value) == str(value) or (isinstance(self.value, list) and value in self.value):
            select_p = ' selected="selected"'
        else:
            select_p = ''
        return indent + '<option%s value="%s">%s</option>\n' % (select_p, web.net.websafe(value), web.net.websafe(desc))
    

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
            'x_page': 'page',
            'x_next': 'next',
            'x_previous': 'previous',
            'x_unlimited': 'unlimited',
            'x_selected': 'selected',
            'x_default': 'default',
            'x_name': 'name',
            'x_type': 'type',
            'x_primary_key': 'primary key',
            'x_optional': 'optional',
            'x_rename': 'rename to',
            'x_empty': 'empty',
            'x_column_number': 'number of column',
            'x_column': 'column(s)',
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
            'x_reportlab_version': 'ReportLab version',
            'x_extended_features': 'extended features',
            'x_user': 'user',
            'x_users': 'users',
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
            'x_key': 'key',
            'x_value': 'value',
            'x_section': 'section',
            'x_files': 'files',
            'x_max_files_number': 'maximum number of files per user',
            'x_max_files_number_error': 'maximum number of files per user exceeded',
            'x_max_file_size': 'maximum file size',
            'x_max_file_size_error': 'maximum file size exceeded',
            'x_file_name': 'file name',
            'x_file_size': 'size',
            'x_database_size': 'size of database file',
            'x_unused_pages': 'number of unused pages',
            'x_shared': 'shared',
            'x_preview': 'preview',
            'x_expression_too_long': 'expression too long',
            'x_expression_invalid': 'invalid expression',            
            'x_info': 'info',
            'x_author': 'author',
            'x_license': 'license',        
            'x_run_time': 'run (time)',
            'x_scripts': 'scripts',
            'x_max_script_size': 'maximum script size',
            'x_detail': 'detail',
            'x_system_check': 'system check',
            'x_table_exists': 'table already exists, however, additional column(s) will be added',
            'x_script_not_runnable': 'could not run this script because nothing is defined, or error(s) found, or has been run before',
            'x_copy_to': 'to',
            'x_copy_from': 'from',
            'x_copy_columns_none': 'no identical column found',
            'x_sqliteboy_x_update': 'updating %s table, please wait...' %(FORM_TBL),
            'x_sqliteboy_x_update_files': 'updating %s table (files), please wait...' %(FORM_TBL),
            'x_please_wait': 'please wait...',
            'x_server_command_mode': 'server command mode',
            'x_style': 'style',
            'x_user_defined_profile': 'user-defined profile', 
            'x_profile': 'profile',
            'x_create_table_schema': 'create table based on this schema',
            'x_messages': 'messages',
            'x_messages_all': 'for all users',
            'x_application': 'application',
            'x_application_title': 'title (maximum %s characters)' %(APPLICATION_TITLE_MAX),
            'x_not_avail_pdf': 'not available, PDF output will be disabled',
            'tt_insert': 'insert',
            'tt_edit': 'edit',
            'tt_column': 'column',
            'tt_rename': 'rename',
            'tt_empty': 'empty',
            'tt_drop': 'drop',
            'tt_query': 'query',
            'tt_create': 'create',
            'tt_readme': 'readme',
            'tt_source': 'source',
            'tt_login': 'login',
            'tt_password': 'password',
            'tt_users': 'users',
            'tt_hosts': 'hosts',
            'tt_system': 'system',
            'tt_form_run': 'form run',
            'tt_form_edit': 'form edit',
            'tt_form_create': 'form create',
            'tt_report_run': 'report run',
            'tt_report_edit': 'report edit',
            'tt_report_create': 'report create',
            'tt_report_run_result': 'report run (result)',
            'tt_notes': 'notes',
            'tt_files': 'files',
            'tt_pages': 'page',
            'tt_calculator': 'calculator',
            'tt_scripts': 'scripts',
            'tt_script': 'script',
            'tt_import_csv': 'import',
            'th_error': 'ERROR',
            'th_ok': 'OK',
            'tt_copy': 'copy',
            'tt_vacuum': 'vacuum',
            'tt_profile': 'profile',
            'tt_schema': 'schema',
            'cmd_browse': 'browse',
            'cmd_insert': 'insert',
            'cmd_column': 'column',
            'cmd_rename': 'rename',
            'cmd_table_empty': 'empty',
            'cmd_table_drop': 'drop',
            'cmd_export_csv': 'export',
            'cmd_import_csv': 'import',
            'cmd_copy': 'copy',
            'cmd_table_create': 'create',
            'cmd_query': 'query',
            'cmd_query_export_csv': 'query (export)',
            'cmd_query_src': 'query',
            'cmd_delete_selected': 'delete selected',
            'cmd_edit_selected': 'edit selected',
            'cmd_clear_selected': 'clear selected',
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
            'cmd_files': 'files',
            'cmd_pages': 'page',
            'cmd_calculator': 'calculator',
            'cmd_calculate': 'calculate',
            'cmd_users': 'users',
            'cmd_hosts': 'hosts',
            'cmd_system': 'system',
            'cmd_backup': 'backup',
            'cmd_save': 'save',
            'cmd_run': 'run',
            'cmd_form_create': 'create',
            'cmd_report_create': 'create',
            'cmd_report': 'report',
            'cmd_view': 'view',
            'cmd_use_result': 'use the result',
            'cmd_scripts': 'scripts',
            'cmd_vacuum': 'vacuum',
            'cmd_go': 'go',
            'cmd_go_print': 'go (print)',
            'cmd_csv': 'csv',
            'cmd_pdf': 'pdf',
            'cmd_shortcut': 'shortcut',
            'cmd_profile': 'profile',
            'cmd_schema': 'schema',
            'cmd_hide': 'hide',
            'cmd_show': 'show',
            'cf_delete_selected': 'are you sure you want to delete selected row(s)?',
            'cf_drop': 'confirm drop table',
            'cf_empty': 'confirm empty table',
            'cf_vacuum': 'confirm vacuum database',
            'e_db_static': 'ERROR: database file must not be placed in static directory',
            'e_notfound': 'ERROR 404: the page you are looking for is not found',
            'e_access_forbidden': 'access forbidden',
            'e_connect': 'ERROR: unable to connect to',
            'e_insert': 'ERROR: insert into table',
            'e_edit': 'ERROR: update table',
            'e_rename': 'ERROR: alter table (rename)',
            'e_empty': 'ERROR: empty table',
            'e_drop': 'ERROR: drop table',
            'e_table_exists': 'ERROR: table already exists',
            'e_open_file': 'ERROR: open file',
            'e_login': 'ERROR: unknown user or incorrect password',
            'e_password_general': 'ERROR: could not change password',
            'e_password_auth': 'ERROR: authentication failed',
            'e_password_mismatch': 'ERROR: passwords mismatch',
            'e_password_blank': 'ERROR: please enter new password',
            'e_hosts': 'ERROR: could not update hosts',
            'e_system': 'ERROR: could not update system configuration',
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
            'e_scripts_max_size': 'ERROR: maximum script size exceeded',
            'e_scripts_syntax_or_required' : 'ERROR: script code error or required keys are not set',
            'e_scripts_name': 'ERROR: invalid script name',
            'e_script_column_conflict': 'ERROR: table already exists and conflicted column(s) found',
            'e_script': 'ERROR: script run',
            'e_copy': 'ERROR: copy table',
            'e_import_csv': 'ERROR: import csv',
            'e_profile': 'ERROR: could not update profile',
            'o_insert': 'OK: insert into table',
            'o_edit': 'OK: update table',
            'o_column': 'OK: alter table (column)',
            'o_rename': 'OK: alter table (rename)',
            'o_password': 'OK: password changed',
            'o_hosts': 'OK: hosts updated',
            'o_system': 'OK: system configuration updated',
            'o_form_run': 'OK: form run',
            'o_form_create': 'OK: create form',
            'o_report_create': 'OK: create report',
            'o_notes': 'OK: notes updated',
            'o_files': 'OK: files updated',
            'o_pages': 'OK: page updated',
            'o_scripts': 'OK: scripts updated',
            'o_script': 'OK: script run',
            'o_table_create': 'OK: create table',
            'o_drop': 'OK: drop table',
            'o_copy': 'OK: copy table',
            'o_empty': 'OK: empty table',
            'o_vacuum': 'OK: vacuum database',
            'o_import_csv': 'OK: import csv',
            'o_profile': 'OK: profile updated',
            'o_profile_set': 'OK: profile set',
            'h_insert': 'hint: leave blank to use default value (if any)',
            'h_edit': 'hint: for blob field, leave blank = do not update',
            'h_column': 'hint: only add column is supported in SQLite. Primary key/unique is not allowed in column addition. Default value(s) must be constant.',
            'h_rename': '',
            'h_empty': '',
            'h_drop': '',
            'h_query': 'hint: only one statement at a time is supported',
            'h_create': 'hint: please do not put whitespace in table name',
            'h_create2': 'hint: for multiple primary keys, do not select type contains "primary key", use primary key column instead. For date/time type, please use integer. If date/time default is needed, please use current_time, current_date or current_timestamp. To use non-constant literally, please surround with quote(\'), for example \'current_time\'.',
            'h_users': 'hint: only valid value(s) will be updated. You could not delete yourself or update your admin level. New username must be unique, must not contain whitespace and will be lowercased.',
            'h_hosts': 'hint: for custom hosts, please use whitespace separated format',
            'h_system': '',
            'h_form_create': 'hint: please do not put whitespace in form name. Form name must be alphanumeric/underscore and will be converted to lowercase. Form code in JSON format. Please read <a href="%s">README</a> for form code reference.' %(URL_README[0]),
            'h_form_run': '',
            'h_report_create': 'hint: please do not put whitespace in report name. Report name must be alphanumeric/underscore and will be converted to lowercase. Report code in JSON format. Please read <a href="%s">README</a> for report code reference.' %(URL_README[0]),
            'h_report_run': '',
            'h_notes': '',
            'h_files': '',
            'h_pages': 'hint: HTML tags will be stripped on page save. Please read <a href="%s">README</a> for page code reference. For example: %s' %(URL_README[0], web.htmlquote(SAMPLE_PAGE)),
            'h_calculator': 'hint: valid characters: %s. Maximum length: %s.' %(CALCULATOR_ALLOWED, CALCULATOR_MAX_INPUT),
            'h_scripts': 'hint: script code in JSON format. Please read <a href="%s">README</a> for script code reference.' %(URL_README[0]),
            'h_script': 'hint: only valid value(s) will be read. Script could not be run if there is error. Backup before running a script is recommended.',
            'h_copy': 'hint: copy content of source table to existing destination table (insert), only for identical column(s) (name and type)',
            'h_vacuum': 'hint: vacuum command will rebuild the entire database and may reduce the size of database file. Please make sure there is enough free space, at least twice the size of the original database file. This command may change the rowids of rows in any tables that do not have an explicit integer primary key column.',
            'h_import_csv': 'hint: import CSV file (Excel dialect) into table (insert). First row will be read as column(s).',
            'h_profile': '',
            'z_table_whitespace': 'could not handle table with whitespace in name',
            'z_view_blob': '[blob data]',
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
    s = str(s)
    #
    ret = 0
    #
    try:
        ret = int(s)
        if abs(ret) > sys.maxint:
            ret = 0
        else:
            ret = int(ret)
    except:
        pass
    #
    return ret
SQLITE_UDF.append(('sqliteboy_as_integer', 1, sqliteboy_as_integer))

def sqliteboy_as_float(s):
    s = str(s)
    #
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

def sqliteboy_is_datetime(s):
    ret = 0
    #
    try:
        s = s.strip()
        p = time.strptime(s, PYTIME_FORMAT)
        ret = 1
    except:
        pass
    #
    return ret
SQLITE_UDF.append(('sqliteboy_is_datetime', 1, sqliteboy_is_datetime))

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

def sqliteboy_time3a():
    return sqliteboy_time3(sqliteboy_time())
SQLITE_UDF.append(('sqliteboy_time3a', 0, sqliteboy_time3a))

def sqliteboy_time4(f):
    try:
        return time.strftime(PYTIME_FORMAT, time.gmtime(f))
    except:
        return ''
SQLITE_UDF.append(('sqliteboy_time4', 1, sqliteboy_time4))

def sqliteboy_time4a():
    return sqliteboy_time4(sqliteboy_time())
SQLITE_UDF.append(('sqliteboy_time4a', 0, sqliteboy_time4a))

def sqliteboy_time5(s1, s2, mode):
    s1 = str(s1)
    s2 = str(s2)
    if not sqliteboy_is_integer(mode):
        mode = 0
    #
    tnow = sqliteboy_time()
    if not s1.strip() or not sqliteboy_is_datetime(s1):
        s1 = sqliteboy_time3(tnow)
    if not s2.strip() or not sqliteboy_is_datetime(s2):
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

def sqliteboy_time6(f, year, month, day, mode):
    ret = ''
    #
    try:
        f = float(f)
    except:
        return ret
    #
    year = str(year)
    month = str(month)
    day = str(day)
    #
    if not sqliteboy_is_integer(mode) or mode < 0:
        mode = 0
    #
    if 'e' in str(f).lower():
        return ret
    #
    f1, f2 = str(f).split('.')
    try:
        y = int(f1)
    except:
        return ret
    #
    leftm = f - y
    fm = float(leftm * 12) 
    m1, m2 = str(fm).split('.')
    try:
        m = int(round(float(m1), 0))
    except:
        return ret
    #
    leftd = fm - m
    d = int(round(leftd * DAYS_IN_MONTH_AVERAGE, 0))
    d30 = int(round(leftd * DAYS_IN_MONTH_30, 0))
    d31 = int(round(leftd * DAYS_IN_MONTH_31, 0))
    #
    dd = d
    if mode == 1:
        dd = d30
    elif mode == 2:
        dd = d31
    #
    ret = '%s%s%s%s%s%s' %(
            y,
            year,
            m,
            month,
            dd,
            day
        )
    #
    return ret
SQLITE_UDF.append(('sqliteboy_time6', 5, sqliteboy_time6))

def sqliteboy_is_leap(n):
    ret = 0
    #
    if sqliteboy_is_integer(n):
        ret = calendar.isleap(n)
    #
    return ret
SQLITE_UDF.append(('sqliteboy_is_leap', 1, sqliteboy_is_leap))

def sqliteboy_lower(s):
    s = sqliteboy_strs(s)
    return s.lower()
SQLITE_UDF.append(('sqliteboy_lower', 1, sqliteboy_lower))

def sqliteboy_upper(s):
    s = sqliteboy_strs(s)
    return s.upper()
SQLITE_UDF.append(('sqliteboy_upper', 1, sqliteboy_upper))

def sqliteboy_swapcase(s):
    s = str(s)
    return s.swapcase()
SQLITE_UDF.append(('sqliteboy_swapcase', 1, sqliteboy_swapcase))

def sqliteboy_capitalize(s, what):
    s = str(s)
    if not sqliteboy_is_integer(what) or what < 0:
        what = 0
    #
    if what == 0: #first 
        return s.capitalize()
    else:
        return string.capwords(s)
SQLITE_UDF.append(('sqliteboy_capitalize', 2, sqliteboy_capitalize))

def sqliteboy_justify(s, justify, length, padding):
    s = str(s)
    if not sqliteboy_is_integer(justify) or justify < 0:
        justify = 0
    #
    padding = str(padding)
    if padding:
        padding = padding[0]
    else:
        padding = ' '
    #
    ls = len(s)
    if not sqliteboy_is_integer(length) or length < 0 or length < ls:
        length = ls
    #
    ret = s
    #
    if justify == 0: #left
        ret = s.ljust(length, padding)
    elif justify == 1: #right
        ret = s.rjust(length, padding)
    elif justify == 2: #center
        ret = s.center(length, padding)
    #
    return ret
SQLITE_UDF.append(('sqliteboy_justify', 4, sqliteboy_justify))

def sqliteboy_find(s, sub, position, case):
    s = str(s)
    sub = str(sub)
    if not sqliteboy_is_integer(position) or position < 0:
        position = 0
    #
    if not sqliteboy_is_integer(case) or case < 0:
        case = 0
    if not case: #ignore case
        s = s.lower()
        sub = sub.lower()
    #
    ret = -1
    #
    if position == 0: #left
        ret = s.find(sub)
    elif position == 1: #right
        ret = s.rfind(sub)
    #
    return ret
SQLITE_UDF.append(('sqliteboy_find', 4, sqliteboy_find))

def sqliteboy_reverse(s):
    s = str(s)
    #
    return s[::-1]
SQLITE_UDF.append(('sqliteboy_reverse', 1, sqliteboy_reverse))

def sqliteboy_repeat(s, n):
    s = str(s)
    #
    if not sqliteboy_is_integer(n) or n < 1:
        n = 1
    #
    n = abs(n)
    ret = s * n
    return ret
SQLITE_UDF.append(('sqliteboy_repeat', 2, sqliteboy_repeat))

def sqliteboy_count(s, sub, case):
    s = str(s)
    sub = str(sub)
    #
    if not sqliteboy_is_integer(case) or case < 0:
        case = 0
    if not case: #ignore case
        s = s.lower()
        sub = sub.lower()
    #    
    ret = s.count(sub)
    return ret
SQLITE_UDF.append(('sqliteboy_count', 3, sqliteboy_count))

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

def sqliteboy_split0(s, separator, index):
    ret = ''
    #
    s = str(s)
    separator = str(separator)
    #
    if not sqliteboy_is_integer(index):
        return ret
    #
    if not s.strip():
        return ret
    #
    if separator:
        data = s.split(separator)
    else:
        data = s.split()
    #
    try:
        ret = data[index]
    except:
        pass
    #
    return ret
SQLITE_UDF.append(('sqliteboy_split0', 3, sqliteboy_split0))

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

def sqliteboy_number_to_words(s, language):
    ret = ''
    #
    s = str(s)
    language = str(language).lower()
    #
    if not language in NUMBER_TO_WORDS.keys():
        return ret
    #
    oc = NUMBER_TO_WORDS.get(language)
    try:
        oo = oc()
        ret = oo.get_words(s)
    except:
        pass
    #
    return ret
SQLITE_UDF.append(('sqliteboy_number_to_words', 2, sqliteboy_number_to_words))

def sqliteboy_lookup1(table, field, field1, value1, function, distinct):
    ret = ''
    #
    function_all = [
                    'avg',
                    'count',
                    'group_concat',
                    'max',
                    'min',
                    'sum',
                    'total'
            ]
    #
    table = str(table).lower()
    field = str(field).lower()
    field1 = str(field1).lower()
    function = str(function).lower()
    #
    if not table in tables():
        return ret
    cols = columns(table, True)
    if not field1 in cols or not field in cols:
        return ret
    if not function in function_all:
        return ret
    if not sqliteboy_is_number(distinct) or distinct < 0:
        distinct = 0        
    #
    where = [
            '%s=$%s' %(field1, field1), 
            ]
    var = {field1: value1}
    #
    sdistinct = ''
    if distinct:
        sdistinct = ' distinct '
    #
    what_field = '%s(%s %s)' %(function, sdistinct, field)
    #
    try:
        r = db.select(
            table,
            what=what_field,
            where=' and '.join(where),
            vars=var).list()
        ret = r[0][what_field]
    except:
        pass
    #
    if ret: 
        ret = str(ret)
    #
    return ret
SQLITE_UDF.append(('sqliteboy_lookup1', 6, sqliteboy_lookup1))

def sqliteboy_lookup2(table, field, field1, value1, order, default):
    table = str(table).lower()
    field = str(field).lower()
    field1 = str(field1).lower()
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
    table = str(table).lower()
    field = str(field).lower()
    field1 = str(field1).lower()
    field2 = str(field2).lower()
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

def sqliteboy_split1(s, separator, table, column, convert):
    ret = 0
    #
    s = str(s)
    separator = str(separator)
    table = str(table).strip().lower()
    column = str(column).strip().lower()
    if not sqliteboy_is_integer(convert) or convert < 0:
        convert = 0
    #
    if not s.strip():
        return ret
    #
    if not table in tables():
        return ret
    #
    if not column in columns(table, True):
        return ret
    #
    if separator:
        data = s.split(separator)
    else:
        data = s.split()
    if not data:
        return ret
    #
    if hasws(table) or hasws(column):
        return ret
    #
    cols = columnst(table)
    colt = cols.get(column)
    f = COLUMN_CONVERT.get(colt)
    if not f:
        f = COLUMN_CONVERT_DEFAULT
    #
    func = globals().get(f)
    if not callable(func):
        return ret
    #
    count = 0
    t = db.transaction()
    try:
        for d in data:
            if convert:
                x = func(d)
            else:
                x = d
            #
            r = db.query(
                    '''
                        insert into $table ($column) values($data)
                    ''',
                    vars = {
                            'table': web.sqlliteral(table),
                            'column': web.sqlliteral(column),
                            'data': x,
                        }
                )
            if r:
                count += 1
    except:
        return ret
    else:
        t.commit()
        ret = count
    #
    return ret
SQLITE_UDF.append(('sqliteboy_split1', 5, sqliteboy_split1))    

def sqliteboy_list_datetime1(s, n, interval, table, column, local):
    ret = 0
    #
    s = str(s).strip()
    table = str(table).strip().lower()
    column = str(column).strip().lower()
    #
    if not sqliteboy_is_integer(n) or n < 1:
        return ret
    #
    if not sqliteboy_is_integer(interval) or interval == 0:
        return ret
    #
    if not sqliteboy_is_integer(local) or local < 0:
        local = 0
    #
    if not table in tables():
        return ret
    #
    if not column in columns(table, True):
        return ret
    #
    tnow = sqliteboy_time()
    if not s:
        s = sqliteboy_time3(tnow)
    #
    if not sqliteboy_is_datetime(s):
        return ret
    #
    t2 = sqliteboy_time2(s)
    #
    count = 0
    t = db.transaction()
    try:
        for i in range(n):
            if local:
                t3 = sqliteboy_time3(t2)
            else:
                t3 = sqliteboy_time4(t2)
            #
            if not t3:
                continue
            #
            r = db.query(
                    '''
                        insert into $table ($column) values($data)
                    ''', 
                    vars={
                        'table': web.sqlliteral(table),
                        'column': web.sqlliteral(column),
                        'data': t3,
                    }
                )
            if r:
                count += 1
            #
            t2 += interval
    except:
        return ret
    else:
        t.commit()
        ret = count
    #
    return ret
SQLITE_UDF.append(('sqliteboy_list_datetime1', 6, sqliteboy_list_datetime1))

def sqliteboy_http_remote_addr():
    return web.ctx.ip
SQLITE_UDF.append(('sqliteboy_http_remote_addr', 0, sqliteboy_http_remote_addr))

def sqliteboy_http_user_agent():
    return web.ctx.env.get('HTTP_USER_AGENT', '')
SQLITE_UDF.append(('sqliteboy_http_user_agent', 0, sqliteboy_http_user_agent))

def sqliteboy_app_title():
    return TITLE
SQLITE_UDF.append(('sqliteboy_app_title', 0, sqliteboy_app_title))

def sqliteboy_var_set(name, value):
    name = str(name)
    return v_set(name, value)
SQLITE_UDF.append(('sqliteboy_var_set', 2, sqliteboy_var_set))

def sqliteboy_var_get(name):
    name = str(name)
    return v_get(name)
SQLITE_UDF.append(('sqliteboy_var_get', 1, sqliteboy_var_get))

def sqliteboy_var_del(name):
    name = str(name)
    return v_del(name)
SQLITE_UDF.append(('sqliteboy_var_del', 1, sqliteboy_var_del))


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

def s_select(p, string=True, what='*, rowid', order='rowid asc'):
    pr = p.split(FORM_SPLIT)[:len(FORM_FIELDS)]
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
    r = db.select(FORM_TBL, 
                    what=what, 
                    order=order,
                    where = ' and '.join(st), 
                    vars=sd)
    ret = []
    for i in r:
        d = {}
        for k in i.keys(): 
            ik = i[k]
            if string: 
                if ik:
                    ik = str(ik)
                else:
                    ik = ''
            d[k] = ik
        ret.append(d)
    #
    return ret

def s_save(p, last=False, maxsplit=0):
    if maxsplit:
        pr = p.split(FORM_SPLIT, maxsplit)[:len(FORM_FIELDS)]
    else:
        pr = p.split(FORM_SPLIT)[:len(FORM_FIELDS)]
    sf = []
    sv = []
    sd = {}
    st = []
    for i in range(len(pr)):
        fi = FORM_FIELDS[i]
        sf.append(fi)
        #
        pri = pr[i]
        sv.append(pri)
        #
        s = '%s=$%s' %(fi, fi)
        st.append(s)
        sd[fi] = pri        
    #
    ret = False
    #
    if not last:
        pr0 = pr[:-1]
        saved = s_select(FORM_SPLIT.join(pr0))
    else:
        saved = s_select(p)
    #
    try:
        if not saved:
            sv = [str(web.sqlquote(x)) for x in sv]
            q = '''
                insert into %s (%s) values (%s)
            ''' %(
                    FORM_TBL,
                    ','.join(sf),
                    ','.join(sv),
                )
            db.query(q)
        else:
            if len(st) < 2:
                raise Exception
            #
            q = '''
                update %s set %s where %s
            ''' %(
                    FORM_TBL,
                    st[-1],
                    ' and '.join(st[:-1]),
                )
            db.query(q, vars=sd)
        #
        ret = True
    except:
        pass
    #
    return ret
    
def s_check(p, value):
    if not s_select(p):
        s_save(value)
    #
    ret = None
    try:
        ret = s_select(p)
        ret = ret[0]
    except:
        pass
    #
    return ret 
    
def s_check2(p, default):
    value = FORM_SPLIT.join([p, str(default)])
    return s_check(p, value)

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
            if path.startswith('/vacuum') or path.startswith('/query') or path.startswith('/table') or path.startswith('/admin') or path.startswith('/form/edit') or path.startswith('/report/edit'):
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
        #
        if sess.user:
            sess.user = ''
        #
        if path.startswith('/login') or  \
            path.startswith('/logout') or \
            path.startswith('/password') or \
            path.startswith('/form') or \
            path.startswith('/report') or \
            path.startswith('/notes') or \
            path.startswith('/files') or \
            path.startswith('/fs') or \
            path.startswith('/pages') or \
            path.startswith('/page') or \
            path.startswith('/calculator') or \
            path.startswith('/profile') or \
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

def proc_account_check(handle):
    if not isnosb():
        a = s_select('user.account')
        if not a:
            db.insert(FORM_TBL, 
                a='user', 
                b='account', 
                d=DEFAULT_ADMIN_USER, 
                e=md5(DEFAULT_ADMIN_PASSWORD).hexdigest(), 
                f='1'
            )
    #
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
    url = web.url().lower()
    #
    if not url in NOTFOUND_CHECK:
        dflt()
    #
    start()
    data = {
                'title': _['th_error'],
                'command': 'error_404',
                'message': _['e_notfound'],
            }
    content = ''
    stop()
    return web.notfound(T(data, content))

def dflt():
    raise web.seeother('/')

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
    
def size(s=None):
    if s is None:
        s = os.path.getsize(dbfile)
    #
    try:
        s = float(s)
    except:
        s = 0.0
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
            what='lower(name) as name',
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
            ret.append(i.name.lower())
        else:
            d = {}
            for k in i.keys(): d[k.lower()] = i[k]
            ret.append(d)
    #
    return ret

def columnst(table):
    ret = {}
    #
    cols = columns(table)
    if not cols:
        return ret
    #
    for k in cols:
        kn = k.get('name', '')
        kt = k.get('type', '')
        kn = str(kn).strip().lower()
        kt = str(kt).strip().lower()
        if kn and kt:
            ret[kn] = kt
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
    ret = [str(x).lower() for x in ret]
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
                    ['browse/%s' %(DEFAULT_LIMIT), _['cmd_browse']],
                    ['insert', _['cmd_insert']],
                    ['column', _['cmd_column']],
                    ['rename', _['cmd_rename']],
                    ['table_empty', _['cmd_table_empty']],
                    ['table_drop', _['cmd_table_drop']],
                    ['export_csv', _['cmd_export_csv']],
                    ['import_csv', _['cmd_import_csv']],
                    ['schema', _['cmd_schema']],
                    ['copy', _['cmd_copy']],
                    ['table_create', _['cmd_table_create']],
                    ['query', _['cmd_query']],
                    ['vacuum', _['cmd_vacuum']],
                )
            ])
    #
    if not isnosb() and sess.user:
        aform = forms(first_blank=True)
        aform1 = aform[1:]
        #
        formact =  [
                    ['run', _['cmd_run']],
                    ['shortcut', _['cmd_shortcut']],
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
        shortcut_form = r_shortcuts().get(SHORTCUT_TYPE_FORM)
        if shortcut_form:
            ret.append(
                [
                    '/form/run',
                    'get',
                    '',
                    [], 
                    [],
                    shortcut_form,
                ])            
    #
    if not isnosb() and sess.user:
        arep = reports(first_blank=True)
        arep1 = arep[1:]
        #
        repact =  [
                    ['run', _['cmd_run']],
                    ['shortcut', _['cmd_shortcut']],
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
        shortcut_report = r_shortcuts().get(SHORTCUT_TYPE_REPORT)
        if shortcut_report:
            ret.append(
                [
                    '/report/run',
                    'get',
                    '',
                    [], 
                    [],
                    shortcut_report,
                ])                        
    #
    return ret

def hasws(s):
    ret = False
    #
    if not isstr(s, True):
        return ret
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
        s_adm = '%s %s %s %s %s %s' %(
            _['x_yes'], 
            link('/admin/users', _['cmd_users']),
            link('/admin/hosts', _['cmd_hosts']),
            link('/admin/system', _['cmd_system']),
            link('/admin/backup', _['cmd_backup']),
            link('/admin/scripts', _['cmd_scripts']),
            )
    if isnosb(): s_adm = _['x_not_applicable']
    #
    try:
        s_reportlab = reportlab.Version
    except:
        s_reportlab = _['x_not_avail_pdf']
    #
    ret = [
            (_['x_version'], s_a),
            (_['x_sqlite_version'], db.db_module.sqlite_version),
            (_['x_python_version'], platform.python_version()),
            (_['x_web_version'], web.__version__),
            (_['x_reportlab_version'], s_reportlab),
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

def fref(reference, execute_sql=True, input_name='input_name'):
    reference2 = 0
    if (type(reference) in [type(''), type(u'')]) and reference:#query
        reference2 = []
        try:
            if not execute_sql:
                reference = ''
            #
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
    elif isinstance(reference, int): #int
        if reference == REFERENCE_FLAG_PASSWORD:
            reference2 = web.form.Password(input_name)
    else:
        reference2 = 0
    #
    return reference2
    
def fref2(reference, name):
    ret = None
    #
    if isinstance(reference, list):
        ret = SimpleDropdown(name, args=reference)
    elif hasattr(reference, 'render'):
        ret = reference
    #
    return ret
    
def fdef(default, execute_sql=True):
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
            #
            if not execute_sql:
                defq = ''
            #
            defr = db.query(defq).list()
            if defr:
                default2 = defr[0]['f']
        except:
            pass
    #
    return default2
    
def parseform2(code, table, execute_sql=True):
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
                dcname = '%s.%s' %(fsub_table, dc)
                #
                reference2 = fref(reference, execute_sql, dcname)
                #
                reference3 = fref2(reference2, dcname)
                #
                default2 = fdef(default, execute_sql)
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

def parseform(form, virtual={}, execute_sql=True):
    fo = {}
    #
    if isstr(form):
        fo = s_select('form.code..%s' %(form))
        try:
            fo = fo[0]['e']
            fo = json.loads(fo)
        except:
            fo = {}
    elif isinstance(form, dict):
        fo = form
    #
    ftitle = fo.get(FORM_KEY_TITLE, form)
    finfo = fo.get(FORM_KEY_INFO, '')
    #single table
    table = ''
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
        cols = []
        colsn = []
        if isinstance(virtual, dict) and virtual:
            try:
                cols = columns(table) + virtual.get(table, [])
                colsn = [x.get('name') for x in cols]
            except:
                pass
        else:
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
                    reference2 = fref(reference, execute_sql, col)
                    #
                    reference3 = fref2(reference2, col)
                    #
                    default2 = fdef(default, execute_sql)
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
    fsub2 = parseform2(fsub, table, execute_sql)
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
    finsert = fo.get(FORM_KEY_INSERT)
    try:
        finsert = int(finsert)
    except:
        finsert = FORM_INSERT_DEFAULT
    #
    fconfirm = fo.get(FORM_KEY_CONFIRM, '')
    try:
        if not isstr(fconfirm):
            fconfirm = str(fconfirm)
        fconfirm = fconfirm.strip()
    except:
        fconfirm = ''
    #
    return [ftitle, finfo, input, fsub2, message2, sql2, finsert, fconfirm]

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

def rheaders(data, cell_len, cell_types):
    r0 = []
    r1 = 0
    ret = [r0, r1]
    #
    if not isinstance(data, list):
        return ret
    #
    if not data:
        return ret
    #
    for i in data:
        #
        if not isinstance(i, list):    
            continue
        #
        if not i:
            continue
        #
        temp = []
        for j in i:
            #
            if not isinstance(j, list):
                continue
            #
            lj = len(j)
            #
            if not lj == cell_len:
                continue
            #
            error = 1
            try:
                for k in range(lj):
                    if not isinstance(j[k], cell_types[k]):
                        raise Exception
                error = 0
            except:
                error = 1
            #
            if error:
                continue
            #
            temp.append(j)
            #
            lt = len(temp)
            if lt > r1:
                r1 = lt
            #
        #
        if temp:
            r0.append(temp)
    #
    ret = [r0, r1]
    return ret    
    
def rfooters(data, cell_len, cell_types):
    return rheaders(data, cell_len, cell_types)

def parsereport(report, execute_sql=True):
    fo = {}
    #
    if isstr(report):
        fo = s_select('report.code..%s' %(report))
        try:
            fo = fo[0]['e']
            fo = json.loads(fo)
        except:
            fo = {}
    elif isinstance(report, dict):
        fo = report
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
            reference2 = fref(reference, execute_sql, key)
            #
            reference3 = fref2(reference2, key)
            #
            default2 = fdef(default, execute_sql)
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
    xheaders = fo.get(REPORT_KEY_HEADERS, [])
    oheaders = rheaders(
                        xheaders, 
                        REPORT_HEADERS_CELL_LEN, 
                        REPORT_HEADERS_CELL_TYPES,
                    )
    #
    xfooters = fo.get(REPORT_KEY_FOOTERS, [])
    ofooters = rfooters(
                        xfooters, 
                        REPORT_FOOTERS_CELL_LEN, 
                        REPORT_FOOTERS_CELL_TYPES,
                    )
    #
    xpaper = fo.get(REPORT_KEY_PAPER, [])
    try:
        if not isinstance(xpaper, list): 
            raise Exception
        #
        xpaper2 = [ 
                        float(xpaper[0]), #width
                        float(xpaper[1]), #height
                ]
        #
        xpaper2 = [abs(x) for x in xpaper2]
    except:
        xpaper2 = []
    #
    xmargins = fo.get(REPORT_KEY_MARGINS, [])
    try:
        if not isinstance(xmargins, list): 
            raise Exception
        #
        xmargins2 = [ 
                        float(xmargins[0]), #left
                        float(xmargins[1]), #right
                        float(xmargins[2]), #top
                        float(xmargins[3]), #bottom
                ]
        #
        xmargins2 = [abs(x) for x in xmargins2]
    except:
        xmargins2 = []
    #
    fconfirm = fo.get(REPORT_KEY_CONFIRM, '')
    try:
        if not isstr(fconfirm):
            fconfirm = str(fconfirm)
        fconfirm = fconfirm.strip()
    except:
        fconfirm = ''    
    #
    return [ftitle, finfo, input, rquery, rheader, message2, oheaders, ofooters,
            xpaper2,
            xmargins2,
            fconfirm,
        ]

def nqtype(ftype):
    ret = False
    ftype = ftype.lower()
    #
    if ftype in NOQUOTE_TYPE or 'int' in ftype:
        ret = True
    #
    return ret 

def s_init_q(table=FORM_TBL):
    af = [x + ' ' + FORM_FIELD_TYPE for x in FORM_FIELDS]
    #
    ret = '''
        CREATE TABLE %s (
                rowid integer primary key autoincrement, 
                rowtime integer default (datetime('now', 'localtime')),
                %s
            )
        ''' %(
                table, ','.join(af)
            )
    #
    return ret

def s_init():
    cmd = s_init_q()
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

def r_system(config, default=None):
    ret = default
    #
    d = {}
    for x in SYSTEM_CONFIG:
        d[x[2]] = x[4]
    df = {}
    for x in SYSTEM_CONFIG:
        df[x[2]] = x[5]
    #
    if not config in d.keys():
        return ret
    #
    try:
        ret = s_check2(config, d.get(config)).get('d', default)
        ret = df.get(config)(ret)
    except:
        pass
    #
    return ret

def r_files(all_=False):
    if not all_:
        q = 'my.files.%s' %(user())
    else:
        q = 'my.files'
    #
    content = s_select(q, what='rowid, a, b, c, d, f, g', order='d asc')
    for c in content:
        g = {}
        try:
            g = json.loads(c.get('g'))
        except:
            pass
        c['size'] = size(g.get('size'))
        #
        if not c.get('d', '').strip():
            c['d'] = ''
    #
    return content

def r_fs_ok(sid):
    if not isstr(sid):
        return False
    #
    if not sid.strip():
        return False
    #
    allx = r_files()
    alld = [x['rowid'] for x in allx]
    if sid in alld:
        return True
    #
    allf = r_files(True)
    allfd = {}
    for f in allf:
        k = f.get('rowid')
        s = f.get('f', '')
        if k.strip():
            allfd[k] = s
    if sid in allfd.keys() and allfd.get(sid) == '1':
        return True
    #
    return False

def r_fs_content(sid):
    ret = []
    #
    try:
        r = db.select(FORM_TBL, 
                        what='d, e, g', 
                        where='rowid=$sid',
                        vars={
                                'sid': long(sid),
                            }
                    )
        r = r[0]
        ft = json.loads(r.g).get('type')
        fn = r.d
        fraw = json.loads(r.g).get('raw')
        if fraw == 1 or isblob(r.e):
            fc = r.e
        else:
            fc = base64.b64decode(r.e)    
        #
        ret = [fn, ft, fc]
    except:
        pass
    #
    return ret

def striphtml(text):
    data = StripHTMLParser()
    data.feed(text)
    ret = ''.join(data.text)
    return ret

def tr_page(code):
    s = str(code)
    #
    s = striphtml(s)
    #
    for r in REGEX_PAGE:
        try:
            if r[2]:
                s = re.compile(r[0], re.M).sub(r[1], s)
            else:
                s = re.compile(r[0]).sub(r[1], s)
        except:
            pass
    #
    return s
        
def fsize(f, working_dir=CURDIR, human_readable=True):
    sz = 0
    #
    try:
        f = os.path.abspath(os.path.join(working_dir, f))
        #
        sz = os.path.getsize(f)
    except:
        pass
    #
    ret = sz
    if human_readable:
        ret = size(sz)
    #
    return ret

def tr_newline(s, br='<br/>'):
    ret = str(s)
    #
    ret = ret.replace('\r\n', br)
    ret = ret.replace('\n\r', br)
    ret = ret.replace('\r', br)
    ret = ret.replace('\n', br)
    #
    return ret

def tr_newline_html(s):
    return tr_newline(s, '<br>')

def tr_report_text(s, data):
    ret = s
    #
    return ret

def r_scripts():
    ret = []
    #
    q = 'install.scripts'
    #
    content = s_select(q)
    for c in content:
        e = {}
        try:
            e = json.loads(c.get('e'))
        except:
            pass
        c[SCRIPT_KEY_NAME] = e.get(SCRIPT_KEY_NAME, '')
        c[SCRIPT_KEY_INFO] = e.get(SCRIPT_KEY_INFO, '')
        c[SCRIPT_KEY_AUTHOR] = e.get(SCRIPT_KEY_AUTHOR, '')
        c[SCRIPT_KEY_LICENSE] = e.get(SCRIPT_KEY_LICENSE, '')
        #
        cn = c.get(SCRIPT_KEY_NAME, '')
        if isstr(cn):
            cn = cn.strip()
        if not isstr(cn) or not cn:
            continue
        #
        ret.append(c)
    #
    return ret

def g_script(script):
    ret = {}
    #
    scripts = r_scripts()
    #
    for s in scripts:
        rowid = s.get('rowid', '')
        if not isstr(rowid):
            continue
        #
        if script == rowid:
            ret = s
            break
    #
    return ret

def xreqparsed(parsed, required):
    ret = False
    #
    try:
        for r in required:
            if not parsed[r]:
                return ret
    except:
        return ret
    #
    return True

def xparsescript(script):
    ret = {}
    #
    e = {}
    try:
        e = json.loads(script.get('e'))
    except:
        pass
    #
    for k in SCRIPT_REQ:
        if not e.has_key(k):
            return ret
    #
    ttypes = []
    for x in COLUMN_TYPES:
        if x[1]:
            ttypes.append(x[0])
    tpk = [x[1] for x in SCRIPT_VALID_COLUMN_FLAG]
    tcode = e.get(SCRIPT_KEY_TABLES, [])
    if not isinstance(tcode, list):
        tcode = []
    tcode2 = []
    virtual_tables = {}
    for tt in tcode:
        tstat = SCRIPT_TABLE_ERROR
        #
        if len(tt) < 2:
            continue
        #
        tcols = tt[1:]
        tcols = [x for x in tcols if isinstance(x, list)]
        tcols = [x for x in tcols if len(x) >= SCRIPT_TABLE_COLUMN_LEN]
        if not tcols:
            continue
        #
        tcols = [x for x in tcols if validfname(x[0])]
        tcols = [x for x in tcols if str(x[1]) in ttypes]
        tcols = [x for x in tcols if x[2] in tpk]
        if not tcols:
            continue
        #
        tname = tt[0]
        if not validfname(tname):
            continue
        #
        ncols = []
        xxcols = []
        if not tname in tables():
            tstat = SCRIPT_TABLE_OK
            ncols = tcols
        else:
            tstat = SCRIPT_TABLE_EXISTS
            #
            conflict = False
            ecolz = {}
            for z in columns(tname):
                ecolz[z.get('name').lower()] = z.get('type').lower()
            #
            ecols = columns(tname, True)
            ecols = [x.lower() for x in ecols]
            for n in tcols:
                if not n[0].lower() in ecols:
                    ncols.append(n)
                else:
                    nl0 = n[0].lower()
                    nl1 = n[1].lower()
                    if nl1 != ecolz.get(nl0):
                        conflict = True
                        xxcols.append(n)
            #
            if conflict:
                ncols = tcols
                tstat = SCRIPT_TABLE_COLUMN_CONFLICT
        #
        if not ncols:
            continue
        #
        ttemp = [tname, tstat, tcols, ncols, xxcols]
        tcode2.append(ttemp)
        #
        try:
            tnamel = tname.lower()
            if not virtual_tables.has_key(tnamel):
                virtual_tables[tnamel] = []
            for n in ncols:
                vt = {
                        'name': n[0], 
                        'type': n[1],
                    }
                vtt = virtual_tables.get(tnamel, [])
                vtt.append(vt)
                virtual_tables[tnamel] = vtt
        except:
            pass
        #
    ret[SCRIPT_KEY_TABLES] = tcode2
    #
    tcode = e.get(SCRIPT_KEY_FORMS, [])
    if not isinstance(tcode, list):
        tcode = []
    tcode2 = []
    for tt in tcode:
        tstat = SCRIPT_FORM_ERROR
        #
        if len(tt) < 2:
            continue
        #
        tname = tt[0]
        tcont = tt[1]
        #
        if not validfname(tname):
            continue
        #
        tname = tname.strip().lower()
        #
        if not isinstance(tcont, dict):
            continue
        #
        parsed = parseform(copy.deepcopy(tcont), virtual=virtual_tables, execute_sql=False)
        if not xreqparsed(parsed, FORM_REQ_X):
            continue
        #
        if not tname in forms():
            tstat = SCRIPT_FORM_OK
        else:
            tstat = SCRIPT_FORM_EXISTS
        #
        jcont = ''
        try:
            jcont = json.dumps(tcont, indent=JSON_INDENT)
        except:
            pass
        #
        ttemp = [tname, tstat, tcont, jcont]
        tcode2.append(ttemp)
    ret[SCRIPT_KEY_FORMS] = tcode2            
    #
    tcode = e.get(SCRIPT_KEY_REPORTS, [])
    if not isinstance(tcode, list):
        tcode = []
    tcode2 = []
    for tt in tcode:
        tstat = SCRIPT_REPORT_ERROR
        #
        if len(tt) < 2:
            continue
        #
        tname = tt[0]
        tcont = tt[1]
        #
        if not validfname(tname):
            continue
        #
        tname = tname.strip().lower()
        #
        if not isinstance(tcont, dict):
            continue
        #
        parsed = parsereport(copy.deepcopy(tcont), execute_sql=False)
        if not xreqparsed(parsed, REPORT_REQ_X):
            continue
        #
        if not tname in reports():
            tstat = SCRIPT_REPORT_OK
        else:
            tstat = SCRIPT_REPORT_EXISTS
        #
        jcont = ''
        try:
            jcont = json.dumps(tcont, indent=JSON_INDENT)
        except:
            pass
        #        
        ttemp = [tname, tstat, tcont, jcont]
        tcode2.append(ttemp)
    ret[SCRIPT_KEY_REPORTS] = tcode2            
    #
    tcode = e.get(SCRIPT_KEY_PROFILES, [])
    if not isinstance(tcode, list):
        tcode = []
    tcode2 = []
    for tt in tcode:
        if not isinstance(tt, list):
            continue
        if len(tt) != PROFILE_USER_DEFINED_LEN:
            continue
        if not isstr(tt[0]):
            continue
        if not validfname(tt[0]):
            continue
        #
        ttemp = tt
        tcode2.append(ttemp)
    ret[SCRIPT_KEY_PROFILES] = tcode2
    #
    for k in e.keys():
        if not ret.has_key(k):
            ret[k] = e.get(k)
    #
    return ret

def xokscript(pscript):
    ret = False
    #
    if not isinstance(pscript, dict):
        return ret
    #
    if not pscript:
        return ret
    #
    tables = pscript.get(SCRIPT_KEY_TABLES, [])
    forms = pscript.get(SCRIPT_KEY_FORMS, [])
    reports = pscript.get(SCRIPT_KEY_REPORTS, [])
    #
    if not tables and not forms and not reports:
        return ret
    #
    errors = 0
    #
    alls = [tables, forms, reports]
    for a in alls:
        if not isinstance(a, list):
            errors += 1
            continue                
        #
        for i in a:
            if not isinstance(i, list):
                errors += 1
                continue                
            #
            if not len(i) > 2: #check: xparsescript, dirty, at least
                errors += 1
                continue
            #
            if i[1] < 0: #negative, error
                errors += 1
    #
    if errors:
        return ret
    #
    return True

def s_isold():
    ret = False
    #
    if isnosb():
        return ret
    #
    cols = columns(FORM_TBL, True)
    #
    for r in FORM_FIELDS_R1:
        if not r in cols:
            ret = True
            break
    #
    return ret
    
def s_xupdate():
    allt = tables()
    while True:
        newtbl = '%s_%s' %(FORM_TBL, random.randint(0, 100000))
        if not newtbl in allt:
            break
    #
    ret = 0
    rows = ret
    #
    #
    try:
        q = s_init_q(newtbl)
        db.query(q)
    except:
        return ret
    #
    try:
        cols = columns(FORM_TBL, True)
        q = '''
                insert into %s(%s) select %s from %s
            ''' %(
                newtbl,
                ','.join(cols),
                ','.join(cols),
                FORM_TBL,
            )
        rows = db.query(q)
    except:
        return ret
    #
    try:
        q = 'drop table %s' %(FORM_TBL)
        db.query(q)
    except:
        return ret
    #
    try:
        q = 'alter table %s rename to %s' %(newtbl, FORM_TBL)
        db.query(q)
    except:
        return ret
    #
    ret = rows
    return ret

def p_pragma(pragma, default=''):
    ret = default
    #
    try:
        r = db.query('pragma $pragma', 
                vars={
                        'pragma': web.sqlliteral(pragma),
                    }
            ).list()
        ret = r[0].get(pragma)
    except:
        pass
    #
    return ret

def scmdx_path(f):
    ret = ''
    #
    try:
        f = os.path.basename(f)
        f = os.path.join(SCURDIR, f)
        f = os.path.abspath(f)
        ret = f
    except:
        return ret
    #
    return ret

def scmd_favicon(data):
    ret = ''
    #
    try:
        cmd = data[0]
        #
        out = data[1]
        out = scmdx_path(out)
        #
        if os.path.exists(out):
            raise Exception
        #
        f = open(out, 'wb')
        f.write(favicon())
        f.close()
        #
        ret = out
    except:
        return ret
    #
    return ret

def scmd_pyinstaller(data):
    ret = ''
    #
    try:
        cmd = data[0]
        #
        out = data[1]
        out = scmdx_path(out)
        #
        ico = data[2]
        ico = scmdx_path(ico)
        #
        tpl = string.Template(PYINSTALLER_SPEC)
        tplo = tpl.substitute(tpl, 
                title=TITLE,
                command=cmd,
                source=URL_SOURCE[2],
                readme=URL_README[2],
                source_path=os.path.join(CURDIR, URL_SOURCE[2]),
                readme_path=os.path.join(CURDIR, URL_README[2]),
                output=DEFAULT_WIN_EXE,
                icon=ico,
                output_md5=DEFAULT_WIN_MD5,
                output_version=DEFAULT_WIN_EXE_VERSION,
                datetime=sqliteboy_time3(sqliteboy_time())
            )
        #
        if os.path.exists(out):
            raise Exception        
        #
        if not os.path.exists(ico):
            raise Exception
        #
        f = open(out, 'wb')
        f.write(tplo)
        f.close()
        #
        ret = out
    except:
        return ret
    #
    return ret

def scmd_build(data):
    ret = ''
    #
    try:
        cmd = data[0]
        #
        d3 = ['generate_version', DEFAULT_VERSION]
        r3 = scmd_version(d3)
        #
        d1 = ['generate_favicon', DEFAULT_FAVICON]
        r1 = scmd_favicon(d1)
        #
        d2 = ['generate_pyinstaller', DEFAULT_SPEC, r1]
        r2 = scmd_pyinstaller(d2)
        #
        ret = '%s %s %s' %(r3, r1, r2)
        ret = ret.strip()
    except:
        return ret
    #
    return ret
    
def scmd_version(data):
    ret = ''
    #
    try:
        cmd = data[0]
        #
        out = data[1]
        out = scmdx_path(out)
        #
        tpl = string.Template(VERSION_SPEC)
        tplo = tpl.substitute(tpl, 
                title=TITLE,
                command=cmd,                
                datetime=sqliteboy_time3(sqliteboy_time())
            )        
        #
        if os.path.exists(out):
            raise Exception
        #
        f = open(out, 'wb')
        f.write(tplo)
        f.close()
        #
        ret = out
    except:
        return ret
    #
    return ret

def shortcut(t, name):
    ret = False
    #
    t = str(t).strip().lower()
    name = str(name).strip().lower()
    #
    if not t in SHORTCUT_ALL:
        return ret
    #
    if not validfname(name):
        return ret
    #
    alls = []
    if t == SHORTCUT_TYPE_FORM:
        alls = forms()
    elif t == SHORTCUT_TYPE_REPORT:
        alls = reports()
    if not name in alls:
        return ret
    #
    q = 'my.shortcuts.%s.%s.%s' %(
                                user(),
                                name,
                                t,
                            )
    allq = s_select(q)
    #
    if not allq:
        try:
            r = db.insert(FORM_TBL,
                        a='my',
                        b='shortcuts',
                        c=user(),
                        d=name,
                        e=t
                )
            ret = True
        except:
            return ret
    else:
        try:
            r = db.delete(FORM_TBL,
                        where='a=$a and b=$b and c=$c and d=$d and e=$e',
                        vars={
                                'a': 'my',
                                'b': 'shortcuts',
                                'c': user(),
                                'd': name,
                                'e': t,
                            }
                )
            ret = True
        except:
            return ret
    #
    return ret

def r_shortcuts():
    q = 'my.shortcuts.%s' %(user())
    res = s_select(q)
    #
    sform = []
    sreport = []
    #
    for i in res:
        t = i.get('e')
        n = i.get('d')
        if not t or not n:
            continue
        #
        if not isstr(t) or not isstr(n):
            continue
        #
        n = n.strip().lower()
        if t == SHORTCUT_TYPE_FORM:
            sform.append(n)
        elif t == SHORTCUT_TYPE_REPORT:
            sreport.append(n)
    #
    ret = {
            SHORTCUT_TYPE_FORM: sform,
            SHORTCUT_TYPE_REPORT: sreport,
            }
    #
    return ret

def u_print(inp, data):
    if not isinstance(data, dict):
        return data
    #
    if not hasattr(inp, 'has_key'):
        return data
    #
    if inp.has_key(PRINT_DATA_KEY):
        data[PRINT_DATA_KEY] = PRINT_DATA_VALUE
    #
    return data

def c_db_static(db):
    ret = False
    #
    db = os.path.abspath(db)
    dirn = os.path.dirname(db)
    dirn = os.path.basename(dirn)
    dirn = str(dirn).lower()
    #
    if dirn in DEFAULT_WEBPY_STATIC:
        ret = True
    #
    return ret

def pr_user(default, x):
    ret = default
    if x:
        ret = x
    #
    return ret

def pr_style(default, x):
    ret = PROFILE_ITEM_STYLE[default]
    #
    if x < len(PROFILE_ITEM_STYLE):
        ret = PROFILE_ITEM_STYLE[x]
    #
    return ret

def pr_all(execute_sql=True, usr=None):
    ret = []
    #
    if isnosb() or usr == '':
        res = []
        upr = ''
    else:
        if usr is None:
            usr = user()
        res = s_select('user.account..%s' %(usr))
        upr = r_system('users.profile.')
    #
    try:
        if len(res) != 1:
            raise Exception
        #
        res = res[0]
        g0 = res.get('g')
        g = json.loads(g0)
    except:
        g = {}
    #
    upr1 = []
    try:
        upr1 = json.loads(upr)
        if not isinstance(upr1, list):
            raise Exception
    except:
        upr1 = []
    #
    upr2 = []
    upr2a = []
    spr = [x[0] for x in PROFILE_ALL]
    for i in upr1:
        if not isinstance(i, list):
            continue
        if not len(i) == PROFILE_USER_DEFINED_LEN:
            continue
        #
        name = str(i[0]).strip().lower()
        label = str(i[1])
        if not validfname(name):
            continue
        if name in spr:
            continue
        if name in upr2a:
            continue
        #
        data = [ 
                    name, 
                    label, 
                    i[2], 
                    i[3], 
                    PROFILE_USER_DEFINED_HANDLER,
                    PROFILE_USER_DEFINED_TYPE,
                    PROFILE_USER_DEFINED_LEVEL,
                ]
        upr2.append(data)
        upr2a.append(name)
    #
    pall = PROFILE_ALL + upr2
    for i in pall:
        name = i[0]
        label = i[1]
        value = fref(i[2], execute_sql, name)
        func = i[5]
        #
        dflt = i[3]
        if g.has_key(name):
            dflt = g.get(name)
        dflt = func(dflt)
        #
        check = globals().get(i[4])
        rcheck = check(i[3], dflt)
        #
        level = i[6]
        if level == PROFILE_USER_DEFINED_LEVEL:
            if isinstance(value, list):
                uvalue = []
                for v in value:
                    if isinstance(v, list):
                        uv = []
                        for iv in v:
                            if iv is not None: 
                                ivv = PROFILE_USER_DEFINED_TYPE(iv)
                            else:
                                ivv = ''
                            uv.append(ivv)
                        uvalue.append(uv)
                value = uvalue
        #
        value2 = fref2(value, name)
        if value2:
            try:
                value2.set_value(dflt)
            except:
                pass        
        #
        data = [name, label, value, dflt, rcheck, value2, func, level]
        ret.append(data)
    #
    return ret

def pr_get0(name, usr):
    ret = None
    #
    res = pr_all(False, usr)
    for i in res:
        if i[0] == name:
            ret = i[4]
            break
    #
    return ret
    
def pr_get(name):
    return pr_get0(name, user())

def v_set(name, value):
    ret = 0
    #
    if not isstr(name):
        return ret
    name = name.strip().lower()
    if not name:
        return ret
    if not validfname(name):
        return ret
    #
    u = user()
    #
    if not sess.var.has_key(u):
        sess.var[u] = {}
    if not isinstance(sess.var.get(u), dict):
        sess.var[u] = {}
    #
    su = sess.var.get(u)
    ku = []
    try:
        ku = su.keys()
    except:
        pass
    #
    lku = len(ku)
    if name in ku:
        lku -= 1
    if lku >= ENV_VAR_MAX:
        return ret
    #
    su[name] = value
    ret = 1
    #
    return ret
    
def v_get(name):
    ret = ''
    #
    try:
        u = user()
        name = name.strip().lower()
        ret = sess.var.get(u).get(name)
    except:
        pass
    #
    return ret
    
def v_del(name):
    ret = 0
    #
    try:
        u = user()
        name = name.strip().lower()
        del sess.var.get(u)[name]
        ret = 1
    except:
        pass
    #
    return ret

def py_o(name, func, prefix):
    ret = ''
    #
    if not isstr(name) or not isstr(prefix):
        return ret
    if not callable(func):
        return ret
    #
    name = name.strip()
    if not name in func():
        return ret
    #
    ret = '%s%s' %(prefix, name)
    return ret
    
def py_f(name):
    return py_o(name, forms, DEFAULT_PY_FORM)

def py_r(name):
    return py_o(name, reports, DEFAULT_PY_REPORT)

def py_handler(name):
    ret = None
    #
    m = None
    #
    try:
        m = __import__(DEFAULT_PY_HANDLER)
        reload(m)
    except:
        return ret
    #
    if m:
        if hasattr(m, name):
            res = getattr(m, name)
            if callable(res):
                ret = res
    #
    return ret

def r_schema(table):
    ret = ''
    #
    try:
        r = db.select(DEFAULT_TABLE, 
                        what='sql', 
                        where=" type='table' and tbl_name=$tbl_name",
                        vars={
                                'tbl_name': table,
                            }
            )
        ret = r[0].sql
    except:
        pass
    #
    return ret

def r_messages(category):
    ret = ''
    #
    if isnosb():
        return ret
    #
    category = str(category).strip().lower()
    if hasws(category) or not category:
        return ret
    #
    try:
        q = 'messages.%s.' %(category)
        ret = r_system(q)
    except:
        pass
    #
    return ret

def r_messages_all():
    return tr_page(r_messages('all')).strip()

def r_application_title():
    ret = ''
    #
    if not isnosb():
        try:
            q = 'application.title.'
            ret = r_system(q).strip()[:APPLICATION_TITLE_MAX]
        except:
            pass
    #
    return ret

def uquery(content):
    ret = ''
    #
    try:
        lret = []
        for k in content.keys():
            v = content.get(k)
            if isstr(v):
                kv = '%s=%s' %(k, web.urlquote(v))
                lret.append(kv)
        #
        ret_test = ''
        if lret:
            ret_test = '&'.join(lret)
        #
        if len(ret_test) > QUERY_STRING_MAX:
            raise Exception
        #
        ret = ret_test
    except:
        pass
    #
    return ret

def rpt_csv(data, content):
    
    def header_footer(hf):
        ret = []
        #
        for row in hf:
            temp = []
            for col in row:
                ccont = col.get('content', '')
                temp.append(ccont)
            ret.append(temp)   
        #
        return ret
    #
    export = []
    #
    headers = data.get(REPORT_KEY_HEADERS)
    headers_export = header_footer(headers)
    export.extend(headers_export)
    #
    export.append([])
    #
    if data['table']:
        ctr = 0
        keys = []
        for row in content:
            temp = []
            if ctr == 0:
                if not data[REPORT_KEY_HEADER]:
                    keys = row.keys()
                else:
                    keys = data[REPORT_KEY_HEADER]
                for k in keys:
                    temp.append(k)
                export.append(temp)
            #
            temp = []
            for k in keys:
                rk = row.get(k, '')
                if isblob(rk):
                    rk = _['z_view_blob']
                else:
                    if rk:
                        rk = str(rk)
                    else:
                        rk = ''
                temp.append(rk)
            export.append(temp)
            #
            ctr = ctr + 1
    #
    export.append([])
    #
    footers = data.get(REPORT_KEY_FOOTERS)
    footers_export = header_footer(footers)
    export.extend(footers_export)
    #    
    fout = cStringIO.StringIO()
    writer = csv.writer(fout)
    writer.writerows(export)
    ret = fout.getvalue()
    #
    return ret

def rpt_pdf(data, content, parsed):
    
    def header_footer(hf):
        ret = []
        #
        for row in hf:
            temp = []
            for col in row:
                ccont = col.get('content', '')
                cattr = col.get('data', '')
                ccont2 = PDF_PARAGRAPH(tr_newline(ccont), PDF_DEFAULT_PARAGRAPH_STYLE)
                #
                if cattr.get('type') == REPORT_CELL_TYPE_FILES_IMAGE:
                    if r_fs_ok(ccont):
                        ccont_img = r_fs_content(ccont)[2]
                        ccont_fimg = cStringIO.StringIO(ccont_img)
                        ccont2 = PDF_IMAGE(ccont_fimg)
                #
                temp.append(ccont2)
            ret.append(temp)   
        #
        return ret
    #
    spacer = PDF_SPACER(
                            PDF_DEFAULT_SPACER_WIDTH,
                            PDF_DEFAULT_SPACER_HEIGHT
                        )
    #
    export = []
    #
    headers = data.get(REPORT_KEY_HEADERS)
    headers_export = header_footer(headers)
    headers_export_table = PDF_TABLE(
                                        headers_export,
                                        style=PDF_DEFAULT_BORDER_STYLE
                                    )
    export.append(headers_export_table)
    #
    export.append(spacer)
    #
    if data['table']:
        content_export = []
        #
        ctr = 0
        keys = []
        for row in content:
            temp = []
            if ctr == 0:
                if not data[REPORT_KEY_HEADER]:
                    keys = row.keys()
                else:
                    keys = data[REPORT_KEY_HEADER]
                for k in keys:
                    k = PDF_PARAGRAPH(tr_newline(k), PDF_DEFAULT_PARAGRAPH_STYLE)
                    temp.append(k)
                content_export.append(temp)
            #
            temp = []
            for k in keys:
                rk = row.get(k, '')
                if isblob(rk):
                    rk = _['z_view_blob']
                else:
                    if rk:
                        rk = str(rk)
                    else:
                        rk = ''
                rk = PDF_PARAGRAPH(tr_newline(rk), PDF_DEFAULT_PARAGRAPH_STYLE)
                temp.append(rk)
            content_export.append(temp)
            #
            ctr = ctr + 1
        #
        if content_export:
            content_export_table = PDF_TABLE(
                                                content_export,
                                                style=PDF_DEFAULT_BORDER_STYLE
                                            )
            export.append(content_export_table)
    #
    export.append(spacer)
    #
    footers = data.get(REPORT_KEY_FOOTERS)
    footers_export = header_footer(footers)
    footers_export_table = PDF_TABLE(
                                        footers_export,
                                        style=PDF_DEFAULT_BORDER_STYLE
                                    )    
    export.append(footers_export_table)
    #    
    upaper = parsed[8]
    umargins = parsed[9]
    upaper2 = PDF_DEFAULT_PAGE_SIZE
    if upaper:
        upaper2 = upaper
    umargins_l = umargins_r = umargins_t = umargins_b = PDF_UNIT_INCH
    if umargins:
        umargins_l, umargins_r, umargins_t, umargins_b = umargins
    #
    fout = cStringIO.StringIO()
    writer = PDF_TEMPLATE(
                            fout,
                            pagesize=upaper2,
                            leftMargin=umargins_l,
                            rightMargin=umargins_r,
                            topMargin=umargins_t,
                            bottomMargin=umargins_b
                        )
    writer.title = data.get('report', '')
    writer.subject = writer.title
    writer.creator = '%s - %s'%(TITLE, sqliteboy_time3a())
    writer.author = user()
    writer.build(export)
    ret = fout.getvalue()
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

def sqliteboy_x_profile(u, field):
    ret = ''
    #
    u = str(u)
    field = str(field)
    #
    if isnosb(): 
        return ret
    #
    try:
        ret = pr_get0(field, u)
    except:
        return ret
    #
    return ret
SQLITE_UDF.append(('sqliteboy_x_profile', 2, sqliteboy_x_profile))

def sqliteboy_x_my(field):
    return sqliteboy_x_profile(sqliteboy_x_user(), field)
SQLITE_UDF.append(('sqliteboy_x_my', 1, sqliteboy_x_my))


#----------------------------------------------------------------------#
# PYTHON HANDLER                                                       #
#----------------------------------------------------------------------#
py_handler_udf = {}
for i in SQLITE_UDF:
    py_handler_udf[ i[0] ] = i[2]
#
PY_HANDLER_DATA = {
                    'udf': py_handler_udf,
                }


#----------------------------------------------------------------------#
# TEMPLATE                                                             #
#----------------------------------------------------------------------#
T_BASE = '''$def with (data, content)
$ pr_get_style = pr_get('style')
<!DOCTYPE html>
<html>
<head>
<link rel='SHORTCUT ICON' href='/favicon.ico'>
<title>$title(data['title'], '')</title>
<meta charset='utf-8'>
$if data.has_key(print_data_key):
    <style>
    $pr_get_style[0]
    </style>    
$else:    
    <style>
    $pr_get_style[1]    
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

$ r_app_title = r_application_title()

<div class='main_menu'>
<table>
<tr>
<td>
$if r_app_title:
    $r_app_title
    <br>
    <br>
$title(data['title'])
</td>
<td align='right' width='25%'>
$if user():
    $user() <a href='/password'>$_['cmd_password']</a>
    <a href='/profile'>$_['cmd_profile']</a> 
    <a href='/files'>$_['cmd_files']</a> 
    <a href='/notes'>$_['cmd_notes']</a> 
    <a href='/pages'>$_['cmd_pages']</a> 
    <a href='/calculator'>$_['cmd_calculator']</a>
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
    $elif data['command'] == 'calculator':
        $ crtq = data['message']
        $if crtq:
            $crtq[crt['calculator']]
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
    $if len(i) == 6:
        <td colspan='2'>
        $if i[5]:
            $for i5 in i[5]:
                <a href='$i[0]/$i5'>$i5</a>&nbsp;
        </td>
    $else:
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
        $if i[3]:
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
</div>

<br>
$if data['command'] == 'browse':
    $ rows = data['rows']

    <form action="$data['action_url']" method="$data['action_method']">
    $ hkey = data['hidden_key']
    <input type='hidden' name="$hkey" value="$data[hkey]">
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>
    <br><br>
    $if data['limit']: 
        $_['x_page'] $data['page'], $_['x_limit'] $data['limit'], $rows $_['x_row'], $len(data['selected']) $_['x_selected']
        <br>
        $_['x_limit']: 
        $for l in data['browse_limit']:
            $if l == data['limit']:
                $l
            $else:
                <a href="$data['url']?$data['ksort']=$data['input_sort']&$data['korder']=$data['input_order']&$data['klimit']=$l&$data['kpage']=$data['page']&pages=$data['input_pages']">$l</a>
            &nbsp;
        <a href="$data['url']?$data['ksort']=$data['input_sort']&$data['korder']=$data['input_order']&$data['klimit']=0&pages=$data['input_pages']">$_['x_unlimited']</a>
        <br>
        $_['x_page']:
        $if data['input_pages'] == '1':
            <a href="$data['url']?$data['ksort']=$data['input_sort']&$data['korder']=$data['input_order']&$data['klimit']=$data['limit']&$data['kpage']=$data['page']&pages=0">$_['cmd_hide']</a>
        $else:
            <a href="$data['url']?$data['ksort']=$data['input_sort']&$data['korder']=$data['input_order']&$data['klimit']=$data['limit']&$data['kpage']=$data['page']&pages=1">$_['cmd_show']</a>
        |
        <a href="$data['url']?$data['ksort']=$data['input_sort']&$data['korder']=$data['input_order']&$data['klimit']=$data['limit']&$data['kpage']=$data['page_previous']&pages=$data['input_pages']">$_['x_previous']</a>&nbsp;
        <a href="$data['url']?$data['ksort']=$data['input_sort']&$data['korder']=$data['input_order']&$data['klimit']=$data['limit']&$data['kpage']=$data['page_next']&pages=$data['input_pages']">$_['x_next']</a>&nbsp;
        $if data['input_pages'] == '1' and data['pages']:
            |
            $for p in data['pages']:
                $if p == data['page']:
                    $p
                $else:
                    <a href="$data['url']?$data['ksort']=$data['input_sort']&$data['korder']=$data['input_order']&$data['klimit']=$data['limit']&$data['kpage']=$p&pages=$data['input_pages']">$p</a>
                &nbsp;
    $else:
        $rows $_['x_row'], $len(data['selected']) $_['x_selected']
        <br>
        <a href="$data['url']?$data['ksort']=$data['input_sort']&$data['korder']=$data['input_order']&$data['klimit']=$data['default_limit']&pages=$data['input_pages']">$_['x_page']</a>
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
            <a href="$data['url']?$data['column_query']&pages=$data['input_pages']">$data['column_vsort']</a>
            </th>
        $else:
            <th>
            $c['name'] 
            $if c['pk']:
                $pk_sym
            &nbsp;
            $for s in range(len(data['sort'])):
                <a href="$data['url']?$data['ksort']=$data['sort'][s]&$data['klimit']=$data['limit']&$data['kpage']=$data['page']&$data['korder']=$c['name']&pages=$data['input_pages']">$data['vsort'][s]</a>
            </th>
    
    $for x in content:
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
                $if c['type'] in data['blob_type'] or isblob(x[c['name']]):
                    $if x[c['name']]:
                        <a href="$data['blob_url']?$data['blob_var']=$x[rowid]&$data['blob_column']=$c['name']">$data['blob_command']</a>
                $else:
                    $x[c['name']]
            </td>
        </tr>
    </table>
    
    <br>
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>

    </form>
    <br>
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
    <br>
    <br>
    $ r_msg_all = r_messages_all()
    $if r_msg_all:
        <div class='messages'>
            <pre>$r_msg_all
            </pre>
        </div>
$elif data['command'] in ['readme', 'source']:
    <br>
    <br>
    <a href="$data['download']">$_['cmd_download']</a>
    <br>
    <br>
    $data['size']
    <br>
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
        $ ucontent = content.get(i[1], None)
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
            $if ucontent is not None:
                $i[5].set_value(ucontent)
            $i[5].render()
        $else:
            $if i[6]:
                $ defv = i[6]
            $if ucontent is not None:
                $ defv = ucontent
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
        $ ucontent = content.get(i[1], None)
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
            $if ucontent is not None:
                $i[4].set_value(ucontent)        
            $i[4].render()
        $else:
            $if i[5]:
                $ defv = i[5]
            $if ucontent is not None:
                $ defv = ucontent                
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
    $if data.has_key('headers'):
        <br>
        <table>
        $for row in data['headers']:
            <tr>
            $for col in row:
                $ ccont = col.get('content', '')
                $ cattr = col.get('data', {})
                $ ca_style = cattr.get('style', '')
                <td>
                    $if cattr.get('type') == 'files.image':
                        $if ccont:
                            $if ca_style:
                                <img src='/fs?sid=$ccont' style='$ca_style'>
                            $else:
                                <img src='/fs?sid=$ccont' border='0'>
                        $else:
                            $ccont
                    $else:    
                        $tr_newline(ccont)
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
                    <th>$tr_newline(k)
                    </th>
            <tr>
            $for k in keys:
                $ rek = re.get(k, '')
                $if isblob(rek):
                    <td>$_['z_view_blob']</td>
                $else:
                    <td>$tr_newline(rek)
                    </td>
            </tr>
            $ ctr = ctr + 1
        </table>    

    $if data.has_key('footers'):
        <br>
        <table>
        $for row in data['footers']:
            <tr>
            $for col in row:
                $ ccont = col.get('content', '')
                $ cattr = col.get('data', {})
                $ ca_style = cattr.get('style', '')
                <td>
                    $if cattr.get('type') == 'files.image':
                        $if ccont:
                            $if ca_style:
                                <img src='/fs?sid=$ccont' style='$ca_style'>
                            $else:
                                <img src='/fs?sid=$ccont' border='0'>
                        $else:
                            $ccont
                    $else:    
                        $tr_newline(ccont)
                </td>
            </tr>
        </table>
    
    <br>
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
            <input type='checkbox' name="$data['select']" value="$u['rowid']">
        </td>
        <td width='20%'>
            <input type='hidden' name='rowid' value="$u['rowid']">
            <input type='text' name='e' value="$u['e']">
        </td>
        <td>
            <textarea name='f' rows='5' style='width: 90%'>$u['f']</textarea>
        </td>
        <td>
            $if data['xaction']:
                $for a in data['xaction']:
                    <a href='$a[1]$u['rowid']'>$a[0]</a> 
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
            <input type='hidden' name='rowid' value=''>
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
$elif data['command'] == 'system':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    $if data['message']:
        <div>
            $data['message']
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
        <td width='20%'>
            $u[0]
        </td>
        <td>
            $u[1]
        </td>
        <td>
            $if u[4] == 1:
                <textarea name='$u[2]' cols='40' rows='10'>$u[3]</textarea>
            $else:
                <input type='text' name='$u[2]' value="$u[3]">
        </td>
        </tr>
    </table>
    </form>
$elif data['command'] == 'files':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)
                <br>
        </div>
    <form action="$data['action_url']" method="$data['action_method']" enctype="$data['action_enctype']">
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
            <input type='checkbox' name="$data['select']" value="$u['rowid']">
        </td>
        <td width='45%'>
            <input type='hidden' name='rowid' value="$u['rowid']">
            <input type='hidden' name='d' value="$u['d']">
            $u['d']
        </td>
        <td width='15%' align='right'>
            $u['size']
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
        <td>
            $if data['xaction']:
                $for a in data['xaction']:
                    <a href='$a[1]$u['rowid']' target='$a[2]'>$a[0]</a> 
            $else:
                &nbsp;
        </td>
        </tr>
    $for u in range(data['max']):
        <tr>
        <td width='12%' align='center'>
            &nbsp;
        </td>
        <td colspan="$len(data['columns'][1:])">
            <input type='hidden' name='rowid' value=''>
            <input type='hidden' name='d' value=''>
            <input type='hidden' name='f' value=''>
            <input type='file' name='d_new'>
        </td>
        </tr>
    </table>
    </form>
$elif data['command'] == 'pages':
    <p>
    $ hint = data['hint'][0].upper() + data['hint'][1:]
    <i>$hint</i>
    </p>
    $if data['message']:
        <div>
            $data['message']
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
    <a href="$data['url']" target='_blank'>$data['url']</a>
    <br>
    <br>
    <table>
    $for i in data['columns']:
        <th>
            $i
        </th>
    <tr>
    <td width='50%' style='vertical-align: top'>
        <textarea name='content' rows='40' cols='40'>$content[0]</textarea>
    </td>
    <td style='vertical-align: top'>
        <div>
        <pre>$:content[1]</pre>
        </div>
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'error_404':
    $if data['message']:
        <div>
            $data['message']
        </div>
$elif data['command'] == 'page':
    <pre>$:content</pre>
$elif data['command'] == 'calculator':
    $ query = ''
    $ res = data['message']
    $if res:
        $ query = res[0]
    $else:
        $ query = data['calculator']
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    <form action="$data['action_url']" method="$data['action_method']">
    <table>
    <tr>
    <td>
    <input id='qcalculator' type='text' name='q' value='$query' maxlength="$data['max_input']" size="$data['max_input']">
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
        <br>
        $res[0]<br>
        <br>
        $res[2]
        <br>
        $if not res[4]:
            <a href='#' onclick='javascript:document.getElementById("qcalculator").value="$res[2]"'>$_['cmd_use_result']</a>
$elif data['command'] == 'scripts':
    <p>
    $ hint = data['hint'][0].upper() + data['hint'][1:]
    <i>$hint</i>
    </p>    
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)
                <br>
        </div>
    <form action="$data['action_url']" method="$data['action_method']" enctype="$data['action_enctype']">
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
        <td>
            <a href="/admin/script/$u['rowid']">$u['name']</a>
        </td>
        <td>
            $u['info']
        </td>
        <td>
            $u['author']
        </td>
        <td>
            $u['license']
        </td>        
        <td>
            $u['f']
        </td>        
        </tr>
    <tr>
    <td colspan="5">
        <input type='file' name='d_new'>
    </td>
    </tr>
    </table>
    </form>
$elif data['command'] == 'script':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>    
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)
                <br>
        </div>
    <form action="$data['action_url']" method="$data['action_method']" enctype="$data['action_enctype']">
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
        
    $for i in data['info']:
        <tr>
        <td>$i[0]</td>
        <td>$content.get(i[1], '')</td>
        <td>&nbsp;</td>
        </tr>
        
    <tr>
    <td>$_['x_run_time']</td>
    <td>$data['run']</td>
    <td>&nbsp;</td>
    </tr>
    
    $ table_detail = data.get('table_detail', {})
    $ allx = [ ['tables', _['x_table'], data['table_info']], ['forms', _['x_form'], data['form_info']],  ['reports', _['x_report'], data['report_info']], ['profiles', _['x_profile'], data['profile_info']] ]
    $for x in allx:
        $ k = x[0]
        $ t = x[1]
        $ c = x[2]
        $for i in content[k]:
            <tr>
            <td width='20%'>$t</td>
            <td width='30%'>$i[0]</td>
            <td>
            $c.get(i[1], '')
            $if k == 'tables':
                $ zzz = table_detail.get(i[0], [])
                $if zzz:
                    <br>
                    <br>
                    <table>
                    $for zz in zzz:
                        <tr>
                            $for z in zz:
                                <td>
                                    $z
                                </td>
                        </tr>
                    </table>
                    <br>
            </td>
            </tr>
    
    </table>
    </form>
    
    <br>
    <br>
    <textarea style="width: 100%;" rows=10 readonly>
    $data['code']
    </textarea>
    <br>
    <br>
    
$elif data['command'] == 'copy':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>    
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)
                <br>
        </div>
    <form action="$data['action_url']" method="$data['action_method']" enctype="$data['action_enctype']">
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
        &nbsp;
    <br>
    <br>
    <table>
        <tr>
            <td>
            $_['x_copy_from']
            </td>
            <td>
            $data['table']
            <input type='hidden' name='table' value='$data["table"]'>
            </td>            
        </tr>
        <tr>
            <td>
            $_['x_copy_to']
            </td>
            <td>
            $data['target'].render()
            </td>            
        </tr>
    </table>
    </form>
$elif data['command'] == 'empty':
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
$elif data['command'] == 'vacuum':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)
                <br>
        </div>
    <br>
    <table>
    $for i in data['info']:
        <tr>
            <td>
                $i[0]
            </td>
            <td>
                $i[1]
            </td>
        </tr>
    </table>
    <br>    
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
$elif data['command'] == 'import':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)
                <br>
        </div>
    <form action="$data['action_url']" method="$data['action_method']" enctype="$data['action_enctype']">
    $for h in data['hidden']:
        <input type='hidden' name='$h[0]' value='$h[1]'>
    <table>
    <tr>
    <td>
        <input type='file' name='f'>
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
$elif data['command'] == 'profile':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)
                <br>
        </div>
    <form action="$data['action_url']" method="$data['action_method']" enctype="$data['action_enctype']">
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
        &nbsp;
    <br>
    <br>
    $ pro0 = content[0]
    <table>
    $for i in pro0:
        $ i0 = i[0]
        $ i1 = i[1]
        $ i2 = i[2]
        $ i3 = i[3]
        $ i5 = i[5]
        $ i7 = i[7]
        <tr>
            <td width='30%'>
                $if i7 == 0:
                    $_[i1]
                $else:
                    $pk_sym $i1
            </td>
            <td>
                $if i5:
                    $i5.render()
                $else:
                    <input type='text' name='$i0' value='$i3'>
            </td>
        </tr>
    </table>
    <br>
    <i>$pk_sym $_['x_user_defined_profile']</i>
    <br>
    </form>
$elif data['command'] == 'schema':
    <p>
    <i>$data['hint'].capitalize()</i>
    </p>    
    $if data['message']:
        <div>
            $for m in data['message']:
                $': '.join(m)
                <br>
        </div>
    <form action="$data['action_url']" method="$data['action_method']" enctype="$data['action_enctype']">
    $for b in data['action_button']:
        $if b[2]:
            <input type='$b[4]' name='$b[0]' value='$b[1]' onclick='return confirm("$b[3].capitalize()");'>
        $else:
            <input type='$b[4]' name='$b[0]' value='$b[1]'>    
        &nbsp;
    <br>
    <br>
    <table>
        <tr>
            <td colspan='2'>
                <br>
                <br>
                $:content
                <br>
                <br>
            </td>
        </tr>
        <tr>
            <td>
            $_['x_create_table_schema']
            </td>
            <td>
            <input type='hidden' name='table' value='$data["table"]'>
            <input type='text' name='target' value='$data["target"]'>
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
    'shortcuts' : r_shortcuts,
    'print_data_key': PRINT_DATA_KEY,
    'print_data_value': PRINT_DATA_VALUE,
    'pr_get'    : pr_get,
    'r_messages_all': r_messages_all,
    'r_application_title': r_application_title,
    'tr_newline': tr_newline_html,
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
            ('table_empty', '/table/empty?table=' + table),
            ('table_drop', '/table/drop?table=' + table),
            ('export_csv', '/table/export/csv?table=' + table),
            ('import_csv', '/table/import/csv?table=' + table),
            ('schema', '/table/schema?table=' + table),
            ('copy', '/table/copy?table=' + table),
            ('table_create', '/table/create'),
            ('query', '/query'),
            ('vacuum', '/vacuum'),
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
            raise web.seeother('/table/browse/%s?limit=%s' %(table, DEFAULT_LIMIT))
        #
        try:
            select = [int(x) for x in select]
        except:
            dflt()
        #
        if input.has_key('delete'):
            for i in select:
                db.delete(table, where='%s=%s' %(ROWID, i))
            raise web.seeother('/table/browse/%s?limit=%s' %(table, DEFAULT_LIMIT))
        #
        elif input.has_key('edit'):
            sess.table[table][SKT_ROWID] = select
            raise web.seeother('/table/row/%s' %(table))
        #
        elif input.has_key('clear'):
            sess.table[table][SKT_ROWID] = []
            raise web.seeother('/table/browse/%s?limit=%s' %(table, DEFAULT_LIMIT))
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
        input = web.input(limit=0, order='', sort='', page=1, pages=0)
        #
        try:
            limit = abs(int(input.limit))
            page = abs(int(input.page))
            if page == 0:
                page = 1
            offset = (page-1) * limit
        except:
            limit = 0
            page = 1
            offset = 0
        #
        order = input.order
        qorder = None
        sort = input.sort
        column_query = ''
        column_sort = ''
        if not limit:
            limit = None
        if not offset:
            offset = None
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
                    column_query = 'order=%s&sort=%s&limit=%s&page=%s' %(order, ssort(sort), limit, page)
                #
                column_sort = vsort(sort) #current, not next
                qorder = '%s %s' %(order, sort)
        #
        glimit = ''
        if limit: glimit = str(limit)
        gpage = ''
        if page: gpage = str(page)
        iorder = ''
        if order: iorder = order
        if page > 1:
            page_previous = page - 1
        else:
            page_previous = 1
        page_next = page + 1
        #
        ipages = '0'
        apages = []
        if input.pages == '1':
            ipages = '1'
        if ipages == '1' and limit:
            try:
                r = db.select(table, what='count(*) as count')
                ncount = r[0].count
                npages = (ncount / limit) + 1
                if (npages-1) * limit != ncount:
                    npages = npages + 1
                apages = range(1, npages)
            except:
                ipages = '0'
        #
        r = db.select(table, what='%s as %s, *' %(ROWID, rowid), order=qorder, limit=limit, offset=offset).list()
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
            'kpage': 'page',
            'limit': glimit, 
            'select': NAME_SELECT,
            'action_url': '/table/action',
            'action_method': 'post',
            'action_button': (
                                ('delete', _['cmd_delete_selected'], True, _['cf_delete_selected'], 'submit'), 
                                ('edit', _['cmd_edit_selected'], False, '', 'submit'),
                                ('clear', _['cmd_clear_selected'], False, '', 'submit'),
                            ),
            'hidden_key': 'table',
            'rowid' : rowid,
            'blob_type': BLOB_TYPE,
            'blob_url': '/table/blob/%s' %(table),
            'blob_var': BLOB_VAR,
            'blob_column': BLOB_COLUMN,
            'blob_command': _['cmd_download'],
            'selected': sess.table[table][SKT_ROWID],
            'rows': len(r),
            'page': gpage,
            'page_previous': page_previous,
            'page_next': page_next,
            'input_order': iorder,
            'input_sort': sort,
            'browse_limit': [str(x) for x in BROWSE_LIMIT_ALL],
            'input_pages': ipages,
            'pages': [str(x) for x in apages],
            'default_limit': DEFAULT_LIMIT,
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
        table = input.table.strip().lower()
        name = input.name.strip().lower()
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


class table_export_csv:
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
            alld = [x['rowid'] for x in notes]
            if inp.src == 'notes' and inp.sid in alld:
                for n in notes:
                    if n['rowid'] == inp.sid:
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
                                ('query_export', _['cmd_query_export_csv'], False, '', 'submit'),
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
        qerr = 0
        try:
            msg = db.query(q)
            err = _['th_ok']
            multi = 1
            if isinstance(msg, (int, long, float)):
                multi = 0 
        except Exception, e:
            msg = e.message
            err = _['th_error']
            multi = 0
            qerr = 1
        #
        stop()
        t = rt()
        #
        prepsess()
        #
        if web.input().has_key('query_export') and not qerr and multi:
            fout = cStringIO.StringIO()
            writer = csv.writer(fout)
            #
            keys = []
            counter = 0
            for i in msg:
                if counter == 0:
                    keys = i.keys()
                    writer.writerow(keys)
                #
                line = []
                for k in keys:
                    v = i.get(k)
                    if isblob(v):
                        v = base64.b64encode(v)
                    line.append(v)
                #
                writer.writerow(line)
                counter += 1
            #
            content = fout.getvalue()
            #
            disposition = 'attachment; filename=' + '%s' %(DEFAULT_QUERY_EXPORT)
            web.header('Content-Type', CSV_CTYPE)
            web.header('Content-Disposition', disposition)
            return content            
        else:
            sess.query = [q, err, multi, msg, t]
            raise web.seeother('/query')
        #
        dflt()


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
        table = input.table.strip().lower()
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
        #
        inp = web.input(download='')
        download = inp.download.strip()
        error = 0
        #
        data = {
                'title': _['tt_readme'],
                'command': 'readme',
                'download': '%s?download=1' %(URL_README[0]),
                'size': fsize(URL_README[2]),
            }
        #
        try:
            content = open(os.path.join(CURDIR, URL_README[2])).read()
        except:
            content = _['e_open_file']
            error = 1
        #
        stop()
        #
        if download == '1' and not error:
            disposition = 'attachment; filename=%s' %(URL_README[2])
            web.header('Content-Type', PLAIN_CTYPE)
            web.header('Content-Disposition', disposition)
            return content
        #
        return T(data, content)


class sqliteboy_source:
    def GET(self):
        start()
        #
        inp = web.input(download='')
        download = inp.download.strip()
        #        
        data = {
                'title': _['tt_source'],
                'command': 'source',
                'download': '%s?download=1' %(URL_SOURCE[0]),
                'size': fsize(URL_SOURCE[2]),
            }
        #
        content2 = ''
        try:
            content = web.htmlquote(open(os.path.join(CURDIR, URL_SOURCE[2])).read())
            #
            if download == '1':
                content2 = open(os.path.join(CURDIR, URL_SOURCE[2])).read()
        except:
            content = _['e_open_file'] 
        #
        stop()
        #
        if download == '1' and content2.strip():
            disposition = 'attachment; filename=%s' %(URL_SOURCE[2])
            web.header('Content-Type', PLAIN_CTYPE)
            web.header('Content-Disposition', disposition)
            return content2
        #
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
        sess.var = {}
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


class admin_system:
    def GET(self):
        start()
        #
        data = {
                'title': _['tt_system'],
                'command': 'system',
                'action_url': '/admin/system',
                'action_method': 'post',
                'action_button': (
                                    ('save', _['cmd_save'], False, '', 'submit'),
                                ),
                'columns' : (
                                _['x_section'],
                                _['x_key'],
                                _['x_value'],
                            ),
                'message': smsgq(SK_SYSTEM, default=''),
                'hint': _['h_system'],
            }
        #
        content = []
        for s in SYSTEM_CONFIG:
            c = [
                    _[s[0]],
                    _[s[1]],
                    s[2],
                    s_check(s[2], s[3]).get('d'),
                    s[6],
                ]
            content.append(c)
        #
        stop()
        return T(data, content)
    
    def POST(self):
        inp = web.input()
        #
        skeys = [x[2] for x in SYSTEM_CONFIG]
        dkeys = {}
        for s in SYSTEM_CONFIG:
            dkeys[s[2]] = [s[4], s[5]]
        #
        try:
            for k in inp.keys():
                k = k.strip()
                if (k) and (k in skeys) and (s_select(k)):
                    kd = dkeys.get(k, [])
                    kdv = kd[0]
                    kdf = kd[1]
                    ku = inp.get(k, kdv)
                    try:
                        if isinstance(kdf, str):
                            kdf = globals().get(kdf)
                        test = kdf(ku)
                        ku = test
                    except:
                        ku = kdv
                    p = '%s%s%s' %(k, FORM_SPLIT, ku)
                    s_save(p, maxsplit=SYSTEM_CONFIG_MAXSPLIT)
            sess[SK_SYSTEM] = _['o_system']
        except:
            sess[SK_SYSTEM] = _['e_system']
        #
        raise web.seeother('/admin/system')


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
            ('shortcut', '/form/shortcut/' + form),
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
        action_button = ()
        ftitle = ''
        finfo = ''
        fconfirm = ''
        yconfirm = False
        if not reqform(form):
            input = ()
            sub = ()
            sess[SKF_RUN] = [
                                [_['e_form_run_syntax_or_required']],
                            ]
        else:
            try:
                pform = parseform(form)
                fconfirm = pform[7]
                if fconfirm:
                    yconfirm = True
                action_button = (
                                    ('save', _['cmd_go'], yconfirm, fconfirm, 'submit'),
                                )
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
        content = web.input()
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
        finsert = FORM_INSERT_DEFAULT
        try:
            pform = parseform(form)
            finput = pform[2]
            fsub = pform[3]
            message2 = pform[4]
            fsql2 = pform[5]
            finsert = pform[6]
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
        ucontent = ''
        if errors:
            sess[SKF_RUN] = errors
            ucontent = uquery(ocols)
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
                #
                #insert?
                form_res = finsert
                form_last = finsert
                #
                if finsert > 0:
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
                #python handler
                try:
                    py_func = py_handler(py_f(form))
                    f_python_handler = py_func(
                                            user(), 
                                            db, 
                                            pform, 
                                            [
                                                table,
                                                ocols,
                                                fsub_table,
                                                fsub_all2,
                                                fsub_ref,
                                            ],
                                            PY_HANDLER_DATA
                                        )
                    if not isinstance(f_python_handler, int):
                        raise Exception
                except:
                    f_python_handler = -1
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
                    #
                    message2b = string.Template(message2b)
                    ocols[FORM_MESSAGE_VAR_RESULT] = str(form_res)
                    ocols[FORM_MESSAGE_VAR_PYTHON_HANDLER] = str(f_python_handler)
                    message3 = message2b.safe_substitute(ocols)
                #
                sess[SKF_RUN] = [ [message3] ]
            except Exception, e:
                form_trans.rollback()
                sess[SKF_RUN] = [ [_['e_form_insert_general'], str(e)] ]
                raise web.seeother('/form/run/%s' %(form))
            else:
                form_trans.commit()
        #
        raise web.seeother('/form/run/%s?%s' %(form, ucontent))
        

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
                    #
                    db.update(FORM_TBL, where='a=$a and b=$b and d=$d and e=$e',
                        vars={
                                'a': 'my',
                                'b': 'shortcuts',
                                'd': form,
                                'e': SHORTCUT_TYPE_FORM,
                            },
                        d=name
                    )
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
            ('shortcut', '/report/shortcut/' + report),
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
                    #
                    db.update(FORM_TBL, where='a=$a and b=$b and d=$d and e=$e',
                        vars={
                                'a': 'my',
                                'b': 'shortcuts',
                                'd': report,
                                'e': SHORTCUT_TYPE_REPORT,
                            },
                        d=name
                    )                    
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
        action_button = ()
        #
        ftitle = ''
        finfo = ''
        fconfirm = ''
        yconfirm = False
        if not reqreport(report):
            input = ()
            sess[SKR_RUN] = [
                                [_['e_report_run_syntax_or_required']],
                            ]
        else:
            try:
                preport = parsereport(report)
                fconfirm = preport[10]
                if fconfirm:
                    yconfirm = True
                #
                action_button = [
                                    ('report', _['cmd_go'], yconfirm, fconfirm, 'submit'),
                                    (PRINT_DATA_KEY, _['cmd_go_print'], yconfirm, fconfirm, 'submit'),
                                    (REPORT_FORMAT_CSV, _['cmd_csv'], yconfirm, fconfirm, 'submit'),
                                ]
                if reportlab:
                    action_button.append(
                                            (
                                                REPORT_FORMAT_PDF, 
                                                _['cmd_pdf'], 
                                                yconfirm, 
                                                fconfirm, 
                                                'submit'
                                            ),
                                        )                        
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
        content = web.input()
        stop()
        return T(data, content)
        
    def POST(self, unused):
        input = web.input(hreport='')
        report = input.hreport.strip()
        #
        rformat = REPORT_FORMAT_DEFAULT
        if input.has_key(REPORT_FORMAT_CSV):
            rformat = REPORT_FORMAT_CSV
        elif input.has_key(REPORT_FORMAT_PDF):
            rformat = REPORT_FORMAT_PDF
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
        reportinfo = ''
        finput = None
        rquery = None
        rheader = []
        message2 = []
        pheaders = []
        pfooters = []
        pheaders2 = []
        pfooters2 = []        
        try:
            preport = parsereport(report)
            freport = preport[0]
            reportinfo = preport[1]
            finput = preport[2]
            rquery = preport[3]
            rheader = preport[4]
            message2 = preport[5]
            pheaders = preport[6]
            pfooters = preport[7]
        except:
            preport = None
        #
        #if not preport or not finput: 
        #as of 9-July-2013/v1.06, data might be empty
        if not preport:
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
        ucontent = ''
        if errors:
            sess[SKR_RUN] = errors
            ucontent = uquery(ocols)
            raise web.seeother('/report/run/%s?%s' %(report, ucontent))
        else:
            try:
                #python handler or sql query
                py_func = py_handler(py_r(report))
                if py_func:
                    rreport = py_func(
                                        user(), 
                                        db, 
                                        preport, 
                                        [
                                            ocols,
                                        ],
                                        PY_HANDLER_DATA
                                    )
                else:
                    rreport = db.query(rquery, vars=ocols)
            except Exception, e:
                sess[SKR_RUN] = [ [_['e_report_select_general'], str(e)] ]
                raise web.seeother('/report/run/%s' %(report))
        #
        r_row_count = -1
        r_report_result = -1
        #
        data = {
                'title': '%s - %s' %(_['tt_report_run_result'], report), 
                'command': 'report.run.result',
                'report': report,
                'header': rheader,
                'search': rsearch,
                'report2': freport,
                'headers': pheaders2,
                }
        content = rreport
        #
        xtable = hasattr(content, '__iter__')
        data['table'] = xtable
        #
        message3 = ''
        message2b = ''
        if xtable == False:
            ocols[REPORT_MESSAGE_VAR_RESULT] = content
            try:
                if content < 0:
                    message2b = message2[0]
                elif content == 0:
                    message2b = message2[1]
                elif content > 0:
                    message2b = message2[2]
                #
                message2b = string.Template(message2b)
                message3 = message2b.safe_substitute(ocols)                
            except:
                pass
        else:
            try:
                content = content.list()
            except:
                pass
            try:
                r_row_count = len(content)
            except:
                pass
            ocols[REPORT_MESSAGE_VAR_RESULT] = r_report_result
        #
        data['result_message'] = message3
        #
        ocols[REPORT_RESULT_ROW_COUNT] = r_row_count
        ocols[REPORT_RESULT_MESSAGE] = message3
        #
        pboth = [
                    [
                        pheaders, 
                        pheaders2,
                        REPORT_HEADERS_CELL_LEN,
                        REPORT_HEADERS_CELL_TYPES,
                    ],
                    [
                        pfooters, 
                        pfooters2,
                        REPORT_FOOTERS_CELL_LEN,
                        REPORT_FOOTERS_CELL_TYPES,
                    ],
                ]
        #
        for phf in pboth:
            phfx = phf[0]
            phfy = phf[1]
            phfz = phf[2]
            phft = phf[3]
            #
            if not phfx or not len(phfx) == 2:
                continue
            #
            phfx0 = phfx[0]
            phfx1 = phfx[1]
            #
            if (not phfx0) \
                or (not phfx1) \
                or (not isinstance(phfx0, list)) \
                or (not isinstance(phfx1, int)):
                    phfx0 = []
                    phfx1 = 0
            #
            for p in phfx0:
                phfl = []
                #
                for pc in p:
                    if not len(pc) == phfz:
                        continue 
                    #
                    if not isinstance(pc[0], phft[0]) \
                        or not isinstance(pc[2], phft[2]) \
                        or not isinstance(pc[1], phft[1]):
                            continue
                    #
                    if hasattr(pc[0], 'lower'):
                        pc[0] = pc[0].lower()
                    #
                    phfc = {}
                    #
                    pc2 = pc[2]
                    pc2['type'] = pc[0]
                    #
                    if pc[0] == REPORT_CELL_TYPE_TEXT:
                        if rformat in REPORT_FORMAT_ALL:
                            phfc = {
                                        'content': tr_report_text(
                                                        pc[1],
                                                        pc[2]
                                                    ),
                                        'data': pc2,
                                    }
                    elif pc[0] == REPORT_CELL_TYPE_SQL:
                        if rformat in REPORT_FORMAT_ALL:
                            phfq = pc[1]
                            phfqr = ''
                            #                            
                            try:
                                phfqr0 = db.query(phfq, vars=ocols).list()
                                phfqr1 = phfqr0[0]
                                phfqr = phfqr1.get(
                                    REPORT_CELL_TYPE_SQL_RESULT,
                                    ''
                                    )
                                if isblob(phfqr):
                                    phfqr = ''
                            except:
                                pass
                            #
                            phfc = {
                                        'content': phfqr,
                                        'data': pc2,
                                    }
                    elif pc[0] == REPORT_CELL_TYPE_FILES_IMAGE:
                        if rformat in REPORT_FORMAT_ALL:
                            phfc = {
                                        'content': str(pc[1]),
                                        'data': pc2,
                                    }                            
                    #
                    phfl.append(phfc)                        
                #
                phfl2 = [x for x in phfl if x]
                #
                if not phfl2:
                    continue
                #
                #fit to length
                if len(phfl) < phfx1:
                    phfx1d = phfx1 - len(phfl)
                    for d in range(phfx1d):
                        phfl.append({})
                #
                if phfl:
                    phfy.append(phfl)
        #
        phtempd = {
                        'type': REPORT_CELL_TYPE_TEXT,
                }
        #
        if not pheaders2:
            pheaders2.append(
                [
                    {
                        'content': freport,
                        'data': phtempd,
                    },
                    {
                        'content': reportinfo,
                        'data': phtempd,
                    },
                ]
            )
            #
            for x in rsearch:
                phtemp = []
                for y in x:
                    phtemp.append(
                        {
                            'content': y,
                            'data': phtempd,
                        }
                    )
                pheaders2.append(phtemp)
        #
        if not pfooters2:
            if r_row_count > -1:
                pfooters2.append(
                    [
                        {
                            'content': r_row_count,
                            'data': phtempd,
                        },
                        {
                            'content': _['x_row'],
                            'data': phtempd,
                        },
                    ]
                )
            if message3:
                pfooters2.append(
                    [
                        {
                            'content': message3,
                            'data': phtempd,
                        },
                        {
                            'content': '',
                            'data': phtempd,
                        },
                    ]
                )
        #
        data['headers'] = pheaders2
        data['footers'] = pfooters2
        #
        data = u_print(input, data)
        #
        stop()
        #
        if rformat == REPORT_FORMAT_CSV:
            try:
                rpt_csv_content = rpt_csv(data, content)
            except Exception, e:
                sess[SKR_RUN] = [
                                    [_['th_error'], str(e)]
                                ]
                ucontent = uquery(ocols)
                raise web.seeother('/report/run/%s?%s' %(report, ucontent))
            else:
                disposition = 'attachment; filename=' + '%s%s' %(report, CSV_SUFFIX)
                web.header('Content-Type', CSV_CTYPE)
                web.header('Content-Disposition', disposition)
                return rpt_csv_content
        #
        if rformat == REPORT_FORMAT_PDF:
            try:
                rpt_pdf_content = rpt_pdf(data, content, preport)
            except Exception, e:
                sess[SKR_RUN] = [
                                    [_['th_error'], str(e)]
                                ]
                ucontent = uquery(ocols)
                raise web.seeother('/report/run/%s?%s' %(report, ucontent))
            else:
                disposition = 'attachment; filename=' + '%s%s' %(report, PDF_SUFFIX)
                web.header('Content-Type', PDF_CTYPE)
                web.header('Content-Disposition', disposition)
                return rpt_pdf_content
        #
        return T(data, content)


class notes:
    def GET(self):
        start()
        #
        xaction = [
                    (_['cmd_calculator'], '/calculator?src=notes&sid='),
                ]
        if isadmin():
            xaction.append(
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
        inp = web.input(select=[], rowid=[], e=[], f=[])
        select = inp.select
        rowid = inp.rowid
        e = inp.e
        f = inp.f
        msg = []
        #
        updated = 0
        #
        #delete
        allx = s_select('my.notes.%s' %(user()))
        alld = [x['rowid'] for x in allx]
        for i in range(len(rowid)):
            ri = rowid[i]
            ei = e[i]
            fi = f[i]
            if (ri in alld) and (not ri in select):
                if not ei.strip() and not fi.strip():
                    select.append(ri)       
        for s in select:
            if s in alld:
                try:
                    db.delete(FORM_TBL, 
                        where='a=$a and b=$b and c=$c and rowid=$ri', 
                        vars={
                            'a': 'my', 
                            'b': 'notes', 
                            'c': user(), 
                            'ri': s
                        }
                    )
                    sev = ()
                    for a in allx:
                        if a['rowid'] == s:
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
        alld = [x['rowid'] for x in allx]
        for i in range(len(rowid)):
            ri = rowid[i]
            ei = e[i]
            fi = f[i]
            if (ri in alld) and (not ri in select) and (ei.strip() or fi.strip()):
                try:
                    db.update(FORM_TBL, where='a=$a and b=$b and c=$c and rowid=$ri',
                        e=ei,
                        f=fi,
                        vars = {
                            'a': 'my', 
                            'b': 'notes', 
                            'c': user(),
                            'ri': ri
                        }
                    )
                    updated += 1
                except:
                    pass
        #new
        allx = s_select('my.notes.%s' %(user()))
        alld = [x['rowid'] for x in allx]
        for i in range(len(e)):
            ri = rowid[i]
            if ri:
                continue
            #
            ei = e[i]
            fi = f[i]
            #
            if ei.strip() or fi.strip():
                try:
                    db.insert(FORM_TBL, a='my', b='notes', c=user(),  
                        e=ei, f=fi
                    )
                    ex = get_value1([ei.strip(), fi.strip()], '')
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


class files:
    def GET(self):
        start()
        #
        xaction = (
                    (_['cmd_view'], '/fs?sid=', '_blank'),
                    (_['cmd_download'], '/fs?download=1&sid=', '_blank'),
                )
        #
        data = {
                'title': _['tt_files'],
                'command': 'files',
                'action_url': '/files',
                'action_method': 'post',
                'action_enctype': 'multipart/form-data',
                'action_button': (
                                    ('save', _['cmd_save'], False, '', 'submit'),
                                ),
                'columns': (
                            _['x_delete'], 
                            _['x_file_name'], 
                            _['x_file_size'], 
                            _['x_shared'],
                            _['x_action'],
                        ),
                'select': 'select',
                'select_all': _['x_delete'],
                'max': 3,
                'xaction': xaction,
                'message': smsgq(SK_FILES),
                'hint': _['h_files'],
            }
        #
        content = r_files()
        #
        stop()
        return T(data, content)
    
    def POST(self):
        inp = web.input(select=[], rowid=[], d=[], f=[])
        select = inp.select
        rowid = inp.rowid
        d = inp.d
        f = inp.f
        msg = []
        #
        updated = 0
        #
        #delete
        allx = r_files()
        alld = [x['rowid'] for x in allx]
        for s in select:
            if s in alld:
                try:
                    db.delete(FORM_TBL, 
                        where='a=$a and b=$b and c=$c and rowid=$ri', 
                        vars={
                            'a': 'my', 
                            'b': 'files', 
                            'c': user(), 
                            'ri': s
                        }
                    )
                    sev = ()
                    for a in allx:
                        if a['rowid'] == s:
                            sev = [
                                        a['d'].strip(),
                                    ]
                            break
                    se = get_value1(sev, s)
                    m = (_['x_deleted'], se)
                    msg.append(m)
                except:
                    pass
        #update
        allx = r_files()
        alld = [x['rowid'] for x in allx]
        for i in range(len(rowid)):
            ri = rowid[i]
            di = d[i]
            fi = f[i]
            if (ri in alld) and (not ri in select):
                try:
                    db.update(FORM_TBL, where='a=$a and b=$b and c=$c and rowid=$ri',
                        f=fi,
                        vars = {
                            'a': 'my', 
                            'b': 'files', 
                            'c': user(),
                            'ri': ri
                        }
                    )
                    #
                    updated += 1
                except:
                    pass
        #new
        d_new = web.webapi.rawinput().get('d_new')
        if not isinstance(d_new, list):
            d_new = [d_new]
        for n in d_new:
            fname = ''
            try:
                fname = n.filename.strip()
            except:
                pass
            #
            if not fname:
                continue
            #
            max_num = 0
            max_size = 0
            if not isadmin():
                max_num = r_system('files.max_number.')
                max_size = r_system('files.max_size.')
            #
            if max_num:
                allx = r_files()
                if len(allx) >= max_num:
                    m = (_['x_max_files_number_error'], 
                            n.filename, 
                            str(max_num),
                        )
                    msg.append(m)                    
                    continue
            #
            if max_size:
                if len(n.value) >= max_size:
                    m = (_['x_max_file_size_error'], 
                            n.filename,
                            size(len(n.value)),
                            size(max_size),
                        )
                    msg.append(m)                    
                    continue
            #
            #
            g = {}
            gj = ''
            try:
                g['size'] = len(n.value)
                g['type'] = n.type
                g['type_options'] = n.type_options
                g['disposition'] = n.disposition
                g['disposition_options'] = n.disposition_options
                g['raw'] = 1
                #
                gj = json.dumps(g)
            except:
                pass
            #
            try:
                n_value = n.value
                if isblob(n_value):
                    n_value2 = db.db_module.Binary(n_value)
                else:
                    n_value2 = n_value
                #
                db.insert(FORM_TBL, a='my', b='files', c=user(),  
                    d=n.filename, 
                    e=n_value2, 
                    f='0',
                    g=gj,
                )
                m = (_['x_added'], n.filename)
                msg.append(m)
            except:
                pass
        #
        if updated:
            m = (_['o_files'],)
            msg.append(m)
        #        
        sess[SK_FILES] = msg
        raise web.seeother('/files')


class fs:
    def GET(self):
        inp = web.input(sid='', download='')
        sid = inp.sid.strip()
        download = inp.download.strip()
        #
        test = r_fs_ok(sid)
        if not test:
            raise web.notfound()
        #
        ft = ''
        fn = ''
        fc = ''
        try:
            fn, ft, fc = r_fs_content(sid)
        except:
            dflt()
        #
        if download == '1':
            disposition = 'attachment; filename=' + fn
        else:
            disposition = 'inline; filename=' + fn
        #
        web.header('Content-Type', ft)
        web.header('Content-Disposition', disposition)
        return fc


class pages:
    def GET(self):
        start()
        #
        data = {
                'title': _['tt_pages'],
                'command': 'pages',
                'action_url': '/pages',
                'action_method': 'post',
                'action_button': (
                                    ('save', _['cmd_save'], False, '', 'submit'),
                                ),
                'columns': (
                            _['x_code'], 
                            _['x_preview'], 
                        ),                                
                'message': smsgq(SK_PAGES),
                'url': '/page/%s' %(user()),
                'hint': _['h_pages'],
            }
        #
        q = 'my.pages.%s.home' %(user())
        page = s_check2(q, '')
        #
        content = ['', '']
        if page:
            content[0] = page.get('e', '')
            content[1] = tr_page(content[0])
        #
        stop()
        return T(data, content)
    
    def POST(self):
        inp = web.input(content='')
        content = inp.content
        #
        q = 'my.pages.%s.home' %(user())
        #
        try:
            if s_select(q):
                r = db.update(FORM_TBL, 
                        e=striphtml(content), 
                        where=' a=$a and b=$b and c=$c and d=$d ',
                        vars = {
                                    'a': 'my',
                                    'b': 'pages',
                                    'c': user(),
                                    'd': 'home',
                                }
                    )
            sess[SK_PAGES] = _['o_pages']
        except:
            sess[SK_PAGES] = _['e_pages']
        #
        raise web.seeother('/pages')


class page:
    def GET(self, u):
        start()
        #
        allu = s_select('user.account')
        users = [x['d'] for x in allu]
        #
        u = u.strip()
        if not u or not u in users: 
            dflt()
        #
        q = 'my.pages.%s.home' %(u)
        p = s_select(q)
        if not p:
            dflt()
        #
        content = ''
        if p:
            p = p[0]
            content = p.get('e', '')
        #
        if not content.strip():
            dflt()
        #
        data = {
                    'command': 'page',
                    'title': u,
                }
        content = tr_page(content)
        #
        stop()
        return T(data, content)

class calculator:
    def GET(self):
        start()
        #
        inp = web.input(src='', sid='')
        q = ''
        #
        if not isnosb():
            notes = s_select('my.notes.%s' %(user()))
            alld = [x['rowid'] for x in notes]
            if inp.src == 'notes' and inp.sid in alld:
                for n in notes:
                    if n['rowid'] == inp.sid:
                        q = n['f']
                        break
        #
        data = {
            'title': '%s' %(_['tt_calculator']),
            'command': 'calculator',
            'action_url': '/calculator',
            'action_method': 'post',
            'action_button': (
                                ('calculate', _['cmd_calculate'], False, '', 'submit'),
                            ),
            'hint': _['h_calculator'],
            'max_input': CALCULATOR_MAX_INPUT,
            'message': smsgq(SK_CALCULATOR),
            'calculator': q,
        }
        content = ''
        stop()
        return T(data, content)
        
    def POST(self):
        q = web.input(q='').q.strip()
        q0 = q
        q = re.compile('\s+', re.M).sub('', q)
        if not q:
            raise web.seeother('/calculator')
        #
        error = 1
        #
        start()
        try:
            if len(q) > CALCULATOR_MAX_INPUT:
                raise Exception, _['x_expression_too_long']
            #
            for e in q:
                if not e in CALCULATOR_ALLOWED:
                    raise Exception, _['x_expression_invalid']
            #
            q2 = 'select $e'
            msg = db.query(q2, 
                        vars = {
                                'e': web.sqlliteral(q),
                            }
                    )
            msg = msg[0].get(q, '')
            err = _['th_ok']
            error = 0
        except Exception, e:
            msg = e.message
            err = _['th_error']
            error = 1
        #
        stop()
        t = rt()
        #
        sess[SK_CALCULATOR] = [q0, err, msg, t, error]
        raise web.seeother('/calculator')


class admin_scripts:
    def GET(self):
        start()
        #
        data = {
                'title': _['tt_scripts'],
                'command': 'scripts',
                'action_url': '/admin/scripts',
                'action_method': 'post',
                'action_enctype': 'multipart/form-data',
                'action_button': (
                                    ('save', _['cmd_save'], False, '', 'submit'),
                                ),
                'columns': (
                            _['x_name'], 
                            _['x_info'], 
                            _['x_author'], 
                            _['x_license'], 
                            _['x_run_time'],
                        ),                                
                'message': smsgq(SK_SCRIPTS),
                'hint': _['h_scripts'],
            }
        #
        content = r_scripts()
        #
        stop()
        return T(data, content)

    def POST(self):
        inp = web.input(d_new={})
        d_new = inp.d_new
        #
        if not hasattr(d_new, 'filename'):
            raise web.seeother('/admin/scripts')
        #
        fname = d_new.filename
        if not fname:
            raise web.seeother('/admin/scripts')
        #
        code = ''
        dcode = {}
        sname = ''
        g = {}
        msg = []
        #
        try:
            code = d_new.value
            size = len(code)
            smax = r_system('scripts.max_size.')
            #
            if size > smax:
                raise Exception, _['e_scripts_max_size']
            #
            dcode = json.loads(code)
            #
            for k in SCRIPT_REQ:
                if not dcode.has_key(k):
                    raise Exception, _['e_scripts_syntax_or_required']
            #
            g['size'] = size
            g['type'] = d_new.type
            g['type_options'] = d_new.type_options
            g['disposition'] = d_new.disposition
            g['disposition_options'] = d_new.disposition_options            
        except Exception, e:
            msg = [
                    [ fname, str(e) ],
                ]
            sess[SK_SCRIPTS] = msg
            raise web.seeother('/admin/scripts')
        #
        sname = dcode.get(SCRIPT_KEY_NAME, '')
        if isstr(sname):
            sname = sname.strip()
        if not isstr(sname) or not sname:
            msg = [
                    [ _['e_scripts_name'] ],
                ]
            sess[SK_SCRIPTS] = msg
            raise web.seeother('/admin/scripts')            
        #
        try:
            g['user'] = user()
            #            
            gj = json.dumps(g)
            #
            r = db.insert(FORM_TBL, 
                    a='install',
                    b='scripts',
                    c='',
                    d='',
                    e=code,
                    f='',
                    g=gj
                )
            #
            msg = [
                    [ _['o_scripts'] ],
                ]
            sess[SK_SCRIPTS] = msg            
        except:
            pass
        #
        raise web.seeother('/admin/scripts')


class admin_script:
    def GET(self, script):
        start()
        #
        try:
            itest = int(script)
        except:
            dflt()
        #
        scode = g_script(script)
        if not scode:
            dflt()
        #
        action_button = (
                            ('run', _['cmd_run'], False, '', 'submit'),
                        )
        #
        run = str(scode.get('f', ''))
        content = xparsescript(scode)
        #
        if not xokscript(content):
            action_button = ()
            if not sess.get(SK_SCRIPT):
                sess[SK_SCRIPT] = [
                                    [
                                        _['x_script_not_runnable'],
                                    ],
                                ]
        #
        table_detail = {}
        try:
            ctables = content.get(SCRIPT_KEY_TABLES)
            for c in ctables:
                if c[1] == SCRIPT_TABLE_COLUMN_CONFLICT:
                    table_detail[c[0]] = c[4]
                elif c[1] == SCRIPT_TABLE_EXISTS:
                    table_detail[c[0]] = c[3]
                elif c[1] == SCRIPT_TABLE_OK:
                    table_detail[c[0]] = c[3]
        except:
            pass
        #
        profile_info = []
        try:
            profile_info0 = content.get(SCRIPT_KEY_PROFILES)
            profile_info = [x[0] for x in profile_info0 if validfname(x[0])]
        except:
            pass
        #
        ecode = str(scode.get('e', ''))
        #
        data = {
                'title': _['tt_script'],
                'command': 'script',
                'action_url': '/admin/script/%s' %(script,),
                'action_method': 'post',
                'action_enctype': 'multipart/form-data',
                'action_button': action_button,
                'columns': (
                            _['x_key'], 
                            _['x_detail'], 
                            _['x_system_check'], 
                        ),                                
                'info': (
                            (_['x_name'], SCRIPT_KEY_NAME),
                            (_['x_info'], SCRIPT_KEY_INFO),
                            (_['x_author'], SCRIPT_KEY_AUTHOR),
                            (_['x_license'], SCRIPT_KEY_LICENSE),
                        ),
                'table_info': {
                                SCRIPT_TABLE_ERROR: _['th_error'],
                                SCRIPT_TABLE_COLUMN_CONFLICT: _['e_script_column_conflict'],
                                SCRIPT_TABLE_OK: _['th_ok'],
                                SCRIPT_TABLE_EXISTS: _['x_table_exists'],
                            },
                'form_info': {
                                SCRIPT_FORM_ERROR: _['th_error'],
                                SCRIPT_FORM_OK: _['th_ok'],
                                SCRIPT_FORM_EXISTS: _['e_form_edit_exists'],
                            },
                'report_info': {
                                SCRIPT_REPORT_ERROR: _['th_error'],
                                SCRIPT_REPORT_OK: _['th_ok'],
                                SCRIPT_REPORT_EXISTS: _['e_report_edit_exists'],
                            },                            
                'profile_info': {
                            },
                'table_detail': table_detail,
                'run': run,
                'code': ecode,
                'message': smsgq(SK_SCRIPT),
                'hint': _['h_script'],
            }
        #
        stop()
        return T(data, content)

    def POST(self, script):
        inp = web.input()
        #
        itest = -1
        try:
            itest = int(script)
        except:
            dflt()
        #
        scode = g_script(script)
        if not scode:
            dflt()
        #
        url = '/admin/script/%s' %(script,)
        #        
        content = xparsescript(scode)
        if not xokscript(content):
            sess[SK_SCRIPT] = [
                                [
                                    _['th_error'],
                                    _['x_script_not_runnable'],
                                ],
                            ]
            raise web.seeother(url)
        #
        msg = []
        script_trans = db.transaction() 
        oldtables = tables()
        oldtables = [x.lower() for x in oldtables]
        newtables = []
        newforms = []
        newreports = []
        try:
            stables = content.get(SCRIPT_KEY_TABLES)
            for tt in stables:
                tname = tt[0]
                tstat = tt[1]
                tcols = tt[2]
                ncols = tt[3]
                xcols = tt[4]
                #
                if tstat == SCRIPT_TABLE_EXISTS:
                    for n in ncols:
                        q = 'alter table %s add column %s %s' %(
                            tname,
                            n[0],
                            n[1],
                        )
                        r = db.query(q)
                        if r:
                            msg.append(
                                        [
                                            _['o_column'],
                                            tname,
                                            n[0],
                                            n[1],
                                        ]
                            )
                elif tstat == SCRIPT_TABLE_OK:
                    newcols = []
                    newpk = []
                    #
                    for n in tcols:
                        if n[2] == 1: #primary key
                            newcols.append(
                                '%s %s' %(
                                            n[0],
                                            n[1],
                                        )
                            )
                            newpk.append(n[0])
                        elif n[2] == 0:
                            newcols.append(
                                '%s %s' %(
                                            n[0],
                                            n[1],
                                        )
                            )
                        else:
                            for v in SCRIPT_VALID_COLUMN_FLAG:
                                if v[0] and (n[1] in v[0]) and (n[2] == v[1]):
                                    newcols.append(
                                        '%s %s %s' %(
                                                        n[0],
                                                        n[1],
                                                        v[2],
                                                    )
                                    )
                                    break
                        #
                    if newpk:
                        q = 'create table %s(%s, primary key(%s))' %(
                            tname,
                            ','.join(newcols),
                            ','.join(newpk),
                        )
                    else:
                        q = 'create table %s(%s)' %(
                            tname,
                            ','.join(newcols),
                        )                        
                    #
                    r = db.query(q)
                    if r:
                        msg.append(
                                    [
                                        _['o_table_create'],
                                        tname,
                                    ]
                        )
                        newtables.append(tname)
            #
            #
            sforms = content.get(SCRIPT_KEY_FORMS)
            for tt in sforms:
                tname = tt[0]
                tstat = tt[1]
                tcont = tt[2]
                jcont = tt[3]
                #
                if tstat == SCRIPT_FORM_OK:
                    if tname.lower() in newforms:
                        continue
                    #
                    r = db.insert(FORM_TBL,
                            a='form',
                            b='code',
                            d=tname.lower(),
                            e=jcont
                        )
                    if r:
                        msg.append(
                                    [
                                        _['o_form_create'],
                                        tname,
                                    ]
                        )                        
                        newforms.append(tname.lower())
            #
            #
            sreports = content.get(SCRIPT_KEY_REPORTS)
            for tt in sreports:
                tname = tt[0]
                tstat = tt[1]
                tcont = tt[2]
                jcont = tt[3]
                #
                if tstat == SCRIPT_REPORT_OK:
                    if tname.lower() in newreports:
                        continue
                    #
                    r = db.insert(FORM_TBL,
                            a='report',
                            b='code',
                            d=tname.lower(),
                            e=jcont
                        )
                    if r:
                        msg.append(
                                    [
                                        _['o_report_create'],
                                        tname,
                                    ]
                        )
                        newreports.append(tname.lower())
            #
            sprofiles = content.get(SCRIPT_KEY_PROFILES)
            juprofiles = r_system('users.profile.')
            try:
                try:
                    uprofiles = json.loads(juprofiles)
                except:
                    uprofiles = []
                nprofiles = uprofiles + sprofiles
                jnprofiles = json.dumps(nprofiles, indent=JSON_INDENT)
                r = s_save('users.profile..%s' %(jnprofiles))
                if r:
                    for i in sprofiles:
                        msg.append(
                                    [
                                        _['o_profile_set'],
                                        i[0],
                                    ]
                        )
                
            except:
                pass
            #
            db.update(FORM_TBL, where='rowid=$script', 
                f=sqliteboy_time3(sqliteboy_time()),
                vars = {
                    'script': itest,
                }
            )
        except Exception, e:
            msg.append(
                        [
                            _['th_error'],
                            str(e),
                        ],
            )
            #
            if newtables:
                try:
                    for t in newtables:
                        if t.lower() in oldtables:
                            continue
                        #
                        if db.select(t).list():
                            continue
                        #
                        q = 'drop table %s' %(t)
                        db.query(q)
                        #
                        msg.append(
                                    [
                                        _['o_drop'],
                                        t,
                                    ]
                        )
                except:
                    pass
            #
            msg.append(
                        [
                            _['e_script']
                        ],
            )
            script_trans.rollback()
        else:
            msg.append(
                        [
                            _['o_script']
                        ],
            )
            script_trans.commit()
        #
        sess[SK_SCRIPT] = msg
        #
        raise web.seeother(url)


class table_copy:
    def GET(self):
        start()
        #
        table = web.input(table='').table
        if not table in tables(): 
            dflt()
        #
        excludes = COPY_TARGET_EXCLUDE[:]
        excludes.append(table)
        target = tables(exclude=excludes)
        #
        action_button = (
                            ('copy', _['cmd_copy'], False, '', 'submit'),
                        )
        if not target:
            action_button = ()
        #
        data = {
                'title': _['tt_copy'],
                'command': 'copy',
                'action_url': '/table/copy',
                'action_method': 'post',
                'action_enctype': 'multipart/form-data',
                'action_button': action_button,
                'table': table,
                'target': web.form.Dropdown('target', target),
                'message': smsgq(SKT_M_COPY),
                'hint': _['h_copy'],
            }
        #
        content = ''
        #
        stop()
        return T(data, content)

    def POST(self):
        inp = web.input(table='', target='')
        table = inp.table.lower().strip()
        target = inp.target.lower().strip()
        #
        if not table or not target:
            dflt()
        #
        if target == table:
            dflt()
        #
        if target in COPY_TARGET_EXCLUDE:
            dflt()
        #        
        oldtables = tables()
        oldtables = [x.lower() for x in oldtables]
        if not table in oldtables or not target in oldtables:
            dflt()
        #
        scols = columns(table)
        tcols = columns(target)
        if not scols or not tcols:
            dflt()
        #
        sdcols = {}
        tdcols = {}
        sall = (
                (
                    scols,
                    sdcols, 
                ),
                (
                    tcols,
                    tdcols,
                ),
            )
        for a in sall:
            s = a[0]
            d = a[1]
            #
            for c in s:
                cname = c.get('name').lower()
                ctype = c.get('type').lower()
                if cname and ctype:
                    d[cname] = ctype
        #
        ncols = []
        for d in tdcols.keys():
            if sdcols.has_key(d):
                sd = sdcols.get(d)
                td = tdcols.get(d)
                if sd and td:
                    if sd == td:
                        ncols.append(d)
        #
        ncols = [x for x in ncols if validfname(x)]
        ncols.sort()
        #
        msg = [
                [
                    _['x_column'],
                    ','.join(ncols), 
                ]
            ]
        #
        try:
            if not ncols:
                raise Exception, _['x_copy_columns_none']
            #
            q = '''
                insert into %s (%s) select %s from %s
                ''' %(
                        target,
                        ','.join(ncols),
                        ','.join(ncols),
                        table,
                    )
            r = db.query(q)
            msg.append(
                        [
                            _['o_copy'],
                            target,
                            _['x_row'],
                            str(r),
                        ]
            )

        except Exception, e:
            msg.append(
                        [
                            _['e_copy'],
                            str(e),
                        ]
            )
        #
        sess[SKT_M_COPY] = msg
        #
        raise web.seeother('/table/copy?table=' + table)


class table_empty:
    def GET(self):
        start()
        #
        table = web.input(table='').table
        table = str(table)
        table = table.lower().strip()
        #
        if not table in tables(): 
            dflt()
        #
        if table in EMPTY_EXCLUDE:
            dflt()
        #
        data = {
            'title': '%s - %s' %(table, _['tt_empty']),
            'command': 'empty',
            'table': table,
            'hidden': (('table', table), ('confirm', '1')),
            'action_url': '/table/empty',
            'action_method': 'post',
            'action_button': (
                                ('empty', _['cf_empty'], False, '', 'submit'),
                            ),
            'message': smsg(table, SKT_M_EMPTY),
            'hint': _['h_empty'],
        }
        #
        content = ''
        #
        stop()
        return T(data, content)
        
    def POST(self):
        input = web.input(table='', confirm='')
        table = input.table.lower().strip()
        confirm = input.confirm.strip()
        if not table in tables() or not confirm: 
            dflt()
        #
        if table in EMPTY_EXCLUDE:
            dflt()
        #
        msg = []
        #
        q = 'delete from %s' %(table)
        try:
            r = db.query(q)
            msg = [
                    [
                        _['o_empty'],
                        str(r),
                    ]
                ]
        except Exception, e:
            msg = [
                    [
                        _['e_empty'],
                        str(e),
                    ]
                ]
        #
        sess.table[table][SKT_M_EMPTY] = msg
        #
        redir = '/table/empty?table=%s' %(table)
        raise web.seeother(redir)


class vacuum:
    def GET(self):
        start()
        #
        data = {
            'title': '%s' %(_['tt_vacuum']),
            'command': 'vacuum',
            'hidden': (('confirm', '1'),),
            'action_url': '/vacuum',
            'action_method': 'post',
            'action_button': (
                                ('vacuum', _['cf_vacuum'], False, '', 'submit'),
                            ),
            'message': smsgq(SKV),
            'info': [
                        [
                            _['x_database_size'],
                            size(),
                        ],
                        [
                            _['x_unused_pages'],
                            p_pragma(
                                PRAGMA_FREELIST_COUNT, 
                                default=DEFAULT_ERROR_INT
                            ),
                        ],
                    ],
            'hint': _['h_vacuum'],
        }
        #
        content = ''
        #
        stop()
        return T(data, content)
    
    def POST(self):
        inp = web.input(confirm='')
        confirm = inp.confirm.strip()
        #
        if not confirm:
            dflt()
        #
        msg = []
        #
        q = 'vacuum'
        try:
            r = db.query(q)
            msg = [
                    [
                        _['o_vacuum'],
                    ]
                ]
        except Exception, e:
            msg = [
                    [
                        _['th_error'],
                        str(e),
                    ]
                ]
        #
        sess[SKV] = msg
        #
        raise web.seeother('/vacuum')


class form_shortcut:
    def GET(self, form):
        start()
        #
        form = form.strip().lower()
        if not form or not form in forms():
            dflt()
        #
        if not canform(FORM_KEY_SECURITY_RUN, form):
            dflt()
        #
        if not validfname(form):
            dflt()
        #
        res = shortcut(SHORTCUT_TYPE_FORM, form)
        #
        data = {
                }
        content = ''
        #
        stop()
        #
        if not res:
            dflt()
        else:
            raise web.seeother('/?form=%s' %(form))


class report_shortcut:
    def GET(self, report):
        start()
        #
        report = report.strip().lower()
        if not report or not report in reports():
            dflt()
        #
        if not canreport(REPORT_KEY_SECURITY_RUN, report):
            dflt()
        #
        if not validfname(report):
            dflt()
        #
        res = shortcut(SHORTCUT_TYPE_REPORT, report)
        #
        data = {
                }
        content = ''
        #
        stop()
        #
        if not res:
            dflt()
        else:
            raise web.seeother('/?report=%s' %(report))


class table_import_csv:
    def GET(self):
        start()
        #
        table = web.input(table='').table
        table = str(table)
        table = table.strip().lower()
        #
        if not table in tables(): 
            dflt()
        #
        if table in IMPORT_EXCLUDE:
            dflt()
        #
        data = {
            'title': '%s - %s' %(table, _['tt_import_csv']),
            'command': 'import',
            'table': table,
            'hidden': (('table', table),),
            'action_enctype': 'multipart/form-data',
            'action_url': '/table/import/csv',
            'action_method': 'post',
            'action_button': (
                                ('import', _['cmd_import_csv'], False, '', 'submit'),
                            ),
            'message': smsg(table, SKT_M_IMPORT),
            'hint': _['h_import_csv'],
        }
        #
        content = ''
        #
        stop()
        return T(data, content)
        
    def POST(self):
        inp = web.input(table='', f={})
        table = inp.table.strip().lower()
        f = inp.f
        #
        redir = '/table/import/csv?table=%s' %(table)        
        #
        if not table in tables(): 
            dflt()
        #
        if table in IMPORT_EXCLUDE:
            dflt()
        #
        try:
            if not f.value.strip():
                raise Exception
        except:
            raise web.seeother(redir)
        #
        cols = columns(table, True)
        if not cols:
            dflt()
        #
        msg = []
        counter = 0
        #
        x1 = ','.join(cols)
        c2 = ['$'+x for x in cols]
        x2 = ','.join(c2)
        #
        t = db.transaction()
        try:
            reader = csv.DictReader(f.file)
            for i in reader:
                if reader.line_num == 1: #header:
                    continue
                #
                i2 = {}
                for k in i.keys():
                    if isstr(k):
                        i2[k.lower()] = i.get(k)
                #
                v = {}
                for k in cols:
                    if not i2.has_key(k):
                        continue
                    v[k] = i2.get(k)
                #
                if not v.keys():
                    continue
                #
                for k in cols:
                    if not v.has_key(k):
                        v[k] = None
                #
                q = 'insert into %s(%s) values(%s)' %(
                        table,
                        x1,
                        x2
                    )
                r = db.query(q, vars=v)
                if r:
                    counter += 1
            #
            t.commit()
            #
            msg = [
                    [
                        _['o_import_csv'],
                        _['x_row'],
                        str(counter),
                    ]
                ]            
        except Exception, e:
            t.rollback()
            msg = [
                    [
                        _['e_import_csv'],
                        str(e),
                    ]
                ]            
        #
        sess.table[table][SKT_M_IMPORT] = msg
        #
        raise web.seeother(redir)        


class profile:
    def GET(self):
        start()
        #
        data = {
            'title': '%s' %(_['tt_profile']),
            'command': 'profile',
            'action_enctype': 'multipart/form-data',
            'action_url': '/profile',
            'action_method': 'post',
            'action_button': (
                                ('save', _['cmd_save'], False, '', 'submit'),
                            ),
            'message': smsgq(SK_PROFILE),
            'hint': _['h_profile'],
        }
        #
        content = [
                    pr_all(),
                ]
        #
        stop()
        return T(data, content)
        
    def POST(self):
        inp = web.input()
        #
        msg = []
        p = {}
        #
        a = pr_all()
        for i in a:
            name = i[0]
            func = i[6]
            if inp.has_key(name):
                value = inp.get(name)  
                try:
                    value = func(value)
                except:
                    pass
                p[name] = value
        #
        try:
            p = json.dumps(p)
            r = db.update(FORM_TBL, g=p, 
                    where='a=$a and b=$b and d=$d',
                    vars={
                        'a': 'user',
                        'b': 'account',
                        'd': user(),
                    }
                )
            msg = [
                    [
                        _['o_profile'],
                    ]
                ]                        
        except:
            msg = [
                    [
                        _['e_profile'],
                    ]
                ]                        
        #
        sess[SK_PROFILE] = msg
        #
        raise web.seeother('/profile')


class table_schema:
    def GET(self):
        start()
        #
        table = web.input(table='').table
        if not table in tables(): 
            dflt()
        #
        target = web.input(target='').target
        #
        data = {
                'title': '%s - %s' %(table, _['tt_schema']),
                'command': 'schema',
                'action_url': '/table/schema',
                'action_method': 'post',
                'action_enctype': 'multipart/form-data',
                'action_button': (
                                    ('create', _['cmd_table_create'], False, '', 'submit'),
                                ),
                'table': table,
                'target': target,
                'message': smsgq(SK_SCHEMA),
                'hint': _['h_create'],
            }
        #
        content = r_schema(table)
        #
        stop()
        return T(data, content)

    def POST(self):
        inp = web.input(table='', target='')
        table = inp.table.strip().lower()
        target = inp.target.strip().lower()
        #
        if not table:
            dflt()
        #
        oldtables = tables()
        oldtables = [x.lower() for x in oldtables]
        if not table in oldtables:
            dflt()
        #
        redir = '/table/schema?table=%s&target=%s' %(table, target)
        #
        if not target:
            raise web.seeother(redir)
        #
        if target == table or target in oldtables:
            sess[SK_SCHEMA] = [
                                [
                                    _['e_table_exists'],
                                ],
                            ]
            raise web.seeother(redir)
        #
        if hasws(target):
            sess[SK_SCHEMA] = [
                                [
                                    _['z_table_whitespace'],
                                ],
                            ]
            raise web.seeother(redir)
        #
        schema = str(r_schema(table))
        x = schema.find('(')
        if x < 0:
            raise web.seeother(redir)
        #
        cols = schema[x:]
        q = 'create table %s %s' %(target, cols)
        try:
            r = db.query(q)
        except Exception, e:
            sess[SK_SCHEMA] = [
                                [
                                    _['th_error'],
                                    str(e),
                                ],
                            ]
            raise web.seeother(redir)
        else:
            raise web.seeother('/table/browse/%s' %(target))
        #
        dflt()
        

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
    #server command check
    scmd_ret = 0
    try:
        scmd = sys.argv[3].split(SERVER_COMMAND_SEPARATOR)
        if not scmd:
            raise Exception
        #
        scmd = [x.lower() for x in scmd if x.strip()]
        scmd0 = scmd[0]
        if not scmd0 in SERVER_COMMAND_ALL.keys():
            raise Exception
        #
        sfuncn = SERVER_COMMAND_ALL.get(scmd0)
        sfunc = globals().get(sfuncn)
        if not callable(sfunc):
            raise Exception
        #
        log(_['x_server_command_mode'])
        log(_['x_please_wait'])
        log(scmd0)
        sret = sfunc(scmd)
        #
        if sret:
            log(sret)
            scmd_ret = 3
        else:
            scmd_ret = 4
    except:
        pass
    #
    if scmd_ret:
        sys.exit(scmd_ret)
    #
    if c_db_static(dbfile):
        log(dbfile, stream=sys.stderr)
        log(_['e_db_static'], stream=sys.stderr)
        sys.exit(5)
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
    app.add_processor(proc_account_check)
    app.add_processor(proc_misc)
    #
    xupdate_all = [
                        [
                            s_isold,
                            _['x_sqliteboy_x_update'],
                            s_xupdate,
                        ],
                    ]
    for x in xupdate_all:
        if x[0]():
            log('')
            log(x[1])
            xupdate = x[2]()
            if xupdate:
                log('%s: %s %s' %(
                    _['th_ok'],
                    str(xupdate),
                    _['x_row'],
                    )
                )
            else:
                log(_['th_error'])
            log('')
    #
    web.httpserver.runsimple(app.wsgifunc(), (DEFAULT_ADDR, port))
    
