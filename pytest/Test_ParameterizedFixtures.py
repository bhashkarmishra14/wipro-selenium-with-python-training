import pytest
@pytest.fixture(params=("chrome","firefox"))
#request - pytest object that contains information about
#who is calling the fixture and with what data
def browser(request):
    print("Current browser:", request.param)
    return request.param
def testbrowser(browser):
    assert browser in ["chrome" , "firefox"]




























