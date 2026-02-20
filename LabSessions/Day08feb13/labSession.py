import requests
import response

try:
    #make a get request to a api endpoint
    respponse = requests.get("https://api.restful-api.dev/objects")
    print(response)
    #check if type status code is 200k
    if response.status_code == 200:
        print("Status code is 200 k")
        #parse the json file
        data = response.json()
        print(data)
    else: print(f"Error: Received status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")