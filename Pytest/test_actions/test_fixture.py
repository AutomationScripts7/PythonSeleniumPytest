#@ - annotations
#What actually fixtures do: SETUP (Initial steps - launching browser) > YIELD (separating setup and teardown) > TEARDOWN (Final steps - closing browser)
#Fixture : A fixture is a reusable function in Pytest used to perform setup before a test and cleanup (tear down) after a test
#Teardown : Tear down is the cleanup process executed after a test completes, such as closing the browser or releasing resources
import pytest

##------------------------------------------------------------------------

import pytest
def test_login(launch):         #here parameterize the "launch" to perform fixture
   print("login successful")

##------------------------------------------------------------------------


#Fixture using class
@pytest.mark.usefixtures("launch")      #Here we are "pytest.mark.usefixtures" to parameter the conftest action
class TestLaunchURL:
    def test_login(self):
        print("login successful")

    def test_login2(self):
        print("login2 successful")

    def test_login3(self):
        print("login3 successful")

    def test_login4(self):
        print("login4 successful")


##------------------------------------------------------------------------
