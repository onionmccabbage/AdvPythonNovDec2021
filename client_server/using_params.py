import requests
import sys

# we will access an API end-point passing parameters as system argument variables
# parts of the returnend JSON will be displayed nicely

def getInfo(category='todos', id=1): # we can provide sensible defaults
    url = 'https://jsonplaceholder.typicode.com/'
    # append a category and an ID to this url
    api = '{}{}/{}'.format(url, category, id) # this is a REST api
    try:
        response = requests.get(api) # get lets us pass parameters on the URL
        data = response.json() # we just want hte JSON part of the response
    except Exception as err:
        print('Problem: {}'.format(err))
    finally:
        pass
    print(data)

if __name__ == '__main__':
    # we can check if any system aruments were received
    if len(sys.argv) > 1:
        category = sys.argv[1]
        id       = sys.argv[2]
    else: # NB we could ask the user here...
        category = 'albums'
        id       = 3
    getInfo(category, id)
    