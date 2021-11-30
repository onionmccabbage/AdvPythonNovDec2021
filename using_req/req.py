# making use of the requests library
import requests # may need to 'pip install request'

def getInfo():
    url = 'https://jsonplaceholder.typicode.com/todos' # this API always returns JSON
    try:
        response = requests.get(url)
        data = response.json() # this returns 200 data members (0-199)
        # print(data)
        print(data[0]['title']) # just read member zero title
    except Exception as err:
        print('Oops {}'.format(err))
    finally:
        pass

if __name__ == '__main__':
    getInfo()