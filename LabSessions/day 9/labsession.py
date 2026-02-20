import pytest
import sys
import requests


# -------------------------------------------------
# 1️⃣ Skip test (feature not implemented)
# -------------------------------------------------
@pytest.mark.skip(reason="Feature not implemented yet")
def test_feature_not_ready():
    assert True


# -------------------------------------------------
# 2️⃣ Run only on Linux (skip on Windows)
# -------------------------------------------------
@pytest.mark.skipif(sys.platform.startswith("win"),
                    reason="Runs only on Linux")
def test_linux_only():
    assert True


# -------------------------------------------------
# 3️⃣ API health check with dynamic skip
# -------------------------------------------------
def test_api_health():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code != 200:
        pytest.skip("API is not healthy. Skipping test.")

    assert response.status_code == 200


# -------------------------------------------------
# 4️⃣ Mark known failing test as xfail
# -------------------------------------------------
@pytest.mark.xfail(reason="Bug #123")
def test_known_bug():
    assert 2 + 2 == 5


# -------------------------------------------------
# 5️⃣ Parametrized test with selective xfail
# -------------------------------------------------
@pytest.mark.parametrize("num", [
    1,
    2,
    pytest.param(3, marks=pytest.mark.xfail(reason="Bug #124")),
    pytest.param(4, marks=pytest.mark.xfail(reason="Bug #125")),
    5
])
def test_numbers(num):
    assert num < 3
