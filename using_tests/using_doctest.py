import doctest
def nthPower(d, p):
    '''
    This function will return the nth power of a number
    We can use doctest to write tests within te doc string like this
    >>> nthPower(3, 2)
    9
    >>> nthPower(2, 3)
    8
    '''
    return d**p

def cubeIt(a, b):
    '''
    Return the cube of all numbers from a to b
    >>> cubeIt(1,3)
    [1, 8, 27]
    >>> cubeIt(1, 10) # doctest:+ELLIPSIS
    [1, 8, ..., 1000]
    '''
    answers = []
    for i in range(a, b+1):
        answers.append(i*i*i)
    return answers
    
if __name__ == '__main__':
    doctest.testmod(verbose=True)