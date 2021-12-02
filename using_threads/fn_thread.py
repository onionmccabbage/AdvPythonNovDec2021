# we can run threads concurrently - at the same time
# there is always a main thread, which can spawn additional threads
# additional threads then (re)join the main thread when done

from threading import Thread # this is a thread access object
import time
import random
import sys

# here is a thread-runnable function
def myFunc(name):
    # do some long-tail operation (take a non-trivial time)
    for i in range(1,50):
        time.sleep(random.random()*0.1) # 0.1, 0.2, 0.3 etc
        sys.stdout.write( '{}\n'.format(name) ) # or just use print()

if __name__ == '__main__':
    # NB all threads run consecutively and independently
    thr1= Thread( target=myFunc, args=('thread1',) ) # args must be a tuple
    thr2= Thread( target=myFunc, args=('thread2',) ) 
    thr3= Thread( target=myFunc, args=('thread3',) ) 
    thr4= Thread( target=myFunc, args=('thread4',) ) 
    # we need to start our threads
    thr1.start()
    thr2.start()
    thr3.start()
    thr4.start()
    # we need to (re)join to the main thread
    thr1.join()
    thr2.join()
    thr3.join()
    thr4.join()