sqliteboy.py
Simple Web SQLite Manager/Form Application
(c) Noprianto <nop@tedut.com>
2012 
GPL
version 0.11


SCREENSHOTS: https://github.com/nopri/sqliteboy/wiki
(not up-to-date)


FEATURES:
- Work with single SQLite database file
- Single python file
- Configurable port 
  (default 11738 because it looks like sqliteboy)
- Browse table
  - Sort (asc/desc)
  - Download for BLOB type (if not NULL)
  - Multiple selection
  - Delete selected
  - Edit selected
  - Maintain last selected row(s)
  - Limit rows
- Insert into table
  - Default value hint
  - Work with default value(s)
  - Upload for BLOB type
- Edit/Update table
  - Default value hint
  - Work with default value(s)
  - Download for BLOB type (if not NULL)
  - Upload for BLOB type
- Column 
  - Add column (with type and default value)
  - Multiple column addition
- Rename table
- Drop table 
- Create table
  - Support type, primary key, default value
  - Single or multiple primary key
  - Support for integer primary key autoincrement
  - Default value can be non-constant
    (for example: current_time, current_timestamp)
- Query
  - Free form SQL Query
  - Automatically view query output (as integer or table)
- User account
  - Type: admin (full access), 
    standard (limited or configurable form access)
  - Change password
  - User management
- User-defined function
  - Prefix: sqliteboy_
  - Can be used in Query or Form
  - Please read USER-DEFINED FUNCTION below
  - Will be added regularly (or by your request)
- Easy to translate
- Configurable hosts allowed (default: local)
- Human readable database size (GB, MB, KB, B)
- Load time
- Custom Template
- Minimum use of Javascript in default/builtin template
  (only for delete selected confirmation and toggle select all)
- Form support (simple data entry) (v0.12)
  (should be available before 2013)
- Table name limitation: 
  could not handle table with whitespace in name 
  

REQUIREMENTS:
- python
- web.py
- SQLite module (included as sqlite3, in python 2.5+)
- JSON module (included as json, in python 2.6+)


DEFAULT ADMIN USER/PASSWORD: admin


RUN:
- python sqliteboy.py <database_file> [port]
  (then, using web browser, visit localhost:11738, 
   or localhost:PORT, if PORT is specified)


CUSTOM TEMPLATE
- sqliteboy.html, if found in current directory
- For template example: T_BASE variable


USER-DEFINED FUNCTION
- sqliteboy_md5(s)
- sqliteboy_sha1(s)
- sqliteboy_sha224(s)
- sqliteboy_sha256(s)
- sqliteboy_sha384(s)
- sqliteboy_sha512(s)
- sqliteboy_b64encode(s)
- sqliteboy_b64decode(s)
- sqliteboy_randrange(a, b)


FORM CODE REFERENCE
- Must be valid JSON syntax
- String (including keys below) must be double-quoted 
  (between " and ")
- No trailling comma in dict or list
- Python dict
- Keys:
  - title   : form title [str] [optional]
              example: "My Form"
  - info    : form information [str] [optional]
              example: "Form Information"
  - data    : form data [list of dict] <required>
    - table    : table name [str] <required>
                 example: "table1"
    - column   : column [str] <required>
                 example: "col1"
    - label    : label [str] [optional]
                 example: "column 1"
    - required : is required [int] [optional]
                 (0 = not required, 1 = required)
                 example: 1
    - readonly : is readonly [int] [optional]
                 (0 = not readonly, 1 = readonly)
                 example: 0
    - reference: predefined value(s) [optional]
                 can be str, list or int
                 - str: SQL query, 
                        returns 2 columns: a and b
                   rendered as HTML select
                   example: "select col1 as a, col2 as b from table1"
                 - list: static value(s),
                         contains list(s), which
                         contains two members
                   rendered as HTML select
                   example: [ ["0", "NO"], ["1", "YES"] ]
                 - int: ignored
                   example: 0
    - default  : default value [optional]
                 can be str, int, or list
                 - str or int: use as is
                 - list: SQL function call,
                         at least one member
                         first member must be str (function name)
                         return value will be used as default
                         format: [function_name, arg1, ...]
                         do not put () in function_name
                   example: ["sqliteboy_md5", "hello"]
                   example: ["sqlite_version"]
  - security: form security [dict] <required>
    - run      : can run form <required>
                 admin(s): always can run form
                 can be "" or list
                 - "": all users can run this form
                 - list: only users in this list can run this form
                   example: []
                   example: ["user1", "user2"]
  - onsave  : function call on save event [NOT IMPLEMENTED YET]

- Example:
{
  "title" : "My Form 1",
  "info"  : "Form Information", 
  "data"  : [
              {
                "table"    : "table3",
                "column"   : "a",
                "label"    : "column a",
                "required" : 1,
                "reference": [ ["0", "NO"], ["1", "YES"] ],
                "default"  : "1"
              },
              {
                "table"    : "table3",
                "column"   : "ee",
                "reference": "select rootpage as a, name as b from sqlite_master"
              },
              {
                "table"    : "table3",
                "column"   : "b",
                "default"  : ["sqliteboy_md5", "hello"]  
              }
            ],
  "security" : {
                 "run" : ""
               }
}


THANK YOU :)

