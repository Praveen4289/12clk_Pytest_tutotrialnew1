import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as edgeservice
from selenium.webdriver.firefox.service import Service as firefoxservice


@pytest.fixture(params=['chrome','firefox','edge'],scope='class')
def init_browser(request):
    if request.param == 'chrome':
        s=chromeservice()
        driver=webdriver.Chrome(service=s)
    if request.param == 'firefox':
        s=firefoxservice(executable_path="E:\SoftwareTesting\Pycharm Projects\Python_Tutorial_Basics\Drivers\geckodriver.exe")
        driver=webdriver.Firefox(service=s)
    if request.param == 'edge':
        s=edgeservice()
        driver=webdriver.Edge(service=s)
    request.cls.driver=driver
    yield
    driver.close()

@pytest.mark.usefixtures("init_browser")
class test_Fb_browser:
    pass
class Test_Twobrowser(test_Fb_browser):

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

