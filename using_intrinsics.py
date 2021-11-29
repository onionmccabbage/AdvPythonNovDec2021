# there are many things built in to Python
# many of them are instrinsic to python

class TopLevel(object):
    def __init__(self):
        pass

class Derived(TopLevel): # modern approach is to use ONE base class
    '''
    this class is derived fromn tge TopLevel class
    It has its own __str__ method
    '''
    def __init__(self):
        super().__init__() # call teh init mehtod of the parent class
    def __str__(self):
        return 'Derived Class instance'

if __name__ == '__main__':
    t = TopLevel()
    d = Derived()
    print(d)
    # we can explore the instrinsic members of our instances
    print('class name is {}'.format(Derived.__name__))
    print('class docstring is {}'.format(Derived.__doc__))
    print('class dictionary is {}'.format(Derived.__dict__))
    print('class bases are {}'.format(Derived.__bases__))