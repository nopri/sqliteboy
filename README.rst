sqliteboy.py
========================================================================
::

    Simple Web SQLite Manager/Form/Report Application
    (c) Noprianto <nop@tedut.com>
    2012 
    GPL


    Documentation for version 0.17


CONTENTS
========================================================================

1. SCREENSHOTS / TUTORIAL

2. WHY

3. FEATURES

4. REQUIREMENTS

5. DEFAULT ADMIN USER/PASSWORD

6. HOW TO RUN

7. CUSTOM TEMPLATE

8. USER-DEFINED FUNCTION

9. FORM CODE REFERENCE

10. REPORT CODE REFERENCE

11. DONATE

12. COMMERCIAL SUPPORT

13. THANK YOU :)


SCREENSHOTS / TUTORIAL
========================================================================

- https://github.com/nopri/sqliteboy/wiki (screenshot, possibly not 
  up-to-date)

- https://github.com/nopri/sqliteboy/wiki/Mengenal-sqliteboy (Mengenal 
  sqliteboy (intro to sqliteboy in Bahasa Indonesia)) 


WHY
========================================================================

- Easy to use, python and web.py based, Web SQLite Manager with 
  user-defined function and many extended features (Free/open source)

- If Extended feature is enabled: 

  Multi user, simple (yet flexible) form (data entry) and reporting can 
  be created by admin (simple JSON syntax), and can be run by 
  admin/user (configurable).
  
  Form field supports predefined values (options) from SQL Query or 
  Python list. Also, default value can be result of function call or 
  static value. Constraint is also supported, to do checking before 
  save, to prevent saving invalid value (and, it's possible to call 
  function before comparison)
  
  Reporting wizard also supports form field predefined values, default 
  value and constraint (checking before reporting query is executed). 
  Future version of reporting will support custom output format (PDF, 
  CSV, etc).

  User accounts, configurable hosts allowed, and many others are 
  available as extended features.
  
- I need simple form (data entry) and reporting solution. This 
  application is under active development. I use it at work and home. 
  

FEATURES
========================================================================

- Work with single SQLite database file

- Single python file

- Configurable port (default 11738 because it looks like sqliteboy)

- Basic/Extended Feature

  - Basic: Database management + User-defined function
  
  - Extended: Form, Report, User/Login, etc
  
    - Completely optional
  
    - Can be enabled in menu
  
    - If enabled, one table::
      
        _sqliteboy_ 
        
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
  
- Report Support (Extended feature, new in v0.16)

  - Simple reporting

  - Simple syntax (JSON)

  - Please read REPORT CODE REFERENCE section (below)

  - Readonly field

  - Predefined values (field options) from SQL Query 
    or Python list

  - Default value: function call or static value

  - Constraint: check before reporting, 
    (possible to call function before comparison)

  - Flexible SQL query
    (and relation to wizard/user input)
    (free form query, You can use join, etc)

  - Custom header order

  - Simple security setting

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

- User account (Extended feature)

  - Type: admin (full access), 
    standard (limited or configurable form/report access)

  - Change password

  - User management

- User-defined function

  - Prefix::
  
        sqliteboy_

  - Can be used in Query or Form or Report

  - Please read USER-DEFINED FUNCTION below

  - Will be added regularly (or by your request)

- Easy to translate

- Configurable hosts allowed (default: local) (Extended feature)

- Human readable database size (GB, MB, KB, B)

- Load time

- Custom Template

- Minimum use of Javascript in default/builtin template
  (only for delete selected confirmation and toggle select all)

- Table name limitation: 
  could not handle table with whitespace in name 
  

REQUIREMENTS
========================================================================

- python

- web.py

- SQLite module (included as sqlite3, in python 2.5+)

- JSON module (included as json, in python 2.6+)


DEFAULT ADMIN USER/PASSWORD
========================================================================
admin


