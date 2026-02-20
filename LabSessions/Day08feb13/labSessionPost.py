import requests
import response

try:

    data ={
    "id": "ff8081819c5368bb019c554adfaf0305",
    "name": "Apple MacBook Pro 16",
    "createdAt": 1770957496239,
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}
    #make a get request to a api endpoint
    response = requests.post("https://api.restful-api.dev/objects", json = data)
    print(response)
    #check if type status code is 200k
    if response.status_code == 200:
        print("Status code is 200 k")
        #parse the json file
        data = response.json()
        print(data)
    else: print(f"Error: Received status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")