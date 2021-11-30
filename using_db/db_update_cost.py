# make use of other code
# allow user to update cost to a positive float
import sqlite3

def main():
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # ask user for a valid creature name
    invalid = True
    while invalid:
        c = input('Creature name?')
        if type(c) == str and len(c) > 0: # check the length of the string
            invalid = False
    # ask use what is the updated quantity for this creature
    invalidCost = True
    while invalidCost:
        p = input('How much?') # NB input ALWAYS returns a string!!!
        p_float = float(p) # cast the string to an integer
        if type(p_float) == float and p_float >= 0.0:
            invalidCost = False # ends our 'while' loop
    # we conventionaly capitalize sql key words
    st = '''
    UPDATE zoo
    SET cost = {}
    WHERE creature IS "{}"
    '''.format(p_float, c) # inject user values into the SQL statement
    # execute
    try:
        curs.execute(st)
        conn.commit()
    except Exception as err:
        print('There was a problem:{}'.format(err))
    finally:
        conn.close() # always make sure the connection is closed
if __name__ == '__main__':
    main()