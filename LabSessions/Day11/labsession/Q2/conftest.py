import pytest
import requests

@pytest.fixture
def test_user():
    print("\nCreating Test User")

    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json={"name": "Test User", "email": "test@example.com"}
    )

    user_id = response.json().get("id", 101)

    yield user_id

    print("\nDeleting Test User")

    requests.delete(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )
