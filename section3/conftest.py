from pytest import fixture
from selenium import webdriver

@fixture(scope="session")
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser
    #teardown
    #code that executes before the yield returns some data
    print("I am tearing down this browser")

@fixture(scope="function")
def get_configuration():
    
    config = [
        3006,
        "database",
        "mysql"
    ]