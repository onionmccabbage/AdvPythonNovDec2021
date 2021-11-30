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