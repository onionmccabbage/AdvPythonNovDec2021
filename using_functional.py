# recently functional programming has returned
# a pure function has no side-effects (entirely predictable)
# i.e. for given inputs the output is entirely determined
# Python provides the 'functools' library
from functools import reduce

def square(x):
    return x*x

def add(x, y):
    return x + y

def isOdd(n):
    return n%2 != 0 # True or False if even or odd   

if __name__ == '__main__':
    # we may need a list of square numbers: we can 'map' our values into the function
    sq_l = list(map ( square, range(1,6) ))
    print( sq_l )
    # we also have a filter function
    odd_l = list( filter( isOdd, range(1,10) )) # isOdd, range(-10**1000, 10**1000) ) )
    print(odd_l)

    # using 'reduce'
    r = reduce( add, odd_l, 10 ) # sum every value from the odd list and add ten!!
    print( r )