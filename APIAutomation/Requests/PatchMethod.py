import requests

try:
    # Only updating specific field
    data = {
        "name": "Michael"
    }

    url = "https://videogamedb.uk/api/v2/videogame/1"

    # Send PATCH request
    response = requests.patch(url, json=data)

    print(response)

    if response.status_code == 200:
        print("Status code is 200 - Resource patched successfully")
        print(response.json())

    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