HOW TO RUN
========================================================================
Command::

    python sqliteboy.py <database_file> [port]

then, using web browser, visit localhost:11738, or localhost:PORT, if 
PORT is specified


CUSTOM TEMPLATE
========================================================================

- sqliteboy.html, if found in current directory

- For template example: T_BASE variable


USER-DEFINED FUNCTION
========================================================================

- sqliteboy_strs(s)

- sqliteboy_as_integer(s)

- sqliteboy_as_float(s)

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

- sqliteboy_lower(s)

- sqliteboy_upper(s)

- sqliteboy_is_valid_email(s)
  ::
  
    return value  : 
        1 (valid) or 0 (invalid)

- sqliteboy_normalize_separator(s, separator, remove_space, unique)
  ::
  
      argument    : 
         separator (separator string)
         remove_space (remove space in s, 1 or 0)
         unique (1 or 0)
         
      example     : 
        sqliteboy_normalize_separator
          (',,,,,1,1,,  2,  3,  4,,,,', ',', 1, 1)    
        -> '1,2,3,4' 

- sqliteboy_x_user()
  ::
  
    return value  : 
        user name (if extended feature is enabled, or '')
    

FORM CODE REFERENCE
========================================================================

- Must be valid JSON syntax (json.org)

- String (including keys below) must be double-quoted 
  (between " and ")

- No trailling comma in dict or list

- Python dict

- Keys:

+---------------+-------------------------+---------------+-------------+--------------------------+
| Key           | Description             | Type          | Status      | Example                  |
+===============+=========================+===============+=============+==========================+
| title         | form title              | str           | optional    | "My Form"                |
+---------------+-------------------------+---------------+-------------+--------------------------+
| info          | form information        | str           | optional    | "Form Information"       |
+---------------+-------------------------+---------------+-------------+--------------------------+
| data          | form data               | list of dict  | required    |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| security      | form security           | dict          | required    |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| onsave        | function call on save   |               |             |                          |
|               | event [NOT IMPLEMENTED  |               |             |                          |
|               | YET]                    |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+

- Keys (data):

