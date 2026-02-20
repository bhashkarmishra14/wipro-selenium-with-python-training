import requests
from requests.auth import HTTPBasicAuth

try:
    headers = {
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    }

    # Make GET request
    response = requests.get(
        "https://videogamedb.uk/api/v2/videogame",
        auth=HTTPBasicAuth('username', 'password'),
        timeout=5,
        headers=headers
    )

    print(response)

    if response.status_code == 200:
        print("Status code is 200")
        data = response.json()
        print(data)
    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
