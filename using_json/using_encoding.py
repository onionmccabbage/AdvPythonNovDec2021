# we need a set of classes that can encode our own class data type
import json

class Item:
    '''
    This class encapsulate items that have a name (str) and a cost (float)
    '''
    def __init__(self, name, cost):
        self.name = name # this will call the setter method
        self.cost = cost
    def __str__(self):
        return 'Name: {0} Cost: {1:0.2f}'.format(self.name, self.cost)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        # we should validate
        self.__name = new_name
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, new_cost):
        # we should validate
        self.__cost = new_cost

class ItemEncoder(json.JSONEncoder): # we inherit from JSONEncoder to help encode our own classes
    def default(self, obj): # override the built-in default encoding
        # check if the obj is our 'Item' class
        if isinstance(obj, Item):
            return obj.__dict__ # return our object as a dict
        else:
            # if the type is NOT an Item, just use the default encoding
            return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    # can we json encode our class?
    z = Item('Zoetrope', 28)
    z_j = json.dumps(z, cls=ItemEncoder) # make use of our encoder class
    print(z_j)