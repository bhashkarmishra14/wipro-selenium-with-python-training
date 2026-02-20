import pytest

@pytest.fixture(scope="session")
def setup_session():
    print("\nSetup for session")
    yield
    print("\nTeardown for session")


@pytest.mark.usefixtures("setup_session")
def test_session1():
    print("Executing test_session1")


@pytest.mark.usefixtures("setup_session")
def test_session2():
    print("Executing test_session2")
