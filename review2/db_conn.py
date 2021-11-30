import sqlite3 # built in database that comes with Python

conn = sqlite3.connect('my_db') # create the database if not exist
curs = conn.cursor()
# in this database I intend to store 'tod' items'
# userID integer
# id integer (and primary key)
# title is a string
# completed is an SQL boolean (true/false)
st = '''CREATE TABLE todos 
(userID int,
 id INT PRIMARY KEY,
 title VARCHAR(32),
 completed BOOL
 )'''
# we can execute the statement
curs.execute(st)
# commit and close the connection
conn.commit() # without this the xchanges will not persist in the db
conn.close()