#Filename and Method name starts with test_ or end with _test
#Any CODE should be wrapped in METHOD only, we cannot write any code without method
#If you want to write same method name another times, it will OVERRIDE the first method and execute last one
#Methodname should be in sense

#COMMAND TO RUN THE TESTCASES:
#-v     >   VERBUS ( to get detailed output)
#-s     >   PRINT OUTPUT ( to print statement)
#-k     >   EXECUTE FILES WHICH IS HAVE SAME NAME (Example: login - it will all files with login name)
#-m     >   MARK (Execute marked testcases)
#-lf    >   RUN LAST FAILED TEST
#-X     >   STOP ON FIRST FAILURE

#pytest Pytest/test_actions/test_mark.py::test_cases           >   we can run separate method like this or by below command
#pytest -k test_cases2 -v -s                            >   Another way to run separate method

#MARKER:
#pytest.mark.smoke      >smoke
#pytest.mark.regression >regression
#pytest.mark.skip       >skip testcases
#pytest.mark.xfail      >it will fail but not reporting because xfail steps are required to complete the test
#Xfail Example: Even RFO is invalid, script will run until reach to success
#pytest.mark.skipif	    >Example: Skip login tests if Python version < 3.9 or if running on Windows

import pytest
def test_cases1():
    a = 6
    b = 10
    assert a+4 == b , "not matched"

@pytest.mark.smoke
@pytest.mark.skip
def test_cases2():
    print("I am demo2")

@pytest.mark.xfail
def test_xfail():
    print("I am xfail")

@pytest.mark.regression
def test_cases3():
    print("Hello")

