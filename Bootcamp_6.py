import requests
from pprint import pprint


r = requests.get('https://jsonplaceholder.typicode.com/posts/101')
data = r.json()
pprint(data)

post = {
    'body' : 'lorem ipsum',
    'title' : 'Title',
    'userId' : 3
}
req = requests.post('https://jsonplaceholder.typicode.com/posts/', json=post)
print(req.json())

uppdate_post = post
uppdate_post['id'] = 3

req = requests.put(
    'https://jsonplaceholder.typicode.com/posts/', json=uppdate_post)
print(req.json())
