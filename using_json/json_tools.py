# json is JavaScript Object Notation - it is TEXT
import json
import datetime

# here is a rather complex data structure
a = [{'name':'PC', 'cost':500, 'detail':{'a':'True', 'b':[1,2,3,4]}},{'name':'Screen','cost':250, 'detail':{'a':'False', 'b':[9,8,7,6]}}]
# it could be any data structure, and we may need to pass it between services
a_j = json.dumps(a) #take the structure and render it as plain text (json)
print(type(a), type(a_j))
# we can convert json back to a Python structure
b = json.loads(a_j)
print(type(b), b)

# not everything can be serialised straight into JSON
now = datetime.datetime.utcnow() # universal time convention - constistent across computing
# now_j = json.dumps(now) # datetime is not serializable
# NB we could just make hte dt into a string then serialize it

# when JSON fails, use pickle
import pickle
p = pickle.dumps(now)
p_j = json.dumps(str(p)) # not really needed
print(now, type(now), p, type(p))
# return the pickled items to Python structures
n = pickle.loads(p)
print(n, type(n))