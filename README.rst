sqliteboy
========================================================================
::

    Simple Web SQLite Manager/Form/Report Application
    (c) Noprianto <nop@tedut.com>
    2012-2013 
    GPL


Documentation for version 0.65


.. contents:: 


Screenshots And Wiki And Presentation
========================================================================

- screenshot, possibly not up-to-date:  
  https://github.com/nopri/sqliteboy/wiki

- Mengenal sqliteboy (intro to sqliteboy in Bahasa Indonesia):  
  https://github.com/nopri/sqliteboy/wiki/Mengenal-sqliteboy 
  
- Tutorial: simple medical record
  https://github.com/nopri/sqliteboy/wiki/Tutorial-simple-medical-record

- Tutorial: install sqliteboy on ACRyan Playon!HD Mini2 ACRPV73800
  https://github.com/nopri/sqliteboy/wiki/Tutorial-install-sqliteboy-on-ACRyan-Playon!HD-Mini2-ACRPV73800

- SQLiteBoy Presentation (ppt format)
  http://tedut.com/sqliteboy.ppt
  
- More: https://github.com/nopri/sqliteboy/wiki/_pages


Why
========================================================================

- Easy to use, python and web.py based, Web SQLite Manager with 
  user-defined function and many extended features (Free/open source)
  
- User-defined functions: number to words (multi language), number format, 
  table lookup, hash, base64, random, additional date/time, additional 
  string, regular expression, utility

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

  User accounts, Notes, Files (with file sharing support), Page (home page),
  calculator, configurable hosts allowed, database backup, system configuration 
  and many others are available as extended features.
  
- I need simple form (data entry) and reporting solution (web-based) 

- If you are using Windows, standalone / portable application is 
  available (single file executable). Run from Windows Explorer 
  (double-click), no command line needed. Can be run from USB Flash 
  Disk. Can be run by standard user.
  

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
    
  - As of v0.60, headers and footers are supported. If not defined, a 
    default one will be created. Plain text, SQL Query, and Image are 
    supported.  

- Files (Extended feature, new in v0.47)

  - System configuration: maximum number of files per user (admin: unlimited)
  
  - System configuration: maximum file size (admin: unlimited)
  
  - Multiple file upload (content type, filename, etc are saved)
  
  - Action: view 
  
  - Action: download (disposition attachment)
  
  - Simple file sharing support 
  
  - Human readable file size
  
  - URL: /fs
  
  - HTTP 404 Error: file not found or not shared
  
- Page (Extended feature, new in v0.48)

  - Static page per user (home page)
  
  - URL: /page/<user>
  
  - Please read PAGE CODE REFERENCE section (below)

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

- CSV export 

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

- Notes (Extended feature, new in v0.41)

  - Simple notes 
  
  - Content as SQL Query (admin), calculator

- Calculator (Extended feature, new in v0.50)

  - Simple calculator 
  
  - Valid characters: 0123456789.-+*/()
  
  - Maximum length: 36
  
- User-defined function

  - Prefix::
  
        sqliteboy_

  - Can be used in Query or Form or Report

  - Please read USER-DEFINED FUNCTION below

  - Will be added regularly (or by your request)

- Easy to translate

- Configurable hosts allowed (default: local) (Extended feature)

- Database backup (admin) (Extended feature)

- System configuration (admin) (Extended feature, new in v0.43)

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
- Run from Windows Explorer (double-click), no command line needed
- To quit properly, press CTRL-C in terminal (cmd) window
- Documentation and source code are included
- Download: http://tedut.com/sqliteboy.exe


Default Admin User And Password
========================================================================
admin


How To Run
========================================================================
Command::

    run sqliteboy.exe (double-click) from Windows Explorer, and select
    database file (automatically create when opening a non-existent 
    file). 
    
    (if you are using Standalone Windows Application)
    
    or

    sqliteboy.exe <database_file> [port]
    
    (if you are using Standalone Windows Application and prefer command
    line or need to set port)
    
    or
    
    python sqliteboy.py <database_file> [port]
    
    (if you are using source code)
    
    or 
    
    python sqliteboy.py <database_file> [port] > LOGFILE 2>&1 &
    
    (if you are using source code, under Linux/Bash shell, and want to run
    in the background. You could use /dev/null as LOGFILE if you don't care
    about the logs.)

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

- sqliteboy_time2(s)
  ::
  
      get time from string (YYYY-MM-DD HH:MM:SS)
      argument    :
         s (date/time string)
         
      example     :
         sqliteboy_time2('2012-03-28 19:20:21')
         -> 1332937221.0

