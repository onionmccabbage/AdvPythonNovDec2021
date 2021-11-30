import sqlite3

def main():
    # we need a structure for the data members to be added to our db
    creatures_t = ({'creature':'Albatros', 'count':1,   'cost':120.99},
    {'creature':'Bear',     'count':5,   'cost':32.56},
    {'creature':'Carp',     'count':120, 'cost':120.99},
    {'creature':'Deer',     'count':32,  'cost':12.99},
    {'creature':'Eel',      'count':7,   'cost':73.82})

    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # iterate over our structure
    # use '?' as a placeholder in SQL statements
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    for item in creatures_t:
        # execute
        try:
            curs.execute(st, (item['creature'], item['count'], item['cost'])) # replace the '?' placeholders with actual values
            conn.commit()
        except Exception as err:
            print('There was a problem:{}'.format(err))
        finally:
            pass
    # when done, we need to close our connection    
    conn.close() # always make sure the connection is closed
if __name__ == '__main__':
    main()