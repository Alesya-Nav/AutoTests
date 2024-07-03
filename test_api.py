import requests
response= requests.get('https://jsonplaceholder.typicode.com/posts').json()
print(response)
def test_posts():
    assert len(response)==100