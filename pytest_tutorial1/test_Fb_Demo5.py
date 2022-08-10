import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as firefoxservice


@pytest.fixture(scope='class')
def init_firefox_browser(request):
    s=firefoxservice()
    firefox_driver=webdriver.Firefox(service=s)
    request.cls.driver=firefox_driver
    yield
    firefox_driver.close()

@pytest.mark.usefixtures("init_firefox_browser")
class Test_Fb_Base():
    pass
class Test_Fb_firefox(Test_Fb_Base):

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

