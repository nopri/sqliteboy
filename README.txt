sqliteboy.py
Simple Web SQLite Manager/Form Application
(c) Noprianto <nop@tedut.com>
2012 
GPL


SCREENSHOTS: https://github.com/nopri/sqliteboy/wiki


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
- Query
  - Free form SQL Query
  - Automatically view query output (as integer or table)
- Easy to translate
- Allow for local connection only (configurable once user account is done)
- Human readable database size (GB, MB, KB, B)
- Load time
- Custom Template
- Minimum use of Javascript in default/builtin template
  (only for delete selected confirmation and toggle select all)
- Form support (simple data entry) in version 0.05
  (should be available before 2013)
- Table name limitation: 
  could not handle table with whitespace in name 
  

REQUIREMENTS:
- python
- web.py
- SQLite module (included as sqlite3, in python 2.5+)


RUN:
- python sqliteboy.py <database_file> [port]
  (then, using web browser, visit localhost:11738, 
   or localhost:PORT, if PORT is specified)


CUSTOM TEMPLATE
- sqliteboy.html, if found in current directory
- For template example: T_BASE variable


THANK YOU :)

