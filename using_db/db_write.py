import sqlite3

conn = sqlite3.connect('my_db')
curs = conn.cursor()
st = '''
INSERT INTO zoo
VALUES ("Ocelot", 32, 1.09)
'''
# execute
try:
    curs.execute(st)
    conn.commit()
except Exception as err:
    print('There was a problem:{}'.format(err))
finally:
    conn.close() # always make sure the connection is closed
