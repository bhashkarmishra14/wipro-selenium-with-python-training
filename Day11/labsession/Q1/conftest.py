import pytest
import requests

@pytest.fixture(scope="session")
def auth_token():
    print("\nGenerating Auth Token Once Per Session")

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"username": "admin", "password": "admin123"}
    )

    token = "dummy_token_123"
    return token
