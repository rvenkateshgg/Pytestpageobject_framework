import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Config.config import TestData
s = Service(executable_path=TestData.CHROME_EXECUTABLEPATH)


@pytest.fixture()
def init_driver(request):
    web_driver = webdriver.Chrome(service=s)
    request.cls.driver = web_driver
    yield
    web_driver.close()
