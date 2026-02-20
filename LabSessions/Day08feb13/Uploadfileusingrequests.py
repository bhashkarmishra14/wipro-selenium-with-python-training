import requests

files = {
    "file": open("test.txt", "rb")
}

response = requests.post(
    "https://httpbin.org/post",
    files=files
)

print(response.json())
