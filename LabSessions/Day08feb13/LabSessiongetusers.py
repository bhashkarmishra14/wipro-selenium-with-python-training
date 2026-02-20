import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
response.raise_for_status()

users = response.json()

for user in users:
    print(f"Name: {user['name']}, Email: {user['email']}")
