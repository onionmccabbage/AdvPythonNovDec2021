# here we explore some other features built in to Python


# exploring 'zip'
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
fruits = ['banana', 'orange', 'kiwi', 'durian']
drink = ('coffee', 'tea', 'water', 'milk')
after = ['tiramasu', 'ice cream', 'pie', 'creme caramel']

# zip lets us combine data sets together - nothing to do with compression
j = zip(days, fruits, drink, after) # zip stops when the shortest collection runs out of members
# iterate over our zipped collection
for d, f, dr, a in j:
    print('On {} I ate {} with {} then {}'.format(d, f, dr, a))

# exploring deque
# deque is a double-ended queue
from collections import deque
def pal(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print( pal('tenet') ) # True
print( pal('racecar') ) # True
print( pal('halibut') ) # Fasle
print( pal('madam im adam') ) # False

