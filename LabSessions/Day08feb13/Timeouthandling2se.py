import requests
from requests.exceptions import Timeout

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=2
    )
    print(response.status_code)

except Timeout:
    print("Request timed out!")
