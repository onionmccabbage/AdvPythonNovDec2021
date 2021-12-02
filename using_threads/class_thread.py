from threading import Thread # this is a thread access object
import time
import random
import sys

# define a runnable class (descends from Thread class)
class MyClass(Thread):
    def __init__(self, name):
        Thread.__init__(self) # cal the super __init__
        self.name = name
    # override the 'run' method of Thread
    def run(self):
         # this will be called every time we start a thread using this class
         for i in range(1,50):
             time.sleep(random.random()*0.1)
             print(self.name) # or sys.stdout.write()

if __name__ == '__main__':
    m1 = MyClass('class Thread 1')
    m2 = MyClass('class Thread 2')
    m3 = MyClass('class Thread 3')
    m4 = MyClass('class Thread 4')
    # start the threads
    m1.start()
    m2.start()
    m3.start()
    m4.start()
    # join them
    m1.join()
    m2.join()
    m3.join()
    m4.join()