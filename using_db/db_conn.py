import sqlite3 # built in database that comes with Python

# make a conection to this database
# DB2
# import DB2
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username",
# passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")

conn = sqlite3.connect('my_db') # create the database if not exist
# we also need a cursor (to access members of the db)
curs = conn.cursor()
# in this database I intend to store zoo animals
# create name      string of up to 32 characters
# count (how many) integer
# maintenance cost float
# we can write an SQL statement
st = '''CREATE TABLE zoo 
(creature VARCHAR(32) PRIMARY KEY,
 count INT,
 cost FLOAT
 )'''
# we can execute the statement
curs.execute(st)
# commit and close the connection
conn.commit() # without this the xchanges will not persist in the db
conn.close()