import requests # CAREFUL - may need to 'pip install requests'
# we can use the requests library to access API end-points
# we can make a generator that will access members of an API endpoint
def users():
    id = 1
    while id < 10:
        r = requests.get('http://jsonplaceholder.typicode.com/users/{}'.format(id))
        yield r.text # each time we iterate over this generator, a request will be made
        id += 1

if __name__ == '__main__':
    u = users()
    # for user in u:
    #     print(user)
    print(u.__next__())
    print(u.__next__())
    print(u.__next__())