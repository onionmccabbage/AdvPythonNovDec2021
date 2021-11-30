import sqlite3

conn = sqlite3.connect('my_db')
curs = conn.cursor()
st = '''
SELECT creature, cost, count FROM zoo
'''
# execute
try:
    curs.execute(st)
    rows = curs.fetchall()
except Exception as err:
    print('There was a problem:{}'.format(err))
finally:
    conn.close() # always make sure the connection is closed

# we can explore the 'rows'
for animal in rows:
    # print(animal)
    print('Creature:{0}\tcosts {1} each\tand we have {2}.'.format( animal[0], animal[1], animal[2] ))