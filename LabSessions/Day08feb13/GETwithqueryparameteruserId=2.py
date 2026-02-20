import requests

params = {"userId": 2}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

response.raise_for_status()

posts = response.json()
print("Number of posts:", len(posts))
