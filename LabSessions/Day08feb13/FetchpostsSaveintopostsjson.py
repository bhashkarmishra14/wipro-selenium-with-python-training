import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")
response.raise_for_status()

posts = response.json()

with open("posts.json", "w") as file:
    json.dump(posts, file, indent=4)

print("Saved to posts.json")
