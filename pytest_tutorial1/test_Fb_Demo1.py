import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=None
def setup(module):
    global driver
    s=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=s)
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)

def teardown(module):
    driver.close()



def test_verifyTitle():
    actual_title=driver.title
    assert actual_title=="Facebook – log in or sign up"

def test_verifyUrl():
    actual_url=driver.current_url
    assert  actual_url=="https://www.facebook.com/"

def test_userNametxtbx_isEnable():
    flag=driver.find_element(By.ID,"email").is_enabled()
    assert flag==True

def test_Passwordtxtbx_isEnable():
    flag=driver.find_element(By.ID,"pass").is_enabled()
    assert flag==True

def test_Loginbtn():
    actual_text=driver.find_element(By.NAME,"login").text
    assert actual_text=="Log In"


