
::

    SQLiteBoy
    Simple web-based management tool for SQLite database
    (with form, report, website, and many other features)
    (c) Noprianto <nopri.anto@icloud.com>
    2012-2019
    License: GPL
    Version: 1.83

    SQLiteBoy is an independent product, developed separately from the
    SQLite core library, which is maintained by SQLite.org.
    Neither noprianto.com nor SQLite.org take any responsibility for the
    work of the other.




.. contents::



What Is SQLiteBoy
========================================================================

- Easy to use, python and web.py based, simple web-based management tool 
  for SQLite database with user-defined functions and many extended features 
  (Free/open source)

- User-defined functions: number to words (multi language), number format,
  table lookup, hash, base64, random, additional date/time, additional
  string, regular expression, utility

- If Extended feature is enabled:

  Multi user, simple (yet flexible) form (data entry) and reporting can
  be created by admin (simple JSON syntax), and can be run by
  admin/user (configurable). Very simple subform is also supported.

  Form field supports predefined values (options) from SQL Query or
  Python list. Also, default value can be result of function call,
  static value or SQL Query. Constraint is also supported, to check before
  save, to prevent saving invalid value (it's possible to call
  function before comparison). Onsave event is also supported, to
  execute SQL Query (and use the result) just before the data is saved.

  Reporting wizard also supports form field predefined values, default
  value and constraint (checking before reporting query is executed).
  Supported report format: PDF, HTML, HTML (printer friendly) and CSV.

  Form and Report support python handler, which will be automatically called, if
  provided. Python handler eases the integration with external system
  (for example: ERP system). Python handler also could be useful in,
  for example, complex database operation, reading from/writing to
  external devices, etc.

  User accounts, Notes, Files (with file sharing support), Page (home page),
  calculator, configurable hosts allowed, database backup, system configuration,
  Scripts, profile (with user-defined profile support)
  and others are available as extended features

  SQLiteBoy script (simple JSON syntax, single file) can be used to automate
  the creation of tables (including addition of columns, for existing table),
  forms, reports or user-defined profiles
  
  It is also possible to use SQLiteBoy to serve a website with custom URLs.
  URL can be handled by a python function, redirect, Files, template, or HTML.
  POST method is also supported and can be handled by python function.


Links
========================================================================

- screenshot, probably not up-to-date:
  https://github.com/nopri/sqliteboy/wiki

- Free Book: Form dan Report sederhana dengan SQLiteBoy
  (Bahasa Indonesia, available as PDF/ODT, 250+ pages, revision 2):
  https://github.com/nopri/publication/raw/master/form-dan-report-sederhana-dengan-sqliteboy.pdf

- Tutorial: simple medical record:
  https://github.com/nopri/sqliteboy/wiki/Tutorial-simple-medical-record

- Tutorial: install sqliteboy on ACRyan Playon!HD Mini2 ACRPV73800:
  https://github.com/nopri/sqliteboy/wiki/Tutorial-install-sqliteboy-on-ACRyan-Playon!HD-Mini2-ACRPV73800

- Tutorial: Using sqliteboy udf in python handler:
  https://github.com/nopri/sqliteboy/wiki/Tutorial-using-sqliteboy-udf-in-python-handler

- Tutorial: Create a new partner in OpenERP:
  https://github.com/nopri/sqliteboy/wiki/Tutorial-create-a-new-partner-in-openerp

- Tutorial: Search partners in OpenERP:
  https://github.com/nopri/sqliteboy/wiki/Tutorial-search-partners-in-openerp

- Tutorial: Hyperlink and Javascript in label:
  https://github.com/nopri/sqliteboy/wiki/Tutorial-hyperlink-and-javascript-in-label

- More: https://github.com/nopri/sqliteboy/wiki/_pages


Development Notes
========================================================================

- Standalone version is no longer provided, but codes for this
  are still in the source code

