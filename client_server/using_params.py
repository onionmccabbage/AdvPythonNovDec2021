import requests
import sys

# we will access an API end-point passing parameters as system argument variables
# parts of the returnend JSON will be displayed nicely

def getInfo(category='todos', id=1): # we can provide sensible defaults
    url = 'https://jsonplaceholder.typicode.com/'
    # append a category and an ID to this url
    api = '{}{}/{}'.format(url, category, id) # this is a REST api
    try:
        response = requests.get(api)
        data = response.json() # we just want hte JSON part of the response
    except Exception as err:
        print('Problem: {}'.format(err))
    finally:
        pass
    print(data)

if __name__ == '__main__':
    getInfo('users', 7)