import requests

try:
    url = "https://videogamedb.uk/api/v2/videogame"

    response = requests.get(url, timeout=5)

    # Check status code
    if response.status_code == 200:
        print("Status code is 200")

        # JSON response
        data = response.json()
        print("JSON Data:")
        print(data)

        # Text response
        print("\nResponse Text:")
        print(response.text)

        # Binary content
        print("\nResponse Content:")
        print(response.content)

        # Status code
        print("\nStatus Code:")
        print(response.status_code)

        # Headers
        print("\nHeaders:")
        print(response.headers)

        # Redirect history
        print("\nHistory:")
        print(response.history)

        # Final URL
        print("\nURL:")
        print(response.url)

        # Fetch single header
        content_type = response.headers.get("Content-Type")
        print("\nContent-Type Header:")
        print(content_type)

    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
