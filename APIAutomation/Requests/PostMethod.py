import requests

try:
    data = {
        "category": "Platform",
        "name": "Mario",
        "rating": "Mature",
        "releaseDate": "2012-05-04",
        "reviewScore": 85
    }

    # Make POST request
    response = requests.post(
        "https://videogamedb.uk/api/v2/videogame",
        json=data
    )

    print(response)

    # Check if status code is 201 (Created)
    if response.status_code == 201:
        print("Status code is 201 - Resource created successfully")

        # Parse JSON
        response_data = response.json()
        print(response_data)
    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
