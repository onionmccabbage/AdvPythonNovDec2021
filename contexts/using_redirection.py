# we may wish to send output to something other than the default console/terminal
# e.g. a log file print('data', file=fout)
# or to a database, to another pyhton module, to a stream etc.

import sys # the default streama are stdout (and stdin)

class Redirect: # the brackets are optional - we inherit by default from 'object'
    """
    Provide an easy way to redirect the standard output
    (which defaults to pritning to the console)
    """
    def __init__(self, new_stdout): # we can pass ANYTHING to this context
        self.new_stdout = new_stdout # store our choice
    def __enter__(self): # override the built-in __enter__ method
        '''Implement a redirect for output'''
        self.orig_stdout = sys.stdout # make a record of the current stdout
        sys.stdout = self.new_stdout  # set a new stdout
    def __exit__(self, exc_type, exc_value, exc_traceback): # enter and exit are 'lifecycle' methods of every class
        '''Restore the original stdout'''
        sys.stdout = self.orig_stdout


if __name__ == '__main__':
    print('Currently, stdout is {}'.format(sys.stdout))
    # use 'with' to auto-close the file acess object
    with open('mylog.txt', 'a') as fobj: # simple text file output
        # also note: 'with' will auto-close the Redirect class, calling it's __exit__ method
        with Redirect(fobj): # we will use our file access object as the new stdout
            print('this gets directed to our log file')
    print('normal output has been restored')

