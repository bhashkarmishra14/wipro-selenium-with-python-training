import requests

session = requests.Session()

# First request
response1 = session.get("https://httpbin.org/cookies/set?name=Bhaskar")
print("Cookies after first request:", session.cookies.get_dict())

# Second request (same session)
response2 = session.get("https://httpbin.org/cookies")
print("Server sees cookies:", response2.json())