- sqliteboy_time3(f)
  ::
  
      get string (YYYY-MM-DD HH:MM:SS) from time (local time) 
      argument    :
         f (time)
         
      example     :
         sqliteboy_time3(1)
         -> 1970-01-01 07:00:01
         -> timezone is UTC+7 

- sqliteboy_time4(f)
  ::
  
      get string (YYYY-MM-DD HH:MM:SS) from time (UTC) 
      argument    :
         f (time)
         
      example     :
         sqliteboy_time4(1)
         -> 1970-01-01 00:00:01

- sqliteboy_time5(s1, s2, mode)
  ::
  
      calculate the difference between two dates in seconds, minutes, hours, days, or years
      (1 year = 365.2425 days)
      argument    :
         s1 (YYYY-MM-DD HH:MM:SS)
         s2 (YYYY-MM-DD HH:MM:SS)
         mode (1=seconds, 2=minutes, 3=hours, 4=days, 5=years)
         
      example     :
         sqliteboy_time5('2010-11-12 13:14:15', '2011-12-13 14:15:16', 1)
         -> 34218061.0 
         
         sqliteboy_time5('2010-11-12 13:14:15', '2011-12-13 14:15:16', 2)
         -> 570301.016667 
         
         sqliteboy_time5('2010-11-12 13:14:15', '2011-12-13 14:15:16', 3)
         -> 9505.01694444 
         
         sqliteboy_time5('2010-11-12 13:14:15', '2011-12-13 14:15:16', 4)
         -> 396.042372685 
         
         sqliteboy_time5('2010-11-12 13:14:15', '2011-12-13 14:15:16', 5)
         -> 1.08432718724 
      
      tips        :
         empty s1 or s2: current date/time (localtime)
         use sqliteboy_number_format() to format the result

- sqliteboy_is_leap(n)
  ::
  
      is leap year  
      argument    :
         n (year)
         
      return value: 
        1 (leap year) or 0 (not leap year)

- sqliteboy_lower(s)

- sqliteboy_upper(s)

- sqliteboy_swapcase(s)

- sqliteboy_capitalize(s, what)
  ::
  
      capitalize string  
      argument    :
         s (input string)
         what (0=first word, 1=all)
         
      example     : 
        sqliteboy_capitalize('hello world', 0)
        -> 'Hello world' 
        
        sqliteboy_capitalize('hello world', 1)
        -> 'Hello World' 

- sqliteboy_justify(s, justify, length, padding)
  ::
  
      left, right, center justify string  
      argument    :
         s (input string)
         justify (0=left, 1=right, 2=center)
         length (length)
         padding (single padding character)
         
      example     : 
        sqliteboy_justify('hello', 0, 10, 'x')
        -> 'helloxxxxx' 
        
        sqliteboy_justify('hello', 1, 10, 'x')
        -> 'xxxxxhello'
        
        sqliteboy_justify('hello', 2, 10, 'x')
        -> 'xxhelloxxx'
        
        sqliteboy_justify(12345, 1, 10, 0)
        -> '0000012345'
        
- sqliteboy_find(s, sub, position, case)
  ::
  
      find index in s where substring sub is found
      argument    :
         s (input string)
         sub (substring)
         position (0=lowest index, 1=highest index)
         case (0=ignore case, 1=case sensitive)

      return value: 
        -1 (not found) or > -1 (found, starts from 0)

      example     : 
        sqliteboy_find('hello sqliteboy', 'e', 0, 0)
        -> 1
        
        sqliteboy_find('hello sqliteboy', 'e', 1, 0)
        -> 11
        
        sqliteboy_find('hello sqlitEboy', 'e', 1, 0)
        -> 11
        
        sqliteboy_find('hello sqlitEboy', 'e', 1, 1)
        -> 1

- sqliteboy_reverse(s)
  ::
  
      reverse string
      argument    :
         s (input string)
         
      example     : 
        sqliteboy_reverse('hello world')
        -> 'dlrow olleh'
        
        sqliteboy_reverse(12345)
        -> '54321'

- sqliteboy_repeat(s, n)
  ::
  
      repeat s (n times)
      argument    :
         s (input string)
         n (n times)

      example     : 
        sqliteboy_repeat('sqliteboy ', 5)
        -> 'sqliteboy sqliteboy sqliteboy sqliteboy sqliteboy'
        
        sqliteboy_repeat(1, 20)
        -> '11111111111111111111'
        
        sqliteboy_repeat('=', 10)
        -> '=========='

