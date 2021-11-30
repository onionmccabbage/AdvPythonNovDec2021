# in Python 3 there is a context manager
from contextlib import contextmanager
import sys

@contextmanager # make this function able to manage contexts
def stdout_redirect(new_stdout):
    save_stdout = sys.stdout # keep a record of the current standard output
    sys.stdout  = new_stdout # redirect output
    yield # this will yield the next available object to be written
    sys.stdout = save_stdout # set the output back to what it was before

if __name__ == '__main__':
    with open('my_log.txt', 'a') as fobj: #remember, 'with' will auto-close our file access object
        with stdout_redirect(fobj):
            # we can write multiple lines...
            print('''This is
redirected 
by our decorated
method
            ''')
    print('back to the terminal')
