from my_abstract import Shape

class Circle(Shape):
    def __init__(self, name):
        self.name = name # this calls the setter
    def display(self):
        print('Circle {}'.format(self.name))
    @property
    def name(self):
        return self.__name
    @name .setter
    def name(self, new_name):
        if type(new_name) == str and new_name !='':
            self.__name = new_name
        else:
            self.__name = 'default' # or we could raise an exception

if __name__ == '__main__': # exercise this module
    c = Circle('round')
    c.display()