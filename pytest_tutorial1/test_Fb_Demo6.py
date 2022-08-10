import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as edgeservice
from selenium.webdriver.firefox.service import Service as firefoxservice


@pytest.fixture(scope='class')
def init_chrome_browser(request):
    s=chromeservice()
    chrome_driver=webdriver.Chrome(service=s)
    request.cls.driver=chrome_driver
    yield
    chrome_driver.close()

@pytest.fixture(scope='class')
def init_firefox_browser(request):
    s=firefoxservice(executable_path="E:\SoftwareTesting\Pycharm Projects\Python_Tutorial_Basics\Drivers\geckodriver.exe")
    firefox_driver=webdriver.Firefox(service=s)
    request.cls.driver=firefox_driver
    yield
    firefox_driver.close()

@pytest.fixture(scope='class')
def init_edge_browser(request):
    s=edgeservice()
    edgedriver_driver=webdriver.Edge(service=s)
    request.cls.driver=edgedriver_driver
    yield
    edgedriver_driver.close()

@pytest.mark.usefixtures("init_chrome_browser")
class Test_browser:
    pass
class Test_Fb(Test_browser):

    def test_verifyTitle(self):
        self.driver.get("https://www.fb.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        actual_title = self.driver.title
        assert actual_title == "Facebook – log in or sign up"


    def test_verifyUrl(self):
        actual_url = self.driver.current_url
        assert actual_url == "https://www.facebook.com/"


    def test_userNametxtbx_isEnable(self):
        flag = self.driver.find_element(By.ID, "email").is_enabled()
        assert flag == True


    def test_Passwordtxtbx_isEnable(self):
        flag = self.driver.find_element(By.ID, "pass").is_enabled()
        assert flag == True


    def test_Loginbtn(self):
        actual_text = self.driver.find_element(By.NAME, "login").text
        assert actual_text == "Log In"

