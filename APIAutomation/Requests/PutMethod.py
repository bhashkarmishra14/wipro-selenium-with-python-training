import requests

try:

    data = {
        "category": "Platform",
        "name": "John",
        "rating": "Mature",
        "releaseDate": "2012-05-04",
        "reviewScore": 85
    }

    # Make PUT request
    response = requests.put(
        "https://videogamedb.uk/api/v2/videogame/1",
        json=data
    )

    print(response)

    if response.status_code == 200:
        print("Status code is 200 - Resource updated successfully")
        print(response.json())
    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
