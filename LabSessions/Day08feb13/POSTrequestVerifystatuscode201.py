import requests

payload = {
    "title": "API Testing",
    "body": "Learning requests library",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload
)

assert response.status_code == 201
print("Resource created successfully:", response.json())
