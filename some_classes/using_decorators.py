# we can declare our own custom decorators
# a decorator function
def show_args(f): # we can pass anything into a function, even another function
    def new_func(*args, **kwargs): 
        # *args is the tuple of all positional arguments
        # **kwargs is the dict of all keyword arguments
        print('We are running the function called {}'.format(f.__name__))
        print('Positional arguments are: {}'.format(args))
        print('Keyword arguments are: {}'.format(kwargs))
        return f(*args, **kwargs)
    return new_func

# a normal function
@show_args # use our decorator
def addInts(a, b):
    return a+b

@show_args
def other(m,n):
    return m**n

if __name__ == '__main__':
    x, y = (1,2) # this unpacks the tuple (does not alter the tuple)
    print(addInts(x,y)) # 3
    print( other( n=3, m=10 ) )

