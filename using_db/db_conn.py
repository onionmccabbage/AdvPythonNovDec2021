import sqlite3 # built in database that comes with Python

# make a conection to this database
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