- Version 1.51 was released as a bug fix (reported in issue #1). In this
  commit, many lines (both in this file and the source code) had been
  added/deleted (due to text reformatting). Please, let me know if
  something was accidentally added or deleted.

- As of v1.64, index URL was changed to /index because / is used for 
  public home page (new in v1.64, please read WEBSITE AND CUSTOM URL REFERENCE)  


Features
========================================================================

- Works with single SQLite database per instance

- Single python file

- Configurable port (default 11738 because it looks like sqliteboy).
  As of v1.75, it is possible to run SQLiteBoy as WSGI application,
  please read HOW TO RUN. 

- SSL Support

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

  - Default value: function call or static value or SQL Query

  - Constraint: check before save,
    prevent saving invalid value
    (possible to call function before comparison)

  - Simple security setting

  - As of v0.21, onsave event is also supported, to execute SQL Query
    (and use the result) just before the data is saved. The SQL Query
    can be very complex and involves nested function calls.

  - As of v0.26, very simple subform is also supported. Subform can be
    used in one to many relationship. However, field in subform is
    limited, compared to form.

  - As of v0.27, custom result message (based on SQL query result),
    is also supported.

  - As of v0.27, optional, additional SQL query statement(s) can be
    provided, and each of them will be executed in order, if you need
    to perform additional task(s), after the form data is saved (for
    example, write to another table). Previously, one might use report
    if need to write to several tables. Last insert rowid value is
    provided.

  - As of v0.75, insert into table can be disabled by setting insert key
    to zero/negative value. This is useful if you need to update/delete data in
    table(s), using additional SQL query statement(s). By default,
    form/subform save will insert new row(s) into table(s).

  - As of v0.98, form supports python handler, which will be automatically
    called, if provided. Python handler eases the integration with external
    system (for example: ERP system). Please read PYTHON HANDLER REFERENCE
    section.

  - As of v1.33, optional, (run before) additional SQL query statement(s)
    can be provided.

  - As of v1.72, links can be added to form

  - As of v1.73, form supports extended result message. This extends 
    custom result message introduced in v0.27. Using extended result, 
    it is possible to perform operations on form fields, and use the result.
    Like custom result message, it is based on SQL query result.
    But unlike custom result message, the result is not limited to integer
    (can be string or another types; probably returned from function call). 

- Report Support (Extended feature, new in v0.16)

  - Simple reporting (and data entry)

  - Simple syntax (JSON)

  - Please read REPORT CODE REFERENCE section (below)

  - Readonly field

  - Predefined values (field options) from SQL Query
    or Python list

  - Default value: function call or static value or SQL Query

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

  - As of v0.85, printer friendly version of report result is supported
    in default output format (HTML)

  - As of v1.00, report supports python handler, which will be automatically
    called, if provided. Python handler eases the integration with external
    system (for example: ERP system). Please read PYTHON HANDLER REFERENCE
    section.

  - As of v1.17, CSV output is supported

  - As of v1.28, PDF output (paper size, margins, image) is supported

  - As of v1.36, text align is supported (HTML and PDF only)

  - As of v1.72, links can be added to report
  
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

- Scripts (Extended feature, new in v0.71)

  - Simple script, to automate the creation of tables
    (including addition of columns, for existing table),
    forms, reports or user-defined profiles

  - Solution can be deployed in form of script, that can be uploaded
    and run by admin

  - Simple syntax (JSON) in single file

  - Please read SCRIPT CODE REFERENCE section (below)

- Profile (Extended feature, new in v0.91)

  - User profile

    - style

  - User-defined profile is also supported. Using this feature,
    custom field(s) in user profile can be added. This is useful,
    for example, in multi-company environment.

    - system configuration

    - Simple syntax (JSON)

    - Predefined values (field options) from SQL Query or Python list
      (as in form or report, is also supported)

    - Please read USER-DEFINED PROFILE REFERENCE section (below)

- Website (Extended feature, new in v1.64)

  - Custom URLs
  
  - URL can be handled by a python function, redirect, Files, template, or HTML
  
  - As of v1.67, POST method handler is supported, using python function

  - As of v1.68, custom not found URL is supported
  
  - Please read WEBSITE AND CUSTOM URL REFERENCE

- Browse table

  - Sort (asc/desc)

  - Download for BLOB type (if not NULL)

  - Multiple selection

  - Delete selected

  - Edit selected

  - Maintain last selected row(s)

  - Limit rows

  - Pagination

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

- Empty table

- Drop table

- CSV export/import

- Schema (view schema, create new table)

- Copy table

- Create table

  - Support type, primary key, default value

  - Single or multiple primary key

  - Support for integer primary key autoincrement

  - Default value can be non-constant
    (for example: current_time, current_timestamp)

- Query

  - Free form SQL Query

  - Automatically view query output (as integer or table)

  - Export query result to CSV (if applicable)

  - User-defined variable is also supported (max per user: 3).
    Please use the following functions: sqliteboy_var_set,
    sqliteboy_var_get, sqliteboy_var_del.

- Vacuum

- User account (Extended feature)

  - Type: admin (full access),
    standard (limited or configurable form/report access)

  - Change password

  - User management

- Notes (Extended feature, new in v0.41)

  - Simple notes

  - Content as SQL Query (admin), calculator, source code

  - Please read Interpreter below

- Calculator (Extended feature, new in v0.50)

  - Simple calculator

  - Valid characters: 0123456789.-+*/()

  - Maximum length: 36

- Interpreter (Extended feature, new in v1.81)

  - Please read MONKEY PROGRAMMING LANGUAGE

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

- Shortcut (form, report) (Extended feature, new in v0.84)

- Logs (Extended feature, new in v1.61)

- Human readable database size (GB, MB, KB, B)

- Load time

- Custom Template

- Minimum use of Javascript in default/builtin template
  (only for confirmation dialog and toggle select all)

- Table name limitation:
  cannot handle table with whitespace in name


Requirements
========================================================================

- python

- web.py (http://webpy.org)

- SQLite module (included as sqlite3, in python 2.5+)

- JSON module (included as json, in python 2.6+)

- Optional: ReportLab (PDF output)

- Optional: pyOpenSSL (SSL support)


Standalone Version
========================================================================
Note: Standalone version is no longer provided


Login
========================================================================

- Default admin user and password: admin

- As of v1.63, additional/custom links at login page are supported. Links
  may be placed at multiple page sections (please read LINK CODE REFERENCE
  and TITLE REFERENCE).
  
- As of v1.66, it is possible to define redirect URL after logged in, 
  using to=<URL> parameter. However, only valid URL is allowed, according
  to WEBSITE AND CUSTOM URL REFERENCE.

- As of v1.69, logout uses redirect URL set in login 


SSL Support
========================================================================
To enable SSL support, please put the following files into current
working directory:

- sqliteboy.cert (SSL certificate)
- sqliteboy.key  (SSL private key)

If you need to create a self-signed test certificate,
OpenSSL can be used::

    openssl req -new -x509 -newkey rsa:1024 -keyout sqliteboy.key -out sqliteboy.cert -days 365 -nodes


How To Run
========================================================================
Command::

    python sqliteboy.py <database_file> [port]

    (if you are using source code)

    or

    python sqliteboy.py <database_file> [port] > LOGFILE 2>&1 &

    (if you are using source code, sh compatible shell (with job control),
    and want to run in the background. If applicable, You could use
    /dev/null as LOGFILE if you don't care about the logs.)

then, using web browser, visit localhost:11738, or localhost:PORT, if
PORT is specified

Please use https if SSL support is enabled

(Please also read SERVER COMMAND REFERENCE)

As of v1.62, it is possible to run multiple SQLiteBoy instances 
(single host, different ports / databases), as the HTTP cookie name is 
set based on database path.

As of v1.75, it is possible to run as WSGI application:

- Please make sure that an SQLite database named data.db exists in
  current working directory (or, it can be an empty file)
- If 'application' is expected::

    from sqliteboy import wsgi_application as application

As of v1.76, disk-based session is supported. If a readable/writable directory
named sqliteboy-session is found in current working directory, disk-based
session will be used. Otherwise, default memory-based session will be used.


Custom Template
========================================================================

- sqliteboy.html, if found in current working directory

- For template example: T_BASE variable

- Please do not put '$def with (data, content)' line in template


Website and Custom URL Reference
========================================================================

- To manage a website, please visit /admin/website (as admin), or visit
  info -> website
  
- Custom URLs, as long as the URLs are not used by SQLiteBoy (reserved).
  List of reserved URLs is shown in website management screen.
  
- URL can be handled by a python function, redirect, Files, template, or HTML

- Each URL is specified by:

  - id: must be alphabetic only (maximum length: 36), converted to 
    lowercase on save. This id is used in python handler.
    
  - url: must be alphanumeric/underscore/dot/slash/dash (maximum length: 128),
    converted to lowercase on save. This is the URL. Please read the 
    additional rules below.
    
  - content: content, interpreted. 
  
- Additional URL rules:

  - Please use / for home page. Without this URL, / will be redirected
    to /index (and then /login if the user is not logged in) 
  
  - Please start url with / (but do not end it with /)

- Only valid values are saved (id and url are checked on save)

- Content interpretation:

  - If there is a python function named web_<id> (in sqliteboy_user.py,
    please also read PYTHON HANDLER REFERENCE):
  
    - It will be called and the return value is used as dynamic contents 
      (with custom HTTP headers)
      
    - If there is an exception, redirection to /index will be performed.
      Please make sure that the python function is valid.
    
  - If python handler for that URL is NOT available:
  
    - If the content looks like a number:
    
      - If the number is a valid file id:
      
        - Contents of the file will be returned (along with saved headers) 

        - To set Content-Disposition as attachment, please set download parameter
          (for example: ?download=download or ?download=true)
        
        - Default Content-Disposition is inline

        - Valid file id:

          - Exists in Files 

          - If user is logged in:

            - File sharing status is checked. If a file is not shared
              (and logged in user is not the owner), it is considered 
              invalid. This applies for all users, including admin users.

      - If the number is NOT a valid file id:
      
        - Content will be returned 
    
    - If it is NOT a number:
    
      - If the content starts with http:// or https://, redirection is
        performed
      
      - Otherwise, the content is interpreted as HTML with template

- HTML template interpretation:

  - If there is an exception (or content is HTML), content will be returned as is
  
  - If this meant to be a template, please start the content with
    :: 
    
        $def with (id, url, content, param)

  - The following globals are available to template:

    - Note: most user-defined functions are also available. 
      Please read USER-DEFINED FUNCTION.
      Unavailable functions are marked with: 
      not available in HTML template interpretation.

    - size: a function, requires no argument, returns database size as string
    
    - user: a function, requires no argument, returns logged in user name 
      as string (or an empty string)
      
    - table_browse: a function, to browse a table 
      (excluding _sqliteboy_, sqlite_sequence, sqlite_master)
      ::
      
        table_browse(table, what='*', where=None, order=None, group=None, limit=None, offset=None) 

    - begin: a function, to begin an HTML document
      ::

        begin(title='', style='', lang='en', charset='utf-8')

    - end: a function, to end an HTML document

    - redirect: a function, to redirect to a URL
      ::

        redirect(url, title='', after=0, lang='en')
        
    - redirect_check: a function, to redirect to a URL, 
      if a condition is false. Otherwise, begin an HTML document.
      ::

        redirect_check(check, url, title_redirect='', after=0, 
        lang='en', title='', style='', charset='utf-8')

    - redirect_user: a function, to redirect to a URL, 
      if user is not logged in. Otherwise, begin an HTML document.
      ::

        redirect_user(url, title_redirect='', after=0, 
        lang='en', title='', style='', charset='utf-8')

  - Please read web.py template for more information

  - Example (begin, end):
    ::

        $def with (id, url, content, param)
        $ a = begin(title='Hello')
        $ b = end()
        $:a
        Hello
        $:b

  - Example (custom URL:/test, /test?hello=world):
    ::

        $def with (id, url, content, param)
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
        $ u = user()
        $if u:
          Hello, $u
          <br>
        $ data = table_browse('A', order='name')
        $if data:
          $for d in data:
            $d['name']
        <br>
        URL: $url
        <br>
        Hello: $param.get('hello', '')
        </body>
        </html>
  
- Python handler:

  - Required arguments:
  
    - user: current user (str)

    - db: database connection object (web.py database object)

    - url_id: url id (str)

    - url: url (str)

    - content: content (str)

    - param: parameter (web.input())

    - data: additional data (helper functions, UDFs, templates, modules, etc) (dict)

  - Function *must* return a list of two members:
  
    - headers, empty list OR list of [HTTP header name, HTTP header value]
    
    - content (str)
    
  - Example (url id: test, url: /test, url: test?hello=world):
    ::

        def web_test(user, db, url_id, url, content, param, data):
            headers = [
                            ['Content-Type', 'text/plain'],
                        ]
            content = 'hello %s' %(param.get('hello', ''))
            return [headers, content]

- POST method:

  - Can only be handled by a python function named post_<id> (in sqliteboy_user.py,
    please also read PYTHON HANDLER REFERENCE)
    
  - If there is an exception, or handler is not available, an empty string
    is returned
    
  - Example (url id: form, url: /form):
    ::

        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
        <form action="/form" method="post">
        Hello <input type="text" name="name">
        <input type="submit">
        </form>
        </body>
        </html>
        
  - POST method handler:
    ::
    
        def post_form(user, db, url_id, url, content, param, data):
            headers = [
                            ['Content-Type', 'text/plain'],
                        ]
            content = 'POST: hello %s' %(param.get('name', ''))
            return [headers, content]      

- Custom not found URL:

  - Can be set at System configuration

  - Only applicable when not logged in
  
  - Please set to existing custom URL

- Note: it is probably a good idea to consider/use a reverse proxy 


User-defined Function
========================================================================

Note: please use SQLite built-in functions whenever and wherever possible.

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

- sqliteboy_randstr(s, a, b)
  ::

      random string
      argument    :
         s (set characters)
         a (min length, > 0)
         b (max length, > 0, >=a)

      example     :
         sqliteboy_randstr('abcdef123456', 3, 8)
         -> 'e2e6'

      tips        :
      - fix length: a = b
      - use sqliteboy_randstr2() or sqliteboy_randstr3() for predefined
        set characters
      - use sqliteboy_randstr_simple() for simple random string

- sqliteboy_randstr2(a, b)
  ::

      random string (predefined set characters, letters + digits + punctuation)
      argument    :
         a (min length, > 0)
         b (max length, > 0, >=a)

      example     :
         sqliteboy_randstr2(3, 8)
         -> '"Z\@Z'

- sqliteboy_randstr3(a, b)
  ::

      random string (predefined set characters, letters + digits)
      argument    :
         a (min length, > 0)
         b (max length, > 0, >=a)

      example     :
         sqliteboy_randstr3(3, 8)
         -> 'nItJ8'

- sqliteboy_randstr_simple()
  ::

      random string (simple)
      example     :
         sqliteboy_randstr_simple()
         -> 'VUmDAQeJCpww9IjmiexrWRuRT6ZgpacKVdOA'

- sqliteboy_is_datetime_format(s, fmt)
  ::

      is date time according to format
      argument    :
         s (input string)
         fmt (date time format string)

      example     :
         sqliteboy_is_datetime_format('2014', '%Y')
         -> 1

         sqliteboy_is_datetime_format('2014-01-01', '%Y-%m-%d')
         -> 1

         sqliteboy_is_datetime_format('2014-01-01', '%Y-%m-%d %H:%M:%S')
         -> 0

         sqliteboy_is_datetime_format('2014-01-01 01:02:03', '%Y-%m-%d %H:%M:%S')
         -> 1

      tips        :
      - use sqliteboy_is_datetime(), sqliteboy_is_date() or sqliteboy_is_time()
        for predefined date time format

- sqliteboy_is_datetime(s)

- sqliteboy_is_date(s)

- sqliteboy_is_time(s)

- sqliteboy_time()

- sqliteboy_time2(s)
  ::

      get time from string (YYYY-MM-DD HH:MM:SS)
      argument    :
         s (date/time string)

      example     :
         sqliteboy_time2('2012-03-28 19:20:21')
         -> 1332937221.0

- sqliteboy_time2_date(s)
  ::

      sqliteboy_time2() using YYYY-MM-DD format

- sqliteboy_time2_format(s, fmt)
  ::

      sqliteboy_time2() using custom format

- sqliteboy_time3(f)
  ::

      get string (YYYY-MM-DD HH:MM:SS) from time (local time)
      argument    :
         f (time)

      example     :
         sqliteboy_time3(1)
         -> 1970-01-01 07:00:01
         -> timezone is UTC+7

- sqliteboy_time3a()
  ::

      alias for sqliteboy_time3(sqliteboy_time())

- sqliteboy_time4(f)
  ::

      get string (YYYY-MM-DD HH:MM:SS) from time (UTC)
      argument    :
         f (time)

      example     :
         sqliteboy_time4(1)
         -> 1970-01-01 00:00:01

- sqliteboy_time4a()
  ::

      alias for sqliteboy_time4(sqliteboy_time())

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
         empty/invalid s1 or s2: current date/time (localtime)
         use sqliteboy_number_format() to format the result

- sqliteboy_time6(f, year, month, day, mode)
  ::

      format the difference between two dates in
      y (years) m (months) d (days) format
      argument    :
         f (number, in year, use sqliteboy_time5 function (mode=5) )
         year (year string)
         month (month string)
         day (day string)
         mode (1=30.44 days/month, 1=30 days/month, 2=31 days/month)

      example     :
         sqliteboy_time6(sqliteboy_time5('2010-11-12 01:02:03', '2011-12-13 11:12:13', 5), ' years ', ' months ', ' days ', 0)
         -> 1 years 1 months 1 days

         sqliteboy_time6(sqliteboy_time5('2010-11-12 01:02:03', '2011-10-11 11:12:13', 5), ' years ', ' months ', ' days ', 0)
         -> 0 years 10 months 29 days

         sqliteboy_time6(sqliteboy_time5('2013-01-01 10:20:30', '2013-01-02 10:20:30', 5), ' years ', ' months ', ' days ', 0)
         -> 0 years 0 months 1 days

         sqliteboy_time6(sqliteboy_time5('2013-01-02 10:20:30', '2013-01-01 10:20:30', 5), ' years ', ' months ', ' days ', 0)
         -> 0 years 0 months -1 days

         sqliteboy_time6(1000, ' years ', ' months ', ' days ', 0)
         -> 1000 years 0 months 0 days

         sqliteboy_time6(1.5, ' years ', ' months ', ' days ', 0)
         -> 1 years 6 months 0 days

         sqliteboy_time6(1.24, ' years ', ' months ', ' days ', 0)
         -> 1 years 2 months 27 days

         sqliteboy_time6(1.24, ' years ', ' months ', ' days ', 1)
         -> 1 years 2 months 26 days

         sqliteboy_time6(1.24, ' years, ', ' months, ', ' days', 0)
         -> 1 years, 2 months, 27 days

         sqliteboy_time6(1.24, ' tahun ', ' bulan ', ' hari ', 0)
         -> 1 tahun 2 bulan 27 hari

- sqliteboy_is_leap(n)
  ::

      is leap year
      argument    :
         n (year)

      return value:
        1 (leap year) or 0 (not leap year)

- sqliteboy_datetime_format(fmt)
  ::

      format date time
      argument    :
         fmt (format string)

- sqliteboy_datetime_format_local(fmt)
  ::

      format date time (local)
      argument    :
         fmt (format string)

- sqliteboy_date()
  ::

      get current date in YYYY-MM-DD format

- sqliteboy_date_local()
  ::

      get current date (local) in YYYY-MM-DD format

- sqliteboy_date_delta_format(s, fmt, n)
  ::

      get date delta (days) from date string, using custom format
      argument    :
         s (date string)
         fmt (format string)
         n (days)

- sqliteboy_date_local_delta_format(s, fmt, n)
  ::

      get date delta (days) from date string, using custom format
      (local time)
      argument    :
         s (date string)
         fmt (format string)
         n (days)

- sqliteboy_date_delta(s, n)
  ::

      get date delta (days) from date string (YYYY-MM-DD)
      argument    :
         s (date string)
         n (days)
      
- sqliteboy_date_local_delta(s, n)
  ::

      get date delta (days) from date string (YYYY-MM-DD)
      (local time)
      argument    :
         s (date string)
         n (days)

- sqliteboy_today_local_delta(n)
  ::

      get date delta (days) from current date (YYYY-MM-DD)
      (local time)
      argument    :
         n (days)

- sqliteboy_today_local_delta_hour(n)
  ::

      get date delta (days) from current date/time (YYYY-MM-DD)
      (local time)
      argument    :
         n (hours)

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

- sqliteboy_split0(s, separator, index)
  ::

      split string s using separator as the delimiter string and
      return index (in list)
      argument    :
         s (input string)
         separator (separator string)
         index (index)

      return value:
        index (in list) or ''

      example     :
        sqliteboy_split0('s.q.l.i.t.e.b.o.y', '.', 1)
        -> 'q'

        sqliteboy_split0('s.q.l.i.t.e.b.o.y', '', 1)
        -> ''

        sqliteboy_split0('s.q.l.i.t.e.b.o.y', '.', -3)
        -> 'b'

        sqliteboy_split0('h e l l o', '', 1)
        -> 'e'

      tips        :
         empty separator: use whitespace

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

- sqliteboy_lookup1(table, field, field1, value1, function, distinct)
  ::

      (not available in HTML template interpretation)

      SELECT <function>(<field>) FROM <table> WHERE <field1>=<value1>
      and
      return function result
      argument    :
         table (table name)
         field (field name)
         field1 (where field)
         value1 (where field value)
         function (avg, count, group_concat, max, min, sum, total)
         distinct (0=non distinct, 1=distinct)

      return value:
        function result (as str) or '' (error)

      example     :
        data in 'lookup' table:
        | a | b |
        ---------
        |a  | 0 |
        |a  | 1 |
        |a1 | 2 |
        |a2 | 3 |

        sqliteboy_lookup1('lookup', 'b', 'a', 'a', 'avg', 0)
        -> '0.5'

        sqliteboy_lookup1('lookup', 'a', 'a', 'a', 'count', 0)
        -> '2'

        sqliteboy_lookup1('lookup', 'a', 'a', 'a', 'count', 1)
        -> '1'

        sqliteboy_lookup1('lookup', 'a', 'a', 'a', 'group_concat', 0)
        -> 'a,a'

        sqliteboy_lookup1('lookup', 'b', 'a', 'a', 'max', 0)
        -> '1'

        sqliteboy_lookup1('lookup', 'b', 'a', 'a', 'min', 0)
        -> '0'

        sqliteboy_lookup1('lookup', 'b', 'a', 'a', 'sum', 0)
        -> '1'

        sqliteboy_lookup1('lookup', 'b', 'a', 'a2', 'total', 0)
        -> '3.0'

- sqliteboy_lookup2(table, field, field1, value1, order, default)
  ::

      (not available in HTML template interpretation)

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

      (not available in HTML template interpretation)

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

- sqliteboy_split1(s, separator, table, column, convert)
  ::

      (not available in HTML template interpretation)

      split string s using separator as the delimiter string and
      insert into table (column) for each member in list
      argument    :
         s (input string)
         separator (separator string)
         table (table to insert)
         column (column in table)
         convert(0=no conversion, 1=convert to column type if applicable (or to string) )

      return value:
        number of row(s) inserted into table, or 0

      example     :
        sqliteboy_split1('h.e.l.l.o.w.o.r.l.d', '.', 'test_split', 'c', 1)
        -> 10

        sqliteboy_split1('hello', '', 'test_split', 'c', 0)
        -> 1

      tips        :
         empty separator: use whitespace

- sqliteboy_list_datetime1(s, n, interval, table, column, local)
  ::

      (not available in HTML template interpretation)

      generate list of datetime starting with s (inclusive),
      as much as n, with interval,
      and insert into table (column) for each member in list
      argument    :
         s (YYYY-MM-DD HH:MM:SS)
         n (as much as, must be > 0)
         interval (interval in seconds, must not zero)
         table (table to insert)
         column (column in table)
         local (0=UTC, 1=local)

      return value:
        number of row(s) inserted into table, or 0

      example     :
        (local timezone is UTC+7)

        sqliteboy_list_datetime1('', 5, 60*60*24, 'test_date', 'a', 1)
        -> 5
        (data in table)
        2013-06-03 23:13:27
        2013-06-04 23:13:27
        2013-06-05 23:13:27
        2013-06-06 23:13:27
        2013-06-07 23:13:27

        sqliteboy_list_datetime1('', 5, 60*60*24, 'test_date', 'a', 0)
        -> 5
        (data in table)
        2013-06-03 16:14:09
        2013-06-04 16:14:09
        2013-06-05 16:14:09
        2013-06-06 16:14:09
        2013-06-07 16:14:09

        sqliteboy_list_datetime1('', 5, -60*60*24, 'test_date', 'a', 1)
        -> 5
        (data in table)
        2013-06-03 23:14:55
        2013-06-02 23:14:55
        2013-06-01 23:14:55
        2013-05-31 23:14:55
        2013-05-30 23:14:55

        sqliteboy_list_datetime1('2013-01-01 00:00:00', 5, 60*60, 'test_date', 'a', 1)
        -> 5
        (data in table)
        2013-01-01 00:00:00
        2013-01-01 01:00:00
        2013-01-01 02:00:00
        2013-01-01 03:00:00
        2013-01-01 04:00:00

      tips        :
         empty s: current date/time (localtime)

- sqliteboy_if(s, a, b)
  ::

      (not available in HTML template interpretation)

      if s, return a, else return b
      argument    :
         s (SQL query, must return column alias named 'if')
         a (return this, if 'if' column considered true)
         b (return this, if 'if' column considered false)

      return value:
        a or b, or '' (error)

      example     :
        sqliteboy_if('select 1 as if' , 'True', 'False')
        -> 'True'

        sqliteboy_if('select -1 as if' , 'True', 'False')
        -> 'True'

        sqliteboy_if('select 0 as if' , 'True', 'False')
        -> 'False'

        sqliteboy_if('select -1 as if' , 1, -1)
        -> 1

        sqliteboy_if('select "" as if' , 'True', 'False')
        -> 'False'

        sqliteboy_if('select "sqliteboy" as if' , 'True', 'False')
        -> 'True'

        sqliteboy_if('select 1' , 'True', 'False')
        -> ''

      tips        :
         for SQLite built-in command, please use CASE expression

- sqliteboy_http_remote_addr()
  ::

    return value  :
        http remote address

- sqliteboy_http_remote_addr_ext()
  ::

    return value  :
        http remote address (read HTTP_X_FORWARDED_FOR)

- sqliteboy_http_user_agent()
  ::

    return value  :
        http user agent (for example: web browser)

- sqliteboy_app_title()
  ::

      return value:
        application title

      example     :
        sqliteboy_app_title()
        -> 'sqliteboy 1.10'

- sqliteboy_var_set(name, value)
  ::

      (not available in HTML template interpretation)

      user-defined variable: set
      (max per user apply)
      argument    :
         name (variable name, underscore and alphanumeric only, not case-sensitive)
         value (value)

      return value:
        1 (ok) or 0

      example     :
        sqliteboy_var_set('a', 1000)
        -> 1

        sqliteboy_var_set('b', 'hello')
        -> 1

      tips        :
        to free some space, please use sqliteboy_var_del function below,
        setting to empty string or 0 does not delete the variable

- sqliteboy_var_get(name)
  ::

      (not available in HTML template interpretation)

      user-defined variable: get
      argument    :
         name (variable name, underscore and alphanumeric only, not case-sensitive)

      return value:
        value of variable or ''

      example     :
        sqliteboy_var_get('a')
        -> 1000

        sqliteboy_var_get('b')
        -> hello

- sqliteboy_var_del(name)
  ::

      (not available in HTML template interpretation)

      user-defined variable: delete
      argument    :
         name (variable name, underscore and alphanumeric only, not case-sensitive)

      return value:
        1 (ok) or 0

      example     :
        sqliteboy_var_del('a')
        -> 1

        sqliteboy_var_del('b')
        -> 1

- sqliteboy_strip_html(s)
  ::

      strip html
      argument    :
         s (input string)

      example     :
        sqliteboy_strip_html('<b>hello</b>')
        -> 'hello'

- sqliteboy_x_user()
  ::

    (not available in HTML template interpretation)

    return value  :
        user name (if extended feature is enabled, or '')

- sqliteboy_x_profile_all(u, field, system)
  ::

      (not available in HTML template interpretation)

      read user profile (both system and user-defined)

      argument    :
         u (user)
         field (custom field)
         system (0=user-defined, 1=system)

      return value:
        field value (if extended feature is enabled and field is set,
        or '')

- sqliteboy_x_profile(u, field)
  ::

      (not available in HTML template interpretation)

      read custom field in user-defined profile for user u
      Please read USER-DEFINED PROFILE REFERENCE section (below)

      argument    :
         u (user)
         field (custom field)

      return value:
        field value (if extended feature is enabled and field is set,
        or '')

- sqliteboy_x_profile_system(u, field)
  ::

      (not available in HTML template interpretation)

      read system profile for user u
      Please read SYSTEM PROFILE REFERENCE section (below)

      argument    :
         u (user)
         field (field)

      return value:
        field value (if extended feature is enabled and field is set,
        or '')

- sqliteboy_x_my(field)
  ::

      (not available in HTML template interpretation)

      alias for sqliteboy_x_profile(sqliteboy_x_user(), field)

- sqliteboy_x_my_system(field)
  ::

      (not available in HTML template interpretation)

      alias for sqliteboy_x_profile_system(sqliteboy_x_user(), field)


Form Code Reference
========================================================================

- Must be valid JSON syntax (json.org)

- String (including keys below) must be double-quoted
  (between " and ")

- No trailling comma in dict or list

- Python dict (keys are case-sensitive)

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
  
- Extended result message is supported, as an alternative to custom result
  message. Using extended result, it is possible to perform operations on 
  form fields, and use the result. Like custom result message, it is based 
  on SQL query result. But unlike custom result message, the result is 
  not limited to integer (can be string or another types; probably returned 
  from function call). 

- Optional, additional SQL query statement(s) can be provided, and each
  of them will be executed in order, if you need to perform additional
  task(s), after the form data is saved (for example, write to another
  table). Previously, one might use report if need to write to several
  tables. Last insert rowid value is provided.

- Insert into table can be disabled by setting insert key to zero/negative
  value. This is useful if you need to update/delete data in table(s), using
  additional SQL query statement(s). By default, form/subform save will
  insert new row(s) into table(s). Please note that setting insert key
  to zero/negative value will also set last insert rowid/query result
  to same value as insert value.

- Please also read PYTHON HANDLER REFERENCE section

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
|               |                         |               |             |                          |
|               | (html is allowed)       |               |             |                          |
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
|               | - $<column> will be     |               |             |                          |
|               |   replaced by user input|               |             |                          |
|               |   value for that column |               |             |                          |
|               |                         |               |             |                          |
|               | - $last_insert_rowid    |               |             |                          |
|               |   will be replaced by   |               |             |                          |
|               |   last_insert_rowid()   |               |             |                          |
|               |   function call result  |               |             |                          |
|               |   (after insert to main |               |             |                          |
|               |   table)                |               |             |                          |
|               |                         |               |             |                          |
|               | - $python_handler       |               |             |                          |
|               |   will be replaced by   |               |             |                          |
|               |   return value of python|               |             |                          |
|               |   handler (if provided, |               |             |                          |
|               |   default: -1)          |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
|               | (html is allowed)       |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| result        | extended result message | list          | optional    |                          |
|               |                         |               |             |                          |
|               |                         |               |             | [                        |
|               | - not applicable to     |               |             |  "$a + $b = $result",    |
|               |   subform               |               |             |  "select $a+$b as result"|
|               |                         |               |             | ]                        |
|               | - must be list of two   |               |             |                          |
|               |   members (str)         |               |             | (Example 3)              |
|               |                         |               |             |                          |
|               |   ["template",          |               |             |                          |
|               |   "sql query"]          |               |             |                          |
|               |                         |               |             |                          |
|               | - $result (in template) |               |             |                          |
|               |   will be replaced by   |               |             |                          |
|               |   actual SQL Query      |               |             |                          |
|               |   result                |               |             |                          |
|               |                         |               |             |                          |
|               | - $<column> will be     |               |             |                          |
|               |   replaced by user input|               |             |                          |
|               |   value for that column |               |             |                          |
|               |                         |               |             |                          |
|               | - $last_insert_rowid    |               |             |                          |
|               |   will be replaced by   |               |             |                          |
|               |   last_insert_rowid()   |               |             |                          |
|               |   function call result  |               |             |                          |
|               |   (after insert to main |               |             |                          |
|               |   table)                |               |             |                          |
|               |                         |               |             |                          |
|               | - $python_handler       |               |             |                          |
|               |   will be replaced by   |               |             |                          |
|               |   return value of python|               |             |                          |
|               |   handler (if provided, |               |             |                          |
|               |   default: -1)          |               |             |                          |
|               |                         |               |             |                          |
|               |                         |               |             |                          |
|               | (html is allowed)       |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| sql0          | additional sql query    | list          | optional    |                          |
|               | statement(s)            |               |             |                          |
|               |                         |               |             |                          |
|               | (run before)            |               |             |                          |
|               |                         |               |             |                          |
|               | (please see sql2)       |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| sql2          | additional sql query    | list          | optional    |                          |
|               | statement(s)            |               |             |                          |
|               |                         |               |             |                          |
|               | (run after)             |               |             |                          |
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
|               |   (sql2 only)           |               |             |                          |
|               |                         |               |             |                          |
|               | - quoting is            |               |             |                          |
|               |   automatically done    |               |             |                          |
|               |                         |               |             |                          |
|               | - each statement is     |               |             |                          |
|               |   executed in           |               |             |                          |
|               |   transaction           |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| insert        | prevent insert new      | int           | optional    |                          |
|               | row(s) into table(s)    |               |             |                          |
|               | on form/subform save,   |               |             |                          |
|               | if zero/negative value  |               |             |                          |
|               | is given                |               |             |                          |
|               |                         |               |             |                          |
|               | (noted above)           |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| confirm       | confirmation message    | str           | optional    |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| focus         | autofocus column        | str           | optional    |                          |
|               |                         |               |             |                          |
|               | (please see "column"    |               |             |                          |
|               | key in data)            |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| link          | links                   | list of list  | optional    | [["http://sqliteboy.com",|
|               |                         | of two members|             |  "sqliteboy"]]           |
|               |                         |               |             |                          |
|               |                         | [target,label]|             |                          |
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
|               | - int: flag             |               |             | - 2                      |
|               |   (2: HTML input        |               |             |                          |
|               |   password)             |               |             |                          |
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
|               | - list (SQL query):     |               |             |                          |
|               |   must be list of two   |               |             |                          |
|               |   str members; first    |               |             |                          |
|               |   member: empty string; |               |             |                          |
|               |   second member: SQL    |               |             |                          |
|               |   query (must return    |               |             |                          |
|               |   one column: a)        |               |             |                          |
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
      "focus" : "d",
      "link" : [["http://sqliteboy.com","sqliteboy"]],
      "message"  : ["unknown result", "zero result", "success: $result"],
      "security" : {
                     "run" : ""
                   }
    }

- Example 3:
::

    {
          "title" : "Addition",
          "data"  : [
                      {
                        "table"     : "table1",
                        "column"    : "a"
                      },
                      {
                        "table"     : "table1",
                        "column"    : "b"
                      }
                    ],
          "insert" : 0,
          "result" : ["$a + $b = $result", "select $a+$b as result"],
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

- Python dict (keys are case-sensitive)

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

- Printer friendly version of report result is supported in default
  output format (HTML)

- Keys:

+---------------+-------------------------+---------------+-------------+--------------------------+
| Key           | Description             | Type          | Status      | Example                  |
+===============+=========================+===============+=============+==========================+
| data          | wizard/search data      | list of dict  | required    | see: Keys (data)         |
|               |                         |               | (might be   |                          |
|               |                         |               | empty list) |                          |
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
|               |                         |               |             |                          |
|               | (html is allowed)       |               |             |                          |
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
| align         | text align              | list          | optional    |                          |
|               |                         |               |             |                          |
|               | (please see header;     |               |             | - [1, 2]                 |
|               | only applicable if      |               |             |                          |
|               | header is set)          |               |             |                          |
|               |                         |               |             |                          |
|               | - HTML and PDF only     |               |             |                          |
|               |                         |               |             |                          |
|               | - must be list of int   |               |             |                          |
|               |                         |               |             |                          |
|               | - 0: left               |               |             |                          |
|               |                         |               |             |                          |
|               | - 1: center             |               |             |                          |
|               |                         |               |             |                          |
|               | - 2: right              |               |             |                          |
|               |                         |               |             |                          |
|               | - 3: justify            |               |             |                          |
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
|               | - $<column> will be     |               |             |                          |
|               |   replaced by user input|               |             |                          |
|               |   value for that column |               |             |                          |
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
|               |   $result will          |               |             |                          |
|               |   be replaced by sql    |               |             |                          |
|               |   query result (integer/|               |             |                          |
|               |   non-select, or -1),   |               |             |                          |
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
| paper         | paper size in point     | list          | optional    |                          |
|               | (1/72 inch)             |               |             |                          |
|               | (PDF)                   |               |             |                          |
|               |                         |               |             |                          |
|               | - must be list of two   |               |             |                          |
|               |   int/float members     |               |             |                          |
|               |   (width, height)       |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| margins       | margins in point        | list          | optional    |                          |
|               | (1/72 inch)             |               |             |                          |
|               | (PDF)                   |               |             |                          |
|               |                         |               |             |                          |
|               | - must be list of four  |               |             |                          |
|               |   int/float members     |               |             |                          |
|               |   (left, right, top,    |               |             |                          |
|               |   bottom)               |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| confirm       | confirmation message    | str           | optional    |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| focus         | autofocus field         | str           | optional    |                          |
|               |                         |               |             |                          |
|               | (please see "key" key   |               |             |                          |
|               | in data)                |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| link          | links                   | list of list  | optional    | [["http://sqliteboy.com",|
|               |                         | of two members|             |  "sqliteboy"]]           |
|               |                         |               |             |                          |
|               |                         | [target,label]|             |                          |
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
|               | - int: flag             |               |             | - 2                      |
|               |   (2: HTML input        |               |             |                          |
|               |   password)             |               |             |                          |
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
|               | - list (SQL query):     |               |             |                          |
|               |   must be list of two   |               |             |                          |
|               |   str members; first    |               |             |                          |
|               |   member: empty string; |               |             |                          |
|               |   second member: SQL    |               |             |                          |
|               |   query (must return    |               |             |                          |
|               |   one column: a)        |               |             |                          |
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
      "focus" : "a_e",
      "link" : [["http://sqliteboy.com","sqliteboy"]],
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

- form
  ::

      [form:name] -> link to run form (or empty string if the form is not available)
      [FORM:name] -> link to run form, followed by a line break (or empty string if the form is not available)

- report
  ::

      [report:name] -> link to run report (or empty string if the report is not available)
      [REPORT:name] -> link to run report, followed by a line break (or empty string if the report is not available)

- horizontal rule
  ::
  
      [-] -> <hr>

- Note: HTML tags will be stripped on page save

- Note: rendered in <pre></pre> tag

- Note: as of v1.59, page supports form/report


Number To Words Reference
========================================================================
- Supported languages:

  - id            : Bahasa Indonesia
  - en            : English (trillion billion million thousand scheme)
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


Script Code Reference
========================================================================

- Script can be used to automate the creation of tables
  (including addition of columns, for existing table),
  forms, reports or user-defined profiles

- Solution can be deployed in form of script, that can be uploaded
  and run by admin

- Notes on tables:

  - Multiple tables support

  - For each table, script developer must define valid columns

  - For each column, script developer must define valid name, type and
    flag

  - Valid column type: integer, real, char, varchar, text, blob, null

  - Valid column flag: 0, 1 (primary key), 2 (only for integer:
    primary key autoincrement)

  - Multiple primary key support (column flag 1 for multiple columns; do
    not use both flag 1 and 2 in same table)

  - Currently, default value is not supported

  - For existing table, addition of columns is supported

    - Developer could define columns and only non-existing ones will be added

    - Existing columns, if defined, will be compared. Error, if there is
      mismatch between new column type and existing column type.

- Notes on forms, reports:

  - Multiple forms, reports support

  - Error, if there is existing form or report

  - Please read FORM CODE REFERENCE section (forms) or
    REPORT CODE REFERENCE section (reports)

- Only valid value(s) will be read

- Script cannot be run if there is an error

- If there is exception while the script is running, any newly created
  table (if empty) will be explicitly deleted. However, newly added
  columns could not be deleted (easily).

- Script is designed to be run only once

- Must be valid JSON syntax (json.org)

- Must be put in single file

- String (including keys below) must be double-quoted
  (between " and ")

- No trailling comma in dict or list

- Python dict (keys are case-sensitive)

- Keys:

+---------------+-------------------------+---------------+-------------+--------------------------+
| Key           | Description             | Type          | Status      | Example                  |
+===============+=========================+===============+=============+==========================+
| name          | script name             | str           | required    | "my script 1"            |
+---------------+-------------------------+---------------+-------------+--------------------------+
| tables        | tables definition       | list of list  | required    | (please see Examples     |
|               |                         |               |             | below)                   |
|               | - must be list of list  |               |             |                          |
|               |   (table) or []         |               |             |                          |
|               |                         |               |             |                          |
|               | - for each table:       |               |             |                          |
|               |   ["tablename",         |               |             |                          |
|               |   [column], ...]        |               |             |                          |
|               |                         |               |             |                          |
|               | - for each [column]:    |               |             |                          |
|               |   ["name", "type", flag]|               |             |                          |
|               |   (please read notes    |               |             |                          |
|               |   above)                |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| forms         | forms definition        | list of list  | required    | (please see Examples     |
|               |                         |               |             | below)                   |
|               | - must be list of list  |               |             |                          |
|               |   (form) or []          |               |             |                          |
|               |                         |               |             |                          |
|               | - for each form:        |               |             |                          |
|               |   ["formname",          |               |             |                          |
|               |   {formcode}]           |               |             |                          |
|               |                         |               |             |                          |
|               | - formcode: valid form  |               |             |                          |
|               |   code (dict)           |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| reports       | reports definition      | list of list  | required    | (please see Examples     |
|               |                         |               |             | below)                   |
|               | - must be list of list  |               |             |                          |
|               |   (report) or []        |               |             |                          |
|               |                         |               |             |                          |
|               | - for each report:      |               |             |                          |
|               |   ["reportname",        |               |             |                          |
|               |   {reportcode}]         |               |             |                          |
|               |                         |               |             |                          |
|               | - reportcode: valid     |               |             |                          |
|               |   report code (dict)    |               |             |                          |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| profiles      | user-defined profiles   | list          | optional    | (please see Examples     |
|               |                         |               |             | below)                   |
|               |                         |               |             |                          |
+---------------+-------------------------+---------------+-------------+--------------------------+
| info          | script information      | str           | optional    | "Script Information"     |
+---------------+-------------------------+---------------+-------------+--------------------------+
| author        | author information      | str           | optional    | "(c) Author <email>"     |
+---------------+-------------------------+---------------+-------------+--------------------------+
| license       | license information     | str           | optional    | "license"                |
+---------------+-------------------------+---------------+-------------+--------------------------+

- Example 1:
::

    {
        "name": "my script",
        "info": "Script Information",
        "author": "(c) Author <email>",
        "license": "GPL",
        "tables": [
                        [
                            "new_table",
                            ["a", "integer", 1],
                            ["b", "integer", 1],
                            ["c", "integer", 1],
                            ["d", "text", 0]
                        ]
                    ],
        "forms": [
                    ],
        "reports": [
                    ]
    }

- Example 2:
::

    {
        "name": "my script 1",
        "info": "Script Information",
        "author": "(c) Author <email>",
        "license": "GPL",
        "tables": [
                        [
                            "new_table_1",
                            ["a", "integer", 1],
                            ["b", "integer", 1],
                            ["c", "integer", 1],
                            ["d", "text", 0]
                        ],
                        [
                            "new_table_2",
                            ["a", "integer", 2],
                            ["b", "integer", 0],
                            ["c", "integer", 0],
                            ["d", "text", 0]
                        ]
                    ],
        "forms": [
                        [
                            "new_form_1",
                            {
                              "title" : "New Form 1",
                              "info"  : "Form Information",
                              "data"  : [
                                          {
                                            "table"     : "new_table_1",
                                            "column"    : "a"
                                          },
                                          {
                                            "table"     : "new_table_1",
                                            "column"    : "b"
                                          }
                                        ],
                              "security" : {
                                             "run" : ""
                                           }
                            }
                        ],
                        [
                            "new_form_2",
                            {
                              "title" : "New Form 2",
                              "info"  : "Form Information",
                              "data"  : [
                                          {
                                            "table"     : "new_table_2",
                                            "column"    : "c"
                                          },
                                          {
                                            "table"     : "new_table_2",
                                            "column"    : "d"
                                          }
                                        ],
                              "security" : {
                                             "run" : ""
                                           }
                            }
                        ]
                    ],
        "reports": [
                        [
                            "new_report_1",
                            {
                              "title" : "New Report 1",
                              "info"  : "Report Information",
                              "header": ["a", "b"],
                              "sql"   : "select a,b from new_table_1 a where a > $input_a or b > $input_b",
                              "data"  : [
                                          {
                                            "key"       : "input_a",
                                            "label"     : "column a >",
                                            "default"   : "0"
                                          },
                                          {
                                            "key"       : "input_b",
                                            "label"     : "column b >",
                                            "default"   : "0"
                                          }
                                        ],
                              "security" : {
                                             "run" : ""
                                           }
                            }
                        ]
                    ],
        "profiles": [
                      [
                         "company",
                         "Company",
                         "select id as a, name as b from company",
                         0
                      ],
                      [
                         "sqliteboy",
                         "Happy SQLiteBoy user?",
                         [ [0,"no :("], [1,"yes :)"] ],
                         1
                      ],
                      [
                         "signature",
                         "Signature",
                         0,
                         ""
                      ]
                    ]

    }


System Profile Reference
========================================================================
- style: user interface style (int)

- first_name: first name (str)

- last_name: last name (str)

- email: email (str)

- website: website (str)


User-defined Profile Reference
========================================================================

- Custom field(s) in user profile can be added. This is useful,
  for example, in multi-company environment.

- System configuration

- Must be valid JSON syntax (json.org)

- String must be double-quoted (between " and ")

- No trailling comma in list

- Python list

- Each member in list, must be list of 4 members:

  - field name (underscore and alphanumeric only)

  - field label

  - reference (please refer to reference in FORM CODE REFERENCE
    or REPORT CODE REFERENCE)

  - default or initial value

- Field(s) in user-defined profile will always be saved as str.
  Conversion might be needed.

- In Form/Report/Query, user-defined profile can be read using
  sqliteboy_x_profile or sqliteboy_x_my function

- Example:
::

    [
      [
         "company",
         "Company",
         "select id as a, name as b from company",
         0
      ],
      [
         "sqliteboy",
         "Happy SQLiteBoy user?",
         [ [0,"no :("], [1,"yes :)"] ],
         1
      ],
      [
         "signature",
         "Signature",
         0,
         ""
      ]
    ]

- Example using sqliteboy_x_profile / sqliteboy_x_my function:
::

    select sqliteboy_x_my('company')

    select sqliteboy_x_profile('admin', 'company')

    select sqliteboy_as_integer(sqliteboy_x_profile('admin', 'company'))


Python Handler Reference
========================================================================

- Python handler eases the integration with external system
  (for example: ERP system). Python handler also could be useful in,
  for example, complex database operation, reading from/writing to
  external devices, etc.

- Availability:

  - Form

  - Report

  - Website

- All handlers must be put in sqliteboy_user.py, in current working
  directory.

- Form:

  - Only one handler is allowed for each form. If provided, it will
    be called, automatically.

  - function name: form_<form_name>. Please rename this function, if you
    need to temporarily disable python handler for that form.

  - function arguments:

    - user: current user (str)

    - db: database connection object (web.py database object)

    - parsed: parsed form data (list)

    - user_data: list of user input (list)

    - data: additional data (helper functions, UDFs, templates, modules, etc) (dict)

  - Function *must* return an integer. To get this value, developer can use
    $python_handler in custom form message. If there is exception, -1 will
    be assigned to $python_handler.

  - Please note that python handler is an additional action, called at
    the end. It will not replace the default/built-in form handler.

  - Integration with external system, for example, can be done by reading
    user input value from SQLiteBoy, and writing to external system

- Report:

  - Only one handler is allowed for each report. If provided, it will
    be called, automatically.

  - function name: report_<report_name>. Please rename this function, if you
    need to temporarily disable python handler for that report.

  - function arguments:

    - user: current user (str)

    - db: database connection object (web.py database object)

    - parsed: parsed report data (list)

    - user_data: list of user input (list)

    - data: additional data (helper functions, UDFs, templates, modules, etc) (dict)

  - Function may return an integer, list of dict or web.py database query
    result

  - Please note that python handler is a replacement to the sql query.
    Return value of function will be used as report result.

  - Integration with external system, for example, can be done by reading
    from external system

- Website: please read WEBSITE AND CUSTOM URL REFERENCE


Server Command Reference
========================================================================

- Server command (new in v0.81) can be used to do actions related to 
  server, database, development, or advanced usage, at the server side. 
  After running such command, SQLiteBoy server will quit. 

- Command is passed as third argument when running SQLiteBoy (after port)

- Command may require additional arguments, which must be concatenated to the command 
  (separated with a dash, for each argument)

- Command may also require additional files to be present

- Available commands:

  - generate_favicon (generates icon file, requires output file, new in v0.81)::
  
        python sqliteboy.py test.db 11738 generate_favicon-sqliteboy.ico
  
  - generate_pyinstaller (generates spec file, requires output and icon file, new in v0.82)::
  
        python sqliteboy.py test.db 11738 generate_pyinstaller-sqliteboy.spec-sqliteboy.ico
  
  - generate_build (generates version, icon, and spec file, new in v0.83)::
  
        python sqliteboy.py test.db 11738 generate_build
  
  - generate_version (generates version file, requires output file, new in v1.07)::
  
        python sqliteboy.py test.db 11738 generate_version-sqliteboy.version
  
  - enable_extended (enables extended features, new in v1.60)::
  
        python sqliteboy.py test.db 11738 enable_extended
  
  - enable_extended_allow_all (enables extended features and allows all hosts, new in v1.60)::

        python sqliteboy.py test.db 11738 enable_extended_allow_all

  - reset_admin_password (resets admin password to default password, new in v1.69)::
  
        python sqliteboy.py test.db 11738 reset_admin_password
  
  - disable_log (temporarily disables log, new in v1.70)::
  
        python sqliteboy.py test.db 11738 disable_log
  
  - restore_log (restores log, new in v1.70)::
  
        python sqliteboy.py test.db 11738 restore_log
  
- Note on usage: 

  - generate_favicon, generate_pyinstaller, generate_build, generate_version 
    are usually used in building standalone SQLiteBoy version

  - enable_extended and enable_extended_allow_all are provided in order 
    to easily enable extended features and allow connection from 
    all hosts (without using the web-based user interface). 
    This way, SQLiteBoy can be installed on a remote server, 
    connected to a database, and managed/accessed from another hosts. 
    Before v1.60, these steps must be done manually (because only
    local connection is allowed by default; probably using text-based 
    web browser on server without GUI). 

  - These commands are not intended for regular use. In order to run
    SQLiteBoy, please read HOW TO RUN.


Link Code Reference
========================================================================

- Must be valid JSON syntax (json.org)

- String (including keys below) must be double-quoted
  (between " and ")

- No trailling comma in dict or list

- Python dict (keys are case-sensitive)

- Additional/custom links at login page can be set at System configuration

- Keys must be non-empty strings, values must be lists (or empty lists), 
  and targets/labels must be non-empty strings. 
  Please note that strict checking is performed on link code. If there is
  an error, no link will be available.

- Keys:

+---------------+-------------------------+---------------+----------------------------------------+
| Key           | Description             | Type          | Example                                |
+===============+=========================+===============+========================================+
| login.main    | shown on login page     | list of list  | [["http://sqliteboy.com", "sqliteboy"]]|
|               | at links section        | of two members|                                        |
|               |                         |               |                                        |
|               |                         | [target,label]|                                        |
+---------------+-------------------------+---------------+----------------------------------------+
| login.extra   | shown on login page     | list of list  | [["http://sqliteboy.com", "sqliteboy"]]|
|               | after login form        | of two members|                                        |
|               |                         |               |                                        |
|               |                         | [target,label]|                                        |
+---------------+-------------------------+---------------+----------------------------------------+

- Example:
::

    {
      "login.main": [["http://sqliteboy.com", "sqliteboy"]],
      "login.extra": [["http://sqliteboy.com", "sqliteboy"]]
    }


Title Reference
========================================================================

- If extended feature is enabled:

  - Title bar:
  
    - Logged in::
    
        [sqliteboy] [<database name>] title 
        or
        [sqliteboy] [<database name>]
    
    - Not logged in::
    
        [sqliteboy] <login translation>
    
  - Main title:
  
    - Logged in: 
    
      - If Application title is set::

            <Application title>
            
            [<home translation>] [<database name>] title 
            or
            [<home translation>] [<database name>] 
       
      - If Application title is not set::

            [<home translation>] [<database name>] title 
            or
            [<home translation>] [<database name>] 

    - Not logged in:

      - If Application title is set::

            <Application title>

      - If Application title is not set::

            [sqliteboy] <login translation>

- If extended feature is not enabled:

  - Title bar::
  
        [sqliteboy] [<database name>] title 
        or
        [sqliteboy] [<database name>]
  
  - Main title::

        [<home translation>] [<database name>] title 
        or
        [<home translation>] [<database name>] 

- Default: 

  - <home translation> is home

  - <login translation> is login

- As of v1.58, SQLiteBoy version is no longer shown in titles


Logs
========================================================================

- Logs (new in v1.61) can be set in System configuration

- Access logs are saved in an SQLite database (table name: sqliteboy_log)

- Columns:

  - rowtime: timestamp in local time
  
  - a: REMOTE_ADDR
  
  - b: HTTP_X_FORWARDED_FOR
  
  - c: HTTP_USER_AGENT
  
  - d: user name
  
  - e: request method
  
  - f: path
  
  - g: query

- Note:

  - Use only absolute path and forward slash / for separator
  
  - On system configuration save, verification will be performed. 
    If verification fails, an empty string will be saved and access logs will be disabled.  

  - Please make sure that log database file is writable by current user
  
  - It is possible to use current database as log database. However, 
    because logs are written per HTTP request, it might impact the 
    database.  

- To view the logs, please use SQLiteBoy 

  - If the logs are stored in external SQLite database, please run another 
    SQLiteBoy instance to connect to the log database

  - If the logs are stored in the current database, please use table browse
    (admin) or reports

- To log only specific URLs (and discard everything else), please set in
  System configuration (new in v1.71). Please start each URL with / and 
  separate URLs with whitespace.


Monkey Programming Language
========================================================================

- Monkey programming language interpreter (new in v1.81)

- Availability:

  - interpreter (link)

  - notes

- Initial environments (as monkey identifiers):

  - SQLITEBOY_NAME
  
  - SQLITEBOY_VERSION_STRING

  - SQLITEBOY_VERSION_INTEGER



