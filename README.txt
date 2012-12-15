sqliteboy.py
Simple Web SQLite Manager/Form/Report Application
(c) Noprianto <nop@tedut.com>
2012 
GPL
version 0.14


SCREENSHOTS: https://github.com/nopri/sqliteboy/wiki
(possibly not up-to-date)


WHY:
- Easy to use, python and web.py based, Web SQLite Manager
  (Free/open source)
- If Extended feature is enabled: 
  Multi user, simple (yet flexible) form (data entry) and 
  reporting can be created by admin (simple JSON syntax), 
  and can be run by admin/user (configurable).
  
  Form field supports predefined values (options) from 
  SQL Query or Python list. Also, default value can be 
  result of function call or static value. Constraint
  is also supported, to do checking before save, to 
  prevent saving invalid value (and, it's possible to
  call function before comparison)
- I need simple form (data entry) and reporting solution. 
  This application is under active development. I use it
  at work and home. 
  

FEATURES:
- Work with single SQLite database file
- Single python file
- Configurable port 
  (default 11738 because it looks like sqliteboy)
- Basic/Extended Feature
  - Basic: Database management
  - Extended: Form, Report, User/Login, etc
    - Completely optional
    - Can be enabled in menu
    - If enabled, one table, _sqliteboy_, 
      will be created. You can delete this table 
      and extended feature will be disabled
- Form Support (Extended feature, new in v0.12)
  - Simple data entry
  - Simple syntax (JSON)
  - Please read FORM CODE REFERENCE section (below)
  - Readonly field
  - Required field
  - Predefined values (field options) from SQL Query 
    or Python list
  - Default value: function call or static value
  - Constraint: check before save, 
    prevent saving invalid value
    (possible to call function before comparison)
  - Simple security setting
  - onsave event (NOT IMPLEMENTED YET)
- Report Support (Extended feature, 
  will be implemented in v0.20)
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
- sqliteboy_len(s)
- sqliteboy_md5(s)
- sqliteboy_sha1(s)
- sqliteboy_sha224(s)
- sqliteboy_sha256(s)
- sqliteboy_sha384(s)
- sqliteboy_sha512(s)
- sqliteboy_b64encode(s)
- sqliteboy_b64decode(s)
- sqliteboy_randrange(a, b)
- sqliteboy_time()


FORM CODE REFERENCE
- Must be valid JSON syntax (json.org)
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
                 only single table is supported, and first table found
                 will be used, other table(s) will be ignored
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
    - constraint: check before save [list] [optional]
                  must be list of four members
                  ["function_name", as_str, "condition", "error_message"]
                  function_name might be empty
                  as_str must be 1 (treat input as string) or 0
                  condition must not empty
                  condition must contain boolean comparison
                  error_message might be empty
                  if function_name is not empty, 
                    function_name will be called
                    with column value as an argument
                    function result will be compared with condition
                  if function_name is empty,
                    column value will compared with condition
                  example: ["", 0, "> 10", "must be larger than 10"]
                    check if column value is > 10
                  example: ["sqliteboy_len", 1, "> 10", ""]
                    check if sqliteboy_len(column value) is > 10
                  if comparison result is 0 (false),
                    form saving will be cancelled
                    if error_message is specified,
                      error_message will be displayed
                    else,
                      generic error message with 
                      column name, function_name (if any) and 
                      condition will be displayed
  - security: form security [dict] <required>
    - run      : can run form <required>
                 admin(s): always can run form
                 can be "" or list
                 - "": all users can run this form
                 - list: only users in this list can run this form
                   example: []
                   example: ["user1", "user2"]
  - onsave  : function call on save event [NOT IMPLEMENTED YET]

- note:
  - if you are using primary key column in form data, 
    '*' character will be added to column label

- Example:
{
  "title" : "My Form 1",
  "info"  : "Form Information", 
  "data"  : [
              {
                "table"     : "table1",
                "column"    : "a",
                "label"     : "column a",
                "required"  : 1,
                "reference" : [ ["0", "NO"], ["1", "YES"] ],
                "default"   : "1"
              },
              {
                "table"     : "table1",
                "column"    : "b",
                "reference" : "select sqliteboy_randrange(1, 100000000000) as a, 'hello ' || sqliteboy_time() as b from _sqliteboy_"
              },
              {
                "table"     : "table1",
                "column"    : "c",
                "default"   : ["sqliteboy_md5", "hello"],  
                "constraint": ["sqliteboy_len", 1, "= 32", ""]
              },
              {
                "table"     : "table1",
                "column"    : "d",
                "label"     : "d (larger than 100)",
                "required"  : 1,
                "constraint": ["", 0, "> 100", "must be larger than 100"]
              }
            ],
  "security" : {
                 "run" : ""
               }
}


DONATE
- If you use this application, or find it useful, or want to support 
  the development, please consider to donate :)
- Any form of donation will be happily accepted


THANK YOU :)

