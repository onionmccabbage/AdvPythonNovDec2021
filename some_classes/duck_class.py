# the file name has no bearing on the class name

# classes let us gather together related aspects of reality
class Duck(): # all classes ultimately descend from the python Object class
    '''
    This Duck class encapsulate a name via get/set methods
    '''
    # we can assign properties to the class (rather than to instances)
    count = 0
    def how_many(self):
        print( 'The Duck class has {} instances'.format(self.count) )   
    def __init__(self, name): # very like a constructor
        self.__name = name # property-name mangling
        Duck.count += 1 # we increment the 'count' property
    def __str__(self): # __str__ overrides the built-in print function
        return 'This duck is called {}'.format(self.__name)
    # we usually write accessor and mutator methods
    @property # this is a getter function
    def name(self):
        return self.__name
    @name.setter # this is a setter function
    def name(self, new_name):
        if type(new_name) == 'string':
            self.__name = new_name

if __name__ == '__main__': # this lets us exercise the code within this module
    h = Duck('Ada')
    h.__name='this is another arbitrary property'
    h.name = 'Howard'
    print( h.name )
    print(h) # uses the __str__ function
    # how many instances
    a = Duck('Ada')
    f = Duck('Fritha')
    print( h.how_many() )