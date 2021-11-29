# writing and reading to persistent files
# every file without exception is made up of bytes

def main():
    # create a file access object
    fout = open('out.txt', 'at') # 'at' to append text 'w' to overwrite 'x' exclusive access
    # we can switch the context of the print function so it outputs to pur file access object
    print('here is some text', file=fout)
    fout.close()

def read_lines():
    try:
        with (open('out.txt', 'r')) as fin: # iterate over the file access object
            l = fin.readline() # read a line
            print('rececived {}'.format(l))
    except Exception as e:
        print(e)
    finally:
        pass
        # fin.close() # no need to close, since hte 'with' operatopr will auto-close when done

def my_read():
    try:
        fin = open('out.txt', 'rt') # 'rt' will read text
        r = fin.read()
        print(r)
    except Exception as e:
        print(e)
    finally: # always runs, even if there was an exception
        fin.close() # always a good idea to clean up

if __name__ == '__main__':
    main()
    my_read()
    read_lines()