- sqliteboy_count(s, sub, case)
  ::
  
      count substring sub in s
      argument    :
         s (input string)
         sub (substring)
         case (0=ignore case, 1=case sensitive)

      return value: 
        0 (not found) or > 0 (found)

      example     : 
        sqliteboy_count('hello sqliteboy', 'e', 0)
        -> 2 
        
        sqliteboy_count('hello hello hello', 'Hello', 0)
        -> 3 
        
        sqliteboy_count('hello hello hello', 'Hello', 1)
        -> 0

- sqliteboy_is_valid_email(s)
  ::
  
    return value  : 
        1 (valid) or 0 (invalid)

- sqliteboy_match(s1, s2)
  ::
  
      regular expression match  
      argument    :
         s1 (pattern string)
         s2 (test string)
         
      return value: 
        1 (match) or 0 (not match)

- sqliteboy_is_number(n)
  ::

      argument    : 
         n (number or string to test)
  
      return value: 
        1 (number) or 0 (not number)

- sqliteboy_is_float(n)
  ::
  
      return value: 
        1 (float) or 0 (not float)

- sqliteboy_is_integer(n)
  ::
  
      return value: 
        1 (integer) or 0 (not integer)

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

- sqliteboy_chunk(s, n, separator, justify, padding)
  ::
  
      split string into evenly sized chunks
      argument    : 
         s (string)
         n (length/size)
         separator (separator string)
         justify (0=left, 1=right)
         padding (single padding character)
         
      example     : 
        select sqliteboy_chunk('123456789', 3, '-', 1, 'x')
        -> '123-456-789' 
        
        select sqliteboy_chunk('123456789', 2, '-', 0, 'x')
        -> '12-34-56-78-9x'
        
        select sqliteboy_chunk('123456789', 2, '-', 1, 'x')
        -> 'x1-23-45-67-89'
        
        select sqliteboy_chunk('123456789', 4, ',', 1, '*')
        -> '***1,2345,6789'

- sqliteboy_number_format(n, decimals, decimal_point, thousands_separator)
  ::
  
      format a number (or number as string) with grouped thousands and decimals
      (works with number in scientific notation (e))
      argument    : 
         n (number or number as string), use string for very big number
         decimals (number of decimal points)
         decimal_point (separator for the decimal point)
         thousands_separator (thousands separator)
         
      example     : 
        sqliteboy_number_format(12345, 3, '.', ',')
        -> '12,345'
      
        sqliteboy_number_format(12345, 3, ',', '.')
        -> '12.345' 
        
        sqliteboy_number_format(12345.1234, 3, ',', '.')
        -> '12.345,123'
        
        sqliteboy_number_format(12345.1234, 0, ',', '.')
        -> '12.345'
        
        sqliteboy_number_format(12345.1234, 10, ',', '.')
        -> '12.345,1234000000'
        
        sqliteboy_number_format(12345.1234, 2, ',', ' ')
        -> '12 345,12'
        
        sqliteboy_number_format('-12345678912345678912345678912345678912.123', 10, ',', '.')
        -> '-12.345.678.912.345.678.912.345.678.912.345.678.912,1230000000'

- sqliteboy_number_to_words(s, language)
  ::
  
      number to words
      Please read NUMBER TO WORDS REFERENCE section (below)
      
      argument    : 
         s (number as string)
         language (language code)
         
      return value: 
        number to words or '' (error/unsupported)
         
      example     : 
        language  : 'id'
        
        sqliteboy_number_to_words('-0', 'id')
        -> 'nol'
        
        sqliteboy_number_to_words('11', 'id')
        -> 'sebelas'
        
        sqliteboy_number_to_words('1000', 'id')
        -> 'seribu'
        
        sqliteboy_number_to_words('1000000', 'id')
        -> 'satu juta'
        
        sqliteboy_number_to_words('-123456789123456789123456789.123456789', 'id')
        -> 'min seratus dua puluh tiga triliun empat ratus lima puluh enam milyar tujuh ratus delapan puluh sembilan juta seratus dua puluh tiga ribu empat ratus lima puluh enam triliun tujuh ratus delapan puluh sembilan milyar seratus dua puluh tiga juta empat ratus lima puluh enam ribu tujuh ratus delapan puluh sembilan koma satu dua tiga empat lima enam tujuh delapan sembilan'

        language  : 'en1'
        
        sqliteboy_number_to_words('-0', 'en1')
        -> 'zero'
        
        sqliteboy_number_to_words('11', 'en1')
        -> 'eleven'
        
        sqliteboy_number_to_words('1000', 'en1')
        -> 'one thousand'
        
        sqliteboy_number_to_words('1000000', 'en1')
        -> 'one million'
        
        sqliteboy_number_to_words('-123456789123456789123456789.123456789', 'en1')
        -> 'minus one hundred twenty-three trillion four hundred fifty-six billion seven hundred eighty-nine million one hundred twenty-three thousand four hundred fifty-six trillion seven hundred eighty-nine billion one hundred twenty-three million four hundred fifty-six thousand seven hundred eighty-nine point one two three four five six seven eight nine'        

