sqliteboy
========================================================================
::

    Simple Web SQLite Manager/Form/Report Application
    (c) Noprianto <nop@tedut.com>
    2012-2013 
    GPL


Documentation for version 0.28


.. contents:: 


Screenshots And Wiki
========================================================================

- screenshot, possibly not up-to-date:  
  https://github.com/nopri/sqliteboy/wiki

- Mengenal sqliteboy (intro to sqliteboy in Bahasa Indonesia):  
  https://github.com/nopri/sqliteboy/wiki/Mengenal-sqliteboy 
  
- More: https://github.com/nopri/sqliteboy/wiki/_pages


Why
========================================================================

- Easy to use, python and web.py based, Web SQLite Manager with 
  user-defined function and many extended features (Free/open source)

- If Extended feature is enabled: 

  Multi user, simple (yet flexible) form (data entry) and reporting can 
  be created by admin (simple JSON syntax), and can be run by 
  admin/user (configurable). Very simple subform is also supported.
  
  Form field supports predefined values (options) from SQL Query or 
  Python list. Also, default value can be result of function call or 
  static value. Constraint is also supported, to do checking before 
  save, to prevent saving invalid value (and, it's possible to call 
  function before comparison). Onsave event is also supported, to 
  execute SQL Query (and use the result) just before the data is saved.
  
  Reporting wizard also supports form field predefined values, default 
  value and constraint (checking before reporting query is executed). 
  Future version of reporting will support custom output format (PDF, 
  CSV, etc).

  User accounts, configurable hosts allowed, and many others are 
  available as extended features.
  
- I need simple form (data entry) and reporting solution. This 
  application is under active development. I use it at work and home. 
  

Features
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

  - As of v0.21, onsave event is also supported, to execute SQL Query 
    (and use the result) just before the data is saved. The SQL Query 
    can be very complex and involves nested function calls.

  - As of v0.26, very simple subform is also supported. Subform can be 
    used in one to many relationship. However, fields in subform is 
    limited, compared to form. 
    
  - As of v0.27, custom result message (based on SQL query result), 
    is also supported. 
    
  - As of v0.27, optional, additional SQL query statement(s) can be 
    provided, and each of them will be executed in order, if you need 
    to perform additional task(s), after the form data is saved (for 
    example, write to another table). Previously, one might use report 
    if need to write to several tables. Last insert rowid value is 
    provided.
  
- Report Support (Extended feature, new in v0.16)

  - Simple reporting (and data entry)

  - Simple syntax (JSON)

  - Please read REPORT CODE REFERENCE section (below)

  - Readonly field

  - Predefined values (field options) from SQL Query 
    or Python list

  - Default value: function call or static value

  - Constraint: check before query, 
    (possible to call function before comparison)

  - Flexible SQL query
    (and relation to wizard/user input)
    (free form query, You can use join, etc)

  - Custom header order

  - Simple security setting
  
  - As of v0.18, report also can be used as form/data entry, using 
    insert SQL query. Custom result message (based on SQL query result), 
    is also supported. 

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
  

Requirements
========================================================================

- python

