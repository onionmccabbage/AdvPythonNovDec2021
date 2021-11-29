# a custom generator must yield generated values

def byteGen(start, stop_before):
    s = start
    while s < stop_before:
        yield bytes(s) # the 'yield' statement makes this into a generator
        s+= 1

if __name__ == '__main__':
    g = byteGen(60, 62)
    #  we can now use our generator
    print( g.__next__() )

    # for b in g:
    #     print(b)
    # check what we have
    print(g)