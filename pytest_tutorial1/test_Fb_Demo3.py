import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager

driver=None
@pytest.fixture(scope='module')
def init_chrome_browser():
    global driver
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()

@pytest.fixture(scope='module')
def init_firefox_browser():
    global driver
    s = Service(executable_path='D:\\SeleniumDrivers\\gecko31\\geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()

@pytest.fixture(scope='module')
def init_ie_browser():
    global driver
    s = Service(IEDriverManager().install())
    driver = webdriver.Ie(service=s)
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()


def test_verifyTitle(init_firefox_browser):
    actual_title=driver.title
    assert actual_title=="Facebook – log in or sign up"


def test_verifyUrl(init_firefox_browser):
    actual_url=driver.current_url
    assert  actual_url=="https://www.facebook.com/"


def test_userNametxtbx_isEnable(init_firefox_browser):
    flag=driver.find_element(By.ID,"email").is_enabled()
    assert flag==True


def test_Passwordtxtbx_isEnable(init_firefox_browser):
    flag=driver.find_element(By.ID,"pass").is_enabled()
    assert flag==True


def test_Loginbtn(init_firefox_browser):
    actual_text=driver.find_element(By.NAME,"login").text
    assert actual_text=="Log In"