- web.py (http://webpy.org)

- SQLite module (included as sqlite3, in python 2.5+)

- JSON module (included as json, in python 2.6+)

(or see below if you prefer standalone application on Windows)


Standalone Windows Application
========================================================================
- Standalone / portable / run from USB Flash Disk 
- Can be run by standard user
- There is no need to install Python / requirements above
- Single file executable (+/- 4 MB)
- Download: http://tedut.com/sqliteboy.exe


Default Admin User And Password
========================================================================
admin


How To Run
========================================================================
Command::

    sqliteboy.exe <database_file> [port]
    
    (if you are using Standalone Windows Application)
    
    or

    python sqliteboy.py <database_file> [port]
    
    (if you are using source code)

then, using web browser, visit localhost:11738, or localhost:PORT, if 
PORT is specified


Custom Template
========================================================================

- sqliteboy.html, if found in current directory

- For template example: T_BASE variable


User-defined Function
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
    

Form Code Reference
========================================================================

- Must be valid JSON syntax (json.org)

- String (including keys below) must be double-quoted 
  (between " and ")

- No trailling comma in dict or list

- Python dict

- Only single table is supported. If you need to write to another 
  table after form data is saved, you can use additional SQL query 
  statement(s) (see below). 

- Onsave event can be used to execute SQL Query (and use the result) 
  just before the data is saved. The SQL Query can be very complex and 
  involves nested function calls.
  
- Very simple subform is also supported. Subform can be used in one to 
  many relationship. However, fields in subform is limited, compared to 
  form (only reference and default are supported; all is required; 
  none is readonly; column(s) can be selected). When saving data, 
  transaction is used. 

- Custom result message (based on SQL query result), is also supported.  
  
- Optional, additional SQL query statement(s) can be provided, and each 
  of them will be executed in order, if you need to perform additional 
  task(s), after the form data is saved (for example, write to another 
  table). Previously, one might use report if need to write to several 
  tables. Last insert rowid value is provided.

- Keys:

+---------------+-------------------------+---------------+-------------+--------------------------+
| Key           | Description             | Type          | Status      | Example                  |
+===============+=========================+===============+=============+==========================+
| data          | form data               | list of dict  | required    | see: Keys (data)         |
+---------------+-------------------------+---------------+-------------+--------------------------+
| security      | form security           | dict          | required    | see: Keys (security)     |
+---------------+-------------------------+---------------+-------------+--------------------------+
| title         | form title              | str           | optional    | "My Form"                |
+---------------+-------------------------+---------------+-------------+--------------------------+
| info          | form information        | str           | optional    | "Form Information"       |
+---------------+-------------------------+---------------+-------------+--------------------------+
| sub           | subform                 | list          | optional    |                          |              
|               |                         |               |             |                          |
|               | - must be list of five  |               |             | - ["table2", "a", [5,3], |
|               |   members: related      |               |             |   [["b", "Column B",     |
|               |   table (str); related  |               |             |   [ ["0", "NO"],         |
|               |   column in that table  |               |             |   ["1", "YES"] ], "1"],  |
|               |   (str); list of [rows  |               |             |   ["c", "Column C",      |
|               |   (int), required rows  |               |             |   "select a, b from      |
|               |   (int)]; list of       |               |             |   table1", ""]],         |
|               |   list (column) [column |               |             |   "My Subform"]          |
|               |   (str), label (str),   |               |             |                          |
|               |   reference, default];  |               |             |                          |
|               |   subform information   |               |             |                          |
|               |   (str)                 |               |             |                          |
|               |                         |               |             |                          |
|               | - see Keys (data) below |               |             |                          |
|               |   for reference/default |               |             |                          |
|               |                         |               |             |                          |
|               | - return value of       |               |             |                          |
|               |   last_insert_rowid()   |               |             |                          |
|               |   will be written to    |               |             |                          |
|               |   related column (each  |               |             |                          |
|               |   row). Use ROWID column|               |             |                          |
|               |   in master table to get|               |             |                          |
|               |   the relation.         |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| message       | custom result message   | list          | optional    |                          |
|               |                         |               |             |                          |
|               |                         |               |             | - [                      |
|               | - not applicable to     |               |             |    "unknown result",     |
|               |   subform               |               |             |    "zero result",        |
|               |                         |               |             |    "success: $result"    |
|               | - must be list of three |               |             |   ]                      |
|               |   members (str)         |               |             |                          |
|               |                         |               |             |                          |
|               |   ["message res < 0",   |               |             |                          |
|               |   "message res = 0",    |               |             |                          |
|               |   "message res > 0"]    |               |             |                          |
|               |                         |               |             |                          |
|               | - $result (in message)  |               |             |                          |
|               |   will be replaced by   |               |             |                          |
|               |   actual SQL Query      |               |             |                          |
|               |   result                |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| sql2          | additional sql query    | list          | optional    |                          |
|               | statement(s)            |               |             |                          |
|               |                         |               |             | - ["insert into table3(  |
|               | - must be list of str   |               |             |   a, b, c, d, e) values( |
|               |                         |               |             |   $a, $b, $c, $d, $e)",  |
|               | - $<column> will be     |               |             |   "insert into table4(x) |
|               |   replaced by user input|               |             |   values(                |
|               |   value for that column |               |             |   $last_insert_rowid)"]  |
|               |                         |               |             |                          |
|               | - $last_insert_rowid    |               |             |                          |
|               |   will be replaced by   |               |             |                          |
|               |   last_insert_rowid()   |               |             |                          |
|               |   function call result  |               |             |                          |
|               |   (after insert to main |               |             |                          |
|               |   table)                |               |             |                          |
|               |                         |               |             |                          |
|               | - quoting is            |               |             |                          |
|               |   automatically done    |               |             |                          |
|               |                         |               |             |                          |
|               | - each statement is     |               |             |                          |
|               |   executed in           |               |             |                          |
|               |   transaction (after    |               |             |                          |
|               |   form data is saved)   |               |             |                          |
|               |                         |               |             |                          |
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
|               | - int: ignored          |               |             | - 0                      |
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
+---------------+-------------------------+---------------+-------------+--------------------------+
| onsave        | execute sql query just  | str           | optional    |                          |
|               | before the data is saved|               |             |                          |
|               |                         |               |             | - "select $value ||      |
|               | - sql query can be very |               |             |   ' : ' ||               |
|               |   complex and involves  |               |             |   sqliteboy_upper(       |
|               |   nested function calls |               |             |   sqliteboy_md5($value)  |
|               |                         |               |             |   ) as onsave"           |
|               | - sql query must return |               |             |                          |
|               |   one column: onsave    |               |             | - In example above, md5  |
|               |                         |               |             |   hash of user input     |
|               | - quoting is            |               |             |   will be calculated     |
|               |   automatically done    |               |             |   using sqliteboy_md5.   |
|               |                         |               |             |   Then the result will   |
|               | - $value will replaced  |               |             |   be uppercased using    |
|               |   with user input value |               |             |   sqliteboy_upper. Then  |
|               |                         |               |             |   the result will be     |
|               | - the returned value    |               |             |   concatenated with      |
|               |   will be saved to      |               |             |   another string (final).|
|               |   table (not the        |               |             |                          |
|               |   user input value)     |               |             | - Example (input=hello): |
|               |                         |               |             |   hello : 5D41402ABC4B2A7|
|               |                         |               |             |   6B9719D911017C592      |
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
      "sub"   : [
                  "table2", 
                  "a", 
                  [5,3], 
                  [
                    ["b", "Column B", [ ["0", "NO"], ["1", "YES"] ], "1"],
                    ["c", "Column C", "select a, b from table1", ""]
                  ],
                  "My Subform" 
                ],  
      "sql2"  : [
                  "insert into table3(a, b, c, d, e) values($a, $b, $c, $d, $e)",
                  "insert into table4(x) values($last_insert_rowid)"
                ],                    
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
                    "constraint": ["sqliteboy_len", 1, "= 32", ""],
                    "onsave"    : "select sqliteboy_upper($value) as onsave"
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
      "message"  : ["unknown result", "zero result", "success: $result"],
      "security" : {
                     "run" : ""
                   }
    }


Report Code Reference
========================================================================

- Must be valid JSON syntax (json.org)

- String (including keys below) must be double-quoted 
  (between " and ")

- No trailling comma in dict or list

- Python dict

- All key (HTML input) in data is required. See Keys (data) below.

- Report also can be used as form/data entry, using insert SQL query. 
  Custom result message (based on SQL query result), is also supported.
  Using free form SQL query, data entry can work with multiple table.

- Keys:

+---------------+-------------------------+---------------+-------------+--------------------------+
| Key           | Description             | Type          | Status      | Example                  |
+===============+=========================+===============+=============+==========================+
| data          | wizard/search data      | list of dict  | required    | see: Keys (data)         |
+---------------+-------------------------+---------------+-------------+--------------------------+
| security      | reporting security      | dict          | required    | see: Keys (security)     |
+---------------+-------------------------+---------------+-------------+--------------------------+
| sql           | free form sql query;    | str           | required    | "select a.a as           |
|               | please note that any    |               |             | 'column a of table1',    |
|               | placeholder must have   |               |             | a.e from table1          |
|               | relation with key in    |               |             | a where a.a =            |
|               | data (see Keys (data))  |               |             | $input_a_a and           |
|               |                         |               |             | a.e > $a_e"              |
|               |                         |               |             |                          |
|               |                         |               |             | For that example,        |
|               |                         |               |             | you must define          |
|               |                         |               |             | "input_a_a"              |
|               |                         |               |             | and "a_e"                |
|               |                         |               |             | key in data              |
+---------------+-------------------------+---------------+-------------+--------------------------+
| title         | report title            | str           | optional    | "My Report"              |
+---------------+-------------------------+---------------+-------------+--------------------------+
| info          | report information      | str           | optional    | "Report Information"     |
+---------------+-------------------------+---------------+-------------+--------------------------+
| header        | header order;           | list          | optional    |                          |
|               | header order for query  |               |             |                          |
|               | result                  |               |             | - [                      |
|               |                         |               |             |    "column a of table1", |
|               | - if not specified,     |               |             |    "e"                   |
|               |   header order is       |               |             |   ]                      |
|               |   unpredictable,        |               |             |                          |
|               |   because each row of   |               |             |                          |
|               |   query result is       |               |             |                          |
|               |   python dict and       |               |             |                          |
|               |   default header order  |               |             |                          |
|               |   will be read from     |               |             |                          |
|               |   first row             |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| message       | custom result message;  | list          | optional    |                          |
|               | only for SQL query that |               |             |                          |
|               | returns integer (insert,|               |             | - [                      |
|               | update, etc). Useful for|               |             |    "unknown result",     |
|               | data entry function.    |               |             |    "zero result",        |
|               |                         |               |             |    "success: $result"    |
|               | - must be list of three |               |             |   ]                      |
|               |   members (str)         |               |             |                          |
|               |                         |               |             |                          |
|               |   ["message res < 0",   |               |             |                          |
|               |   "message res = 0",    |               |             |                          |
|               |   "message res > 0"]    |               |             |                          |
|               |                         |               |             |                          |
|               | - $result (in message)  |               |             |                          |
|               |   will be replaced by   |               |             |                          |
|               |   actual SQL Query      |               |             |                          |
|               |   result                |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+

- Keys (data):

+---------------+-------------------------+---------------+-------------+--------------------------+
| Key           | Description             | Type          | Status      | Example                  |
+===============+=========================+===============+=============+==========================+
| key           | HTML input name;        | str           | required    | "input_a_a"              |
|               | underscore and          |               |             |                          |
|               | alphanumeric only       |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| label         | label                   | str           | optional    | "column a ="             | 
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
|               | - int: ignored          |               |             | - 0                      |
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
| type          | type;                   | str           | optional    |                          |
|               | cast input type as      |               |             |                          |
|               | given type;             |               |             |                          |
|               | currently, only         |               |             |                          |
|               | "integer" is supported  |               |             |                          |
|               | (default: str)          |               |             |                          |
|               |                         |               |             |                          |
|               | - if integer is         |               |             |                          |
|               |   specified,            |               |             |                          |
|               |   input will be         |               |             |                          |
|               |   converted to          |               |             |                          |
|               |   integer using         |               |             |                          |
|               |   python's int()        |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| constraint    | check before reporting  | list          | optional    |                          |
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
|               |   reporting will be     |               |             |                          |
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
| run           | can run report;         | "" or list    | required    |                          |
|               | admin(s): always can run|               |             |                          |
|               | report                  |               |             |                          |
|               |                         |               |             |                          |
|               | - "": all users can     |               |             |                          |
|               |   run this report       |               |             |                          |
|               |                         |               |             |                          |
|               | - list: only users in   |               |             | - []                     |
|               |   this list can run     |               |             |                          |
|               |   this report           |               |             | - ["user1", "user2"]     |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+

- note:

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
      "message"  : ["unknown result", "zero result", "success: $result"],
      "security" : {
                     "run" : ""
                   }
    }


Donate
========================================================================

- If you use this application, or find it useful, or want to support 
  the development, please consider to donate :)

- Any form of donation will be happily accepted


Commercial Support
========================================================================
If you need commercial support (customization, integration, training), 
please let me know :) Support is provided by tedut.com. 


Thank You
========================================================================
Thank You very much :)

