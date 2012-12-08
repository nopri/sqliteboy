#!/usr/bin/env python
#
#
# sqliteboy.py
# Simple Web SQLite Manager/Form Application
# (c) Noprianto <nop@tedut.com>
# 2012
# GPL
#
# Please read README.txt
#

#----------------------------------------------------------------------#
# APPLICATION                                                          #
#----------------------------------------------------------------------#
NAME = 'sqliteboy'
VERSION = '0.02'
WSITE = 'https://github.com/nopri/%s' %(NAME)
TITLE = NAME + ' ' + VERSION
DBN = 'sqlite'
FORM_TBL = '_sqliteboy_'
FORM_URL_INIT = '/sb/init'
FORM_FIELDS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
FORM_FIELD_TYPE = 'text'
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
DFLT_VALUE = 'dflt_value'
MARK_CURRENT = '&#9658' #unused
NAME_SELECT = 'select'
EXCLUDE_TABLE = []
SIZE_KB = 1024
SIZE_MB = 1024 * SIZE_KB
SIZE_GB = 1024 * SIZE_MB
BLOB_TYPE = ['blob']
TEXT_TYPE = ['text', 'clob']
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
URL_README = ('/sb/readme', 'sb_readme', 'README.txt')
URL_SOURCE = ('/sb/source', 'sb_source', __file__)


#----------------------------------------------------------------------#
# MODULE                                                               #
#----------------------------------------------------------------------#
import sys
import os
CURDIR = os.path.dirname(__file__)

import time
import decimal
import random
import string
import socket

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
    '/table/create', 'table_create',
    '/query', 'query',
    '/table/row/(.*)', 'table_row',
    '/table/blob/(.*)', 'table_blob',
    '/table/save', 'table_save',
    FORM_URL_INIT, 'sb_init',
    URL_README[0], URL_README[1],
    URL_SOURCE[0], URL_SOURCE[1],
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
        'table': {}
    }
allow = ''


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
            'x_not_enabled': 'not enabled',
            'x_version': 'version',
            'x_sqlite_version': 'SQLite version',
            'x_web_version': 'web.py version',
            'x_extended_features': 'extended features',
            'tt_insert': 'insert',
            'tt_edit': 'edit',
            'tt_column': 'column',
            'tt_rename': 'rename',
            'tt_drop': 'drop',
            'tt_query': 'query',
            'tt_create': 'create',
            'tt_readme': 'readme',
            'tt_source': 'source',
            'th_error': 'ERROR',
            'th_ok': 'OK',
            'cmd_browse': 'browse',
            'cmd_insert': 'insert',
            'cmd_column': 'column',
            'cmd_rename': 'rename',
            'cmd_table_drop': 'drop',
            'cmd_table_create': 'create',
            'cmd_query': 'query',
            'cmd_delete_selected': 'delete selected',
            'cmd_edit_selected': 'edit selected',
            'cmd_download': 'download',
            'cmd_edit': 'edit',
            'cmd_add': 'add',
            'cmd_next': 'next',
            'cmd_enable_sqliteboy': 'create %s table and enable extended features' %(FORM_TBL),
            'cmd_readme': 'readme',
            'cmd_source': 'source',
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
            'o_insert': 'OK: insert into table',
            'o_edit': 'OK: update table',
            'o_column': 'OK: alter table (column)',
            'o_rename': 'OK: alter table (rename)',
            'h_insert': 'hint: leave blank to use default value (if any)',
            'h_edit': 'hint: for blob field, leave blank = do not update',
            'h_column': 'hint: only add column is supported in SQLite. Primary key/unique is not allowed in column addition. Default value(s) must be constant.',
            'h_rename': '',
            'h_drop': '',
            'h_query': 'hint: only one statement at a time is supported',
            'h_create': 'hint: please do not put whitespace in table name',
            'h_create2': 'hint: for multiple primary keys, do not select type contains "primary key". Use primary key column instead. Currently, default value(s) must be constant (sorry).',
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
# FUNCTION                                                             #
#----------------------------------------------------------------------#
def proc_access(handle):
    #NOTIMPL: quick hack as of 30-nov-2012
    allowed = ['127.0.0.1', socket.gethostbyname(socket.gethostname())]
    ip = web.ctx.ip
    if ip in allowed:
        return handle()
    #
    return _['e_access_forbidden']

