#No changes in calling parameterise fixture during data driven from conftest.
# Only changes in CONFTEST FILE (Way of doing parameterise: return directly or by passing params

import pytest

#Single test data passing
@pytest.mark.usefixtures("loginDetails")
class TestLoginPage:
    def test_enterLoginDetails(self, loginDetails):     #parameterise test function with fixture
        print(loginDetails)
        print(loginDetails[2])      #Accessing list using index

#Multiple test data passing
@pytest.mark.usefixtures("crossBrowser_1")
class TestCrossBrowser_MultipleData:
    def test_crossBrowserTest(self, crossBrowser_1):
        print(crossBrowser_1)

##Multiple test data passing with multiple tuple
@pytest.mark.usefixtures("crossBrowser_2")
class TestCrossBrowser_MultipleTuple:
    def test_crossBrowserTest_MutipleTuple(self, crossBrowser_2):
        print(crossBrowser_2[1])