- sqliteboy_lookup2(table, field, field1, value1, order, default)
  ::
  
      lookup into table
      SELECT <field> FROM <table> WHERE <field1>=<value1> ORDER BY rowid asc
      or
      SELECT <field> FROM <table> WHERE <field1>=<value1> ORDER BY rowid desc
      and
      return first row
      argument    : 
         table (table name)
         field (field name)
         field1 (where field)
         value1 (where field value)
         order (0=asc, 1=desc)
         default (default return value)
         
      example     : 
        data in 'lookup' table:
        | a | b | c |
        -------------
        |a1 |b1 |c1 |
        |a2 |b2 |c2 |
        
        sqliteboy_lookup2('lookup', 'c', 'a', 'a1', 0, ':(')
        -> 'c1' 
        
        sqliteboy_lookup2('lookup', 'c_notfound', 'a', 'a1', 0, ':(')
        -> ':('
        
        sqliteboy_lookup2('lookup', 'b', 'a', 'a1', 0, ':(')
        -> 'b1'
        
        sqliteboy_lookup2(12345, 'b', 'a', 'a1', 0, ':(')
        -> ':('

- sqliteboy_lookup3(table, field, field1, value1, field2, value2, order, default)
  ::
  
      lookup into table
      SELECT <field> FROM <table> WHERE <field1>=<value1> and <field2>=<value2> ORDER BY rowid asc
      or
      SELECT <field> FROM <table> WHERE <field1>=<value1> and <field2>=<value2> ORDER BY rowid desc
      and
      return first row
      argument    : 
         table (table name)
         field (field name)
         field1 (where field1)
         value1 (where field1 value)
         field2 (where field2)
         value2 (where field2 value)
         order (0=asc, 1=desc)
         default (default return value)
         
      example     : 
        data in 'lookup' table:
        | a | b | c |
        -------------
        |a1 |b1 |c1 |
        |a2 |b2 |c2 |
        
        sqliteboy_lookup3('lookup', 'c', 'a', 'a1', 'b', 'b1', 0, ':(')
        -> 'c1' 
        
        sqliteboy_lookup3('lookup', 'c', 'a', 'a1', 'b', 'b2', 0, ':(')
        -> ':('
                
        sqliteboy_lookup3(12345, 'c', 'a', 'a1', 'b', 'b1', 0, ':(')
        -> ':('
        
- sqliteboy_http_remote_addr()
  ::
  
    return value  : 
        http remote address 

- sqliteboy_http_user_agent()
  ::
  
    return value  : 
        http user agent (for example: web browser)

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

- Example 1:
::

    {
      "title" : "My Form (Simple)",
      "info"  : "Form Information", 
      "data"  : [
                  {
                    "table"     : "table1",
                    "column"    : "a"
                  },
                  {
                    "table"     : "table1",
                    "column"    : "d"
                  },
                  {
                    "table"     : "table1",
                    "column"    : "f"
                  }
                ],
      "security" : {
                     "run" : ""
                   }
    }

