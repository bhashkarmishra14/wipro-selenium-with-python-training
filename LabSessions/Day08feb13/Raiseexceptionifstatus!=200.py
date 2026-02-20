import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code != 200:
    raise Exception(f"Request failed with status {response.status_code}")

print("Success")

