#pytest.fixture             - Create new fixture
#pytest.mark.usefixtures    - using fixture
import time

#SCOPE OF FIXTURE
#"function" (default) — runs before/after each test
#"class" — runs once per class
#"module" — runs once per file
#"session" — runs once for the entire test session

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#------------------------------------------------------------------------


#Simply passing fixture to method and testcases
@pytest.fixture(scope="function")      #if we give "scope = class" , it will execute only once in starting and ending of class, not for every testcases
def launch():
    print("running once before every method")
    yield
    print("running once after every method")


#------------------------------------------------------------------------

#No changes in calling parameterise fixture during data driven from conftest.
# Only changes in CONFTEST FILE (Way of doing parameterise: 1. return directly, 2. using params & request keyword instand)

#Single LoadData using fixture  (Single time only execute, if we want to multiple test go with params)
@pytest.fixture(scope="class")
def loginDetails(request):
    print("loading login data")
    return ["Chrome", "Edge", "IE"]       #loginDetails does NOT run multiple times because it uses return with a list, not params

#conftest.py - Centralise the reusable codes


#Multiple data parameterise
@pytest.fixture(params=["Chrome", "Edge", "IE"])
def crossBrowser_1(request):      #request is type of instance for fixture
    return request.param        #it will iterate every value into param

##------------------------------------------------------------------------

#Another example for Multiple data parameterise if 2 or 3 sets - ((params=[("Chrome", "Edge", "IE"), ("Chrome", "Edge", "IE")])
#def test_launchURL(self, crossBrowser_2, login_data):
    #browser = crossBrowser_2[0]  # "Chrome", "Edge", or "IE"
    # tool = crossBrowser_2[1]
    # if browser == "Chrome":
        #driver = webdriver.Chrome()

@pytest.fixture(params=[("Chrome", "Edge", "IE"), ("Chrome", "Edge", "IE")])
def crossBrowser_2(request):      #request is type of instance for fixture
    return request.param        #it will iterate every value into param
##------------------------------------------------------------------------

#practice parameterise using multiple data
@pytest.fixture(params=["BMW", "Audi"])
def searchitem(request):
    return request.param

#parameterise the data
@pytest.fixture(params=[ {"username": "admin", "password": "admin123"},
   {"username": "test1", "password": "test123"} ])

def login_data(request):
   return request.param

##------------------------------------------------------------------------

#This creating browser instance
@pytest.fixture(scope="class")
def launchBrowser():
    # service_Object = Service()
    # driver = webdriver.Chrome(service=service_Object)
    driver = webdriver.Edge()
    url = "https://rahulshettyacademy.com/seleniumPractise/#/"
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    yield driver    #If you don't return/yield the driver after yield, the test method won't receive the driver object in pageaction while calling
                    #if you don't give driver after yield, drivers won't be active in pageactions
    driver.close()

##------------------------------------------------------------------------

#NOTE:
#Command line options - We can give commands itself like (pytest -k <filename> __browser_name Chrome)
#SO we can run using command line options to decide the browsers (chrome,Edge,IE), if declare in browser instance conftest
#For command line options for multiple browser, we need to use (request) default fixture and use (config.getoption)
#Then use (pytest_addoption) get from pytest documentation and configure as below. Later we can use multiple web browser based command option

##------------------------------------------------------------------------

#took from pytest documentation which is useful for configure command line options
def pytest_addoption(parser):           #pytest_addoption - is built in keyword in pytest
    parser.addoption(
        "--browser_name",                  #command line option name
        action="store",                    #keyword
        default="Edge",                  #default browser
        help="metadata(data about data): browser selection"
    )

#Creating one more method for command line option to enable user launch from all browser based on command line options
@pytest.fixture(scope="function")
def launchBrower_CommandLineOption(request):                       #request - is default fixture for all fixtures in build in pytest to enable (getoption)
    browser_name = request.config.getoption("--browser_name")      #getoption - is keywords for making option for browser
                                                                   #once these steps are done, we have to register using pytest_addoption,(added above)
                                                                   # which is available in pytest documentation

    #Launching various browser with help of command lines
    service_Object = Service()
    if browser_name == "Chrome":
        driver = webdriver.Chrome(service=service_Object)
    elif browser_name == "Edge":
        driver = webdriver.Edge(service=service_Object)
    elif browser_name == "Firefox":
        driver = webdriver.Firefox(service=service_Object)

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.close()

##------------------------------------------------------------------------
