import requests

def test_json_schema():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    data = response.json()

    expected_keys = {"id", "name", "username", "email"}

    assert response.status_code == 200
    assert expected_keys.issubset(data.keys())
