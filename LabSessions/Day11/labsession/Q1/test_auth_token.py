def test_api_1(auth_token):
    print("Using token in test_api_1:", auth_token)
    assert auth_token == "dummy_token_123"

def test_api_2(auth_token):
    print("Using token in test_api_2:", auth_token)
    assert auth_token == "dummy_token_123"
