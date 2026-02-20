import requests

try:
    url = "https://videogamedb.uk/api/v2/videogame/1"

    # Send DELETE request
    response = requests.delete(url)

    print(response)

    if response.status_code == 200:
        print("Status code is 200 - Resource deleted successfully")
        print(response.json())

    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
