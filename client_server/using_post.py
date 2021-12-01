import requests

# to amke a POST request we pass a payload of data
def makePost():
    url = 'https://httpbin.org/post' # an echo API end point service
    payload = {'item':'Ocelot', 'status':'admin'}
    try:
        res = requests.post(url, data=payload)
        # dd we receive anything back?
        print(res.text) # we just want the text part of the response
    except Exception as err:
        print(err)

if __name__ == '__main__':
    makePost()