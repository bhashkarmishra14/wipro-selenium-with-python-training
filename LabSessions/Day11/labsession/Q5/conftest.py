import pytest
import requests

@pytest.fixture
def base_url():
    print("\nBase URL Setup")
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def auth_token(base_url):
    print("Generating Auth Token")
    return "chain_token_123"

@pytest.fixture
def user(base_url, auth_token):
    print("Creating User using Token")

    response = requests.post(
        f"{base_url}/users",
        json={"name": "Chain User"}
    )

    user_id = response.json().get("id", 201)

    yield user_id

    print("Deleting User")
    requests.delete(f"{base_url}/users/{user_id}")