+---------------+-------------------------+---------------+-------------+--------------------------+
| Key           | Description             | Type          | Status      | Example                  |
+===============+=========================+===============+=============+==========================+
| table         | table name;             | str           | required    | "table1"                 |
|               | only single table is    |               |             |                          |
|               | supported, and first    |               |             |                          |
|               | table found will be     |               |             |                          |
|               | used, other table(s)    |               |             |                          |
|               | will be ignored         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| column        | column                  | str           | required    | "col1"                   |
+---------------+-------------------------+---------------+-------------+--------------------------+
| label         | label                   | str           | optional    | "column 1"               | 
+---------------+-------------------------+---------------+-------------+--------------------------+
| required      | is required;            | int           | optional    | 1                        |
|               | (0 = not required,      |               |             |                          |
|               | 1 = required)           |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| readonly      | is readonly;            | int           | optional    | 0                        |
|               | (0 = not readonly,      |               |             |                          |
|               | 1 = readonly)           |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| reference     | predefined value(s)     | str, list or  | optional    |                          |
|               |                         | int           |             |                          |
|               | - str: SQL query;       |               |             | - "select col1 as a,     |
|               |   returns 2 columns:    |               |             |   col2 as b from table1" |
|               |   a and b; HTML select  |               |             |                          |
|               |                         |               |             |                          |
|               | - list: static value(s);|               |             | - [ ["0", "NO"],         |
|               |   contains list(s),     |               |             |   ["1", "YES"] ]         |
|               |   which contains        |               |             |                          |
|               |   two members;          |               |             |                          |
|               |   HTML select           |               |             |                          |
|               |                         |               |             |                          |
|               | - int: ignored          |               |             |  - 0                     |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| default       | default value           | str, list or  | optional    |                          |
|               |                         | int           |             |                          |
|               | - str, int: use as is   |               |             |                          |
|               |                         |               |             |                          |
|               | - list: SQL function    |               |             | - ["sqliteboy_md5",      |
|               |   call; at least one    |               |             |   "hello"]               |
|               |   member; first member  |               |             |                          |
|               |   must be str (function |               |             | - ["sqlite_version"]     |
|               |   name); return value   |               |             |                          |
|               |   will be used as       |               |             |                          |
|               |   default;              |               |             |                          |
|               |                         |               |             |                          |
|               |   format:               |               |             |                          |
|               |   [function_name, arg1, |               |             |                          |
|               |   ...]                  |               |             |                          |
|               |                         |               |             |                          |
|               |   do not put () in      |               |             |                          |
|               |   function_name         |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| constraint    | check before save       | list          | optional    |                          |
|               |                         |               |             |                          |
|               | - must be list of four  |               |             | - ["", 0, "> 10",        |
|               |   members               |               |             |   "must be larger than   |
|               |                         |               |             |   10"];                  |
|               |   ["function_name",     |               |             |   check if column value  |
|               |   as_str,               |               |             |   is > 10                |
|               |   "condition",          |               |             |                          |
|               |   "error_message"]      |               |             | - ["sqliteboy_len", 1,   |
|               |                         |               |             |   "> 10", ""];           |
|               |   function_name         |               |             |   check if sqliteboy_len |
|               |   might be empty;       |               |             |   (column value) is > 10 |
|               |   as_str must be 1      |               |             |                          |
|               |   (treat function call  |               |             |                          |
|               |   argument as string)   |               |             |                          |
|               |   or 0;                 |               |             |                          |
|               |   condition must not    |               |             |                          |
|               |   empty;                |               |             |                          |
|               |   condition must        |               |             |                          |
|               |   contain boolean       |               |             |                          |
|               |   comparison;           |               |             |                          |
|               |   error_message might   |               |             |                          |
|               |   be empty;             |               |             |                          |
|               |                         |               |             |                          |
|               | - if function_name is   |               |             |                          |
|               |   not empty,            |               |             |                          |
|               |   function_name will be |               |             |                          |
|               |   called with column    |               |             |                          |
|               |   value as an argument; |               |             |                          |
|               |   function result will  |               |             |                          |
|               |   be compared with      |               |             |                          |
|               |   condition             |               |             |                          |
|               |                         |               |             |                          |
|               | - if function_name is   |               |             |                          |
|               |   empty,                |               |             |                          |
|               |   column value will     |               |             |                          |
|               |   be compared with      |               |             |                          |
|               |   condition             |               |             |                          |
|               |                         |               |             |                          |
|               | - if comparison result  |               |             |                          |
|               |   is 0 (false),         |               |             |                          |
|               |   form saving will be   |               |             |                          |
|               |   cancelled;            |               |             |                          |
|               |   if error_message is   |               |             |                          |
|               |   specified,            |               |             |                          |
|               |   error_message will be |               |             |                          |
|               |   displayed;            |               |             |                          |
|               |   else,                 |               |             |                          |
|               |   generic error message |               |             |                          |
|               |   with column name,     |               |             |                          |
|               |   function_name (if any)|               |             |                          |
|               |   and condition         |               |             |                          |
|               |   will be displayed     |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+

- Keys (security):

+---------------+-------------------------+---------------+-------------+--------------------------+
| Key           | Description             | Type          | Status      | Example                  |
+===============+=========================+===============+=============+==========================+
| run           | can run form;           | "" or list    | required    |                          |
|               | admin(s): always can run|               |             |                          |
|               | form                    |               |             |                          |
|               |                         |               |             |                          |
|               | - "": all users can     |               |             |                          |
|               |   run this form         |               |             |                          |
|               |                         |               |             |                          |
|               | - list: only users in   |               |             | - []                     |
|               |   this list can run     |               |             |                          |
|               |   this form             |               |             | - ["user1", "user2"]     |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+

- note:

  - if you are using primary key column in form data, 
    '*' character will be added to column label

  - tips: use sqliteboy_as_integer function in constraint
    to do integer conversion/comparison

- Example:
::

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
                    "label"     : "d (incorrect larger than 100)",
                    "required"  : 1,
                    "constraint": ["", 0, "> 100", "must be larger than 100"]
                  },
                  {
                    "table"     : "table1",
                    "column"    : "e",
                    "label"     : "e (correct larger than 100)",
                    "required"  : 1,
                    "constraint": ["sqliteboy_as_integer", 1, "> 100", "must be larger than 100"]
                  }
                ],

      "security" : {
                     "run" : ""
                   }
    }