- Example 2:
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
                  },
                  {
                    "table"     : "table1",
                    "column"    : "f"
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
  
- Headers and footers are supported. If not defined, a default one will be 
  created. Plain text, SQL Query, and Image are supported. Headers and
  footers are rendered as tables (multiple rows/columns; one table for 
  headers, one table for footers). If there is difference in number of 
  columns for each row, largest one will be used. 

- Default headers: 

  - First row: first column (report title), second column (report info)
  
  - Next row(s): first column (search key), second column (user input)

- Default footers (SELECT SQL): 

  - First row: first column (number of rows), second column ("row(s)"/translated)

- Default footers (NON-SELECT SQL): 

  - First row: first column (message or ""), second column ("")
  
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
| headers       | custom headers          | list of list  | optional    |                          |
|               |                         | of list       |             |                          |
|               | - must be list of list  |               |             | (please see Example 2    |
|               |   (rows) of list        |               |             | below)                   |
|               |   (columns) of three    |               |             |                          |
|               |   members (each cell)   |               |             |                          |
|               |   (str, str/int, dict)  |               |             |                          |
|               |                         |               |             |                          |
|               | - cell: [type, value,   |               |             |                          |
|               |   attr]                 |               |             |                          |
|               |                         |               |             |                          |
|               | - type: "" (plain text),|               |             |                          |
|               |   "sql" (sql query),    |               |             |                          |
|               |   "files.image" (file   |               |             |                          |
|               |   number in user files) |               |             |                          |
|               |                         |               |             |                          |
|               | - value: any valid value|               |             |                          |
|               |   for type (str is valid|               |             |                          |
|               |   for types above)      |               |             |                          |
|               |                         |               |             |                          |
|               | - attr: {}              |               |             |                          |
|               |                         |               |             |                          |
|               | - for "sql" type,       |               |             |                          |
|               |   $result_row_count will|               |             |                          |
|               |   be replaced by actual |               |             |                          |
|               |   row count (or -1),    |               |             |                          |
|               |   $result_message will  |               |             |                          |
|               |   be replaced by actual |               |             |                          |
|               |   message (or "", for   |               |             |                          |
|               |   custom result         |               |             |                          |
|               |   message), and each key|               |             |                          |
|               |   in data will be       |               |             |                          |
|               |   replaced by user input|               |             |                          |
|               |   value; quoting is     |               |             |                          |
|               |   automatically done;   |               |             |                          |
|               |   sql query must return |               |             |                          |
|               |   one column: a         |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| footers       | custom footers          | list of list  | optional    |                          |
|               |                         | of list       |             |                          |
|               | (please see headers)    |               |             |                          |
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

- Example 1:
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

- Example 2:
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
      "headers"  : [
                      [
                          ["files.image", "31", {}],
                          ["", "My Report", {}]
                      ],
                      [
                          ["", "Date/Time", {}],
                          ["sql", "select sqliteboy_time3(sqliteboy_time()) as a", {}]
                      ],
                      [
                          ["", "User", {}],
                          ["sql", "select sqliteboy_x_user() as a", {}]
                      ],
                      [
                          ["", "column a equals", {}],
                          ["sql", "select $input_a_a as a", {}]
                      ],
                      [
                          ["", "e (as integer) >", {}],
                          ["sql", "select $a_e as a", {}]
                      ],
                      [
                          ["", "Rows", {}],
                          ["sql", "select $result_row_count as a", {}]
                      ]
                   ],                
      "security" : {
                     "run" : ""
                   }
    }


Page Code Reference
========================================================================

- emphasis 
  ::

      ~text~ -> <em>text</em>

- strong
  ::

      *text* -> <strong>text</strong>

- underline
  ::

      _text_ -> <u>text</u>

- link
  ::

      [text|url] -> <a href="url">text</a>

- Note: HTML tags will be stripped on page save

- Note: rendered in <pre></pre> tag


Number To Words Reference
========================================================================
- Supported languages:
  
  - id            : Bahasa Indonesia
  - en1           : English (trillion billion million thousand scheme)
  
- More languages will be added 

- Please let me know/correct me if there is something wrong in the 
  implementation 

- Currently, highest supported large number name is trillion (short scale) 
  or 10**12 or 1,000,000,000,000. And, number supported is ranged
  from: -999,999,999,999,999,999,999,999,999.99... 
  (minus 999.999 999 999 999 999 999 999 999 trillion trillion plus digits after decimal point)
  to:    999,999,999,999,999,999,999,999,999.99... 
  (      999.999 999 999 999 999 999 999 999 trillion trillion plus digits after decimal point)
  
  (This is, however, might be different for each language)
    
- Digits after the decimal point is limited only by python float 
  (that is, very very long long number), so this is valid and supported number:
  999999999999999999999999999.999999999999999999999999999999999999999999999999999999
   

Donate
========================================================================

- If you use this application, or find it useful, or want to support 
  the development, please consider to donate :)

- Any form of donation will be happily accepted


Commercial Support
========================================================================
If you need commercial support (training, integration), 
please let me know :) Support is provided by tedut.com. 


Thank You
========================================================================
Thank You very much :)

