# abc is the abstract base class
from abc import ABCMeta, abstractmethod, abstractproperty

# we can declare an abstract base (top-level) class
class Shape():
    __metaclass__ = ABCMeta
    @abstractmethod
    def display(self):
        pass # we provide no body of the method
    # @abstractproperty # deprecated
    # def name(self):
    #     pass # no body
    @property 
    @abstractmethod
    def name(self):
        pass # no body