def allows():
    #NOTIMPL: quick hack as of 30-nov-2012
    global allow
    allow = _['a_local']
    return allow

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
    f = web.form.Dropdown(
        name='table', 
        args=tables(first_blank=True), 
        )
    #
    ret = (
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
                ['table_create', _['cmd_table_create']],
                ['query', _['cmd_query']],
            )
        ],

    )
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
    
def sysinfo():
    s_a = '%s %s %s' %(VERSION, link(URL_README[0], _['cmd_readme']), 
        link(URL_SOURCE[0], _['cmd_source']))
    #
    s_sb0 = _['x_extended_features']
    if not FORM_TBL in tables():
        s_sb1 = _['x_not_enabled']
        s_sb2 = link(FORM_URL_INIT, _['cmd_enable_sqliteboy'])
    else:
        s_sb1 = _['x_enabled']
        s_sb2 = ''
    s_sb = (s_sb0, '%s %s' %(s_sb1, s_sb2))
    #
    ret = (
            (_['x_version'], s_a),
            (_['x_sqlite_version'], db.db_module.sqlite_version),
            (_['x_web_version'], web.__version__),
            s_sb,
        )
    #
    return ret

def s_init():
    af = [x + ' ' + FORM_FIELD_TYPE for x in FORM_FIELDS]
    cmd = 'CREATE TABLE %s(%s)' %(FORM_TBL, ','.join(af))
    db.query(cmd)
    prepsess()


#----------------------------------------------------------------------#
# TEMPLATE                                                             #
#----------------------------------------------------------------------#
T_BASE = '''$def with (data, content)
<!DOCTYPE html>
<html>
<head>
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
<td align='right' width='12%'>$_['x_allow']: $allows()</td>
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
    <td>
    $i[2].capitalize()
    </td>
    <td width='25%'>
    $if data.has_key('table'):
        $i[3].set_value(data['table'])
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
    <pre>
    $:content
    </pre>
$else:
    $:content
</body>
</html>
'''
test_t_base = os.path.join(CURDIR, DEFAULT_T_BASE)
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
    'allows'    : allows,
    }
T = web.template.Template(T_BASE, globals=GLBL)


#----------------------------------------------------------------------#
# CLASS                                                                #
#----------------------------------------------------------------------#
class index:
    def GET(self):
        start()
        stop()
        data = {'title': '', 'command': 'home'}
        content = (
                    '%s <a href="%s">%s</a>' %(_['x_welcome2'], WSITE, NAME),
                    sysinfo(),
                )
        return T(data, content)


class favicon_ico:
    def GET(self):
        return ''
        

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
            ('table_create', '/table/create'),
            ('query', '/query'),
        )
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


class query:
    def GET(self):
        start()
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


class sb_init:
    def GET(self):
        s_init()
        dflt()
     
        
class sb_readme:
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


class sb_source:
    def GET(self):
        start()
        data = {
                'title': _['tt_source'],
                'command': 'source',
            }
        content = web.htmlquote(open(os.path.join(CURDIR, URL_SOURCE[2])).read())
        stop()
        return T(data, content)


#----------------------------------------------------------------------#
# MAIN                                                                 #
#----------------------------------------------------------------------#
if __name__ == '__main__':
    log(TITLE)
    if len(sys.argv) < 2:
        log('%s %s' %(sys.argv[0], _['usage']))
        sys.exit(1)
    #
    dbfile0 = sys.argv[1]
    dbfile = os.path.abspath(dbfile0)
    #
    try:
        port = int(sys.argv[2])
    except:
        port = DEFAULT_PORT
    #
    try:
        db = web.database(dbn=DBN, db=dbfile)
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
    app.add_processor(proc_access)
    #
    sess = web.session.Session(app, MemSession(), initializer = sess_init)
    prepsess()
    #
    web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', port))
    
