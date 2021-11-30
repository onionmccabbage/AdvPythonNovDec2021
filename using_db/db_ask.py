import sqlite3

def main():
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # ask user for valid values for name, qty and cost
    invalid = True
    while invalid:
        c = input('Creature name?')
        if type(c) == str and len(c) > 0: # check the length of the string
            invalid = False
    q = input('How many?')
    p = input('Cost?')
    # use '?' as a placeholder in SQL statements
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    # execute
    try:
        curs.execute(st, (c, q, p)) # replacee the '?' placeholders with actual values
        conn.commit()
    except Exception as err:
        print('There was a problem:{}'.format(err))
    finally:
        conn.close() # always make sure the connection is closed
if __name__ == '__main__':
    main()