REPORT CODE REFERENCE
========================================================================

- Must be valid JSON syntax (json.org)

- String (including keys below) must be double-quoted 
  (between " and ")

- No trailling comma in dict or list

- Python dict

- Keys:

  - title   : report title [str] [optional]
              example: "My Report"

  - info    : report information [str] [optional]
              example: "Report Information"

  - header  : header order [list] [optional]
              header order for query result
              if not specified, header order is unpredictable
                because each row of query result is python dict
                and default header order will be read from 
                first row
              example: ["column a of table1", "e"]

  - sql     : free form sql query [str] <required>
              please note that any placeholder must have 
              relation with key in data (below)
              example: 
                "select a.a as 'column a of table1', 
                  a.e from table1 a where a.a = $input_a_a and a.e > $a_e"
              for example above, you must define "input_a_a" 
                and "a_e" key in data (below)

  - data    : wizard/search data [list of dict] <required>

    - key      : HTML input name [str] <required>
                 underscore and alphanumeric only
                 example: "input_a_a"

    - label    : label [str] [optional]
                 example: "column a ="

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

    - type     : type [str] [optional]
                 cast input type as given type
                 currently, only "integer" is supported
                 (default: str)
                 if integer is specified, input will be converted
                   to integer using python's int()

    - constraint: check before reporting [list] [optional]
                  must be list of four members
                  ["function_name", as_str, "condition", "error_message"]
                  function_name might be empty
                  as_str must be 1 (treat function call argument as string) 
                    or 0
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
                    reporting will be cancelled
                    if error_message is specified,
                      error_message will be displayed
                    else,
                      generic error message with 
                      column name, function_name (if any) and 
                      condition will be displayed

  - security: reporting security [dict] <required>

    - run      : can run report <required>
                 admin(s): always can run report
                 can be "" or list

                 - "": all users can run this report

                 - list: only users in this list can run this report
                   example: []
                   example: ["user1", "user2"]

- note:

  - if you are using primary key column in form data, 
    '*' character will be added to column label

  - tips: use sqliteboy_as_integer function in constraint
    to do integer conversion/comparison

- Example:
::

    {
      "title" : "My Report",
      "info"  : "Report Information", 
      "header": ["column a of table1", "e"],
      "sql"   : "select a.a as 'column a of table1', a.e from table1 a where a.a = $input_a_a and a.e > $a_e",
      "data"  : [
                  {
                    "key"       : "input_a_a",
                    "label"     : "column a equals",
                    "reference" : [ ["0", "NO"], ["1", "YES"] ],
                    "default"   : "1"
                  },
                  {
                    "key"       : "a_e",
                    "label"     : "e (as integer) >",
                    "constraint": ["sqliteboy_as_integer", 1, "> 0", "e must be integer"]
                  }
                ],

      "security" : {
                     "run" : ""
                   }
    }


DONATE
========================================================================

- If you use this application, or find it useful, or want to support 
  the development, please consider to donate :)

- Any form of donation will be happily accepted


COMMERCIAL SUPPORT
========================================================================
If you need commercial support (customization, integration, training), 
please let me know :) Support is provided by tedut.com. 


THANK YOU :)
========================================================================


