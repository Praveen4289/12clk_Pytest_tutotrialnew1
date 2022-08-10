import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as firefoxservice
from selenium.webdriver.ie.service import Service as ieservice
from webdriver_manager.chrome import ChromeDriverManager


driver = None


@pytest.fixture(scope='module')
def init_chrome_browser():
    global driver
    s = chromeservice(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()


@pytest.fixture(scope='module')
def init_firefox_browser():
    global driver
    s = firefoxservice()
    driver = webdriver.Firefox(service=s)
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()


@pytest.fixture(scope='module')
def init_ie_browser():
    global driver
    s = ieservice()
    driver = webdriver.Ie(service=s)
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()


@pytest.mark.usefixtures("init_firefox_browser")
def test_verifyTitle():
    actual_title = driver.title
    assert actual_title == "Facebook – log in or sign up"


@pytest.mark.usefixtures("init_firefox_browser")
def test_verifyUrl():
    actual_url = driver.current_url
    assert actual_url == "https://www.facebook.com/"


@pytest.mark.usefixtures("init_firefox_browser")
def test_userNametxtbx_isEnable():
    flag = driver.find_element(By.ID, "email").is_enabled()
    assert flag == True


@pytest.mark.usefixtures("init_firefox_browser")
def test_Passwordtxtbx_isEnable():
    flag = driver.find_element(By.ID, "pass").is_enabled()
    assert flag == True


@pytest.mark.usefixtures("init_firefox_browser")
def test_Loginbtn():
    actual_text = driver.find_element(By.NAME, "login").text
    assert actual_text == "Log In"
