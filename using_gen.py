# generators can yield values on demand
# here is a range
r = range(0,10)
# we can make a generator
g = ( i for i in r ) # NB the brackets are a generator, (not a tuple)
l = [ i for i in r ] # this is a LIST generator, where all the values exist in memory
o = ( i for i in range(0, 101, 10) ) # another generator

if __name__ == '__main__':
    print(g, l)
    # we can iterate over our list and over our generator
    for v in g:
        print(v, end=', ')

    # we can still iterate over our list
    for v in l:
        print(v, end='. ') 
    for v in l: # the list is still in memory
        print(v, end='- ')  

    # we cannot iterate over the generator again, since it has been exhausted
    for v in g:
        print(v, end=', ') # no output!!

    # we can call generated values on demand
    print( o.__next__() ) # outputs 0 (the item at position 0 of the generator)
    print( o.__next__() ) # outputs 10 (the item at position 1 of the generator)
    print( o.__next__() ) # outputs 20 (the item at position 2 of the generator)