# iter is built in to python
# it lets us iterate

l = [ False, 7, 'text', (5,4,3) ]

l_iter = iter(l)# we now have an iterable from our list

print(l_iter.__next__() ) # use it like a generator
print(l_iter.__next__() ) # use it like a generator
print(l_iter.__next__() ) # use it like a generator
print(l_iter.__next__() ) # use it like a generator

# can we do this on the original list?
# print(l.__next__()) # fails

# iter has built-in reverse capabilities
r = reversed(l)
print( r.__next__() )
# we can still use conventional iteration
for i in r:
    print(i)