import pytest

@pytest.fixture(scope="module")
def setup_module():
    print("\nSetup for module")
    yield
    print("\nTeardown for module")


@pytest.mark.usefixtures("setup_module")
def test_sample1():
    print("Executing test_sample1")


@pytest.mark.usefixtures("setup_module")
def test_sample2():
    print("Executing test_sample2")
