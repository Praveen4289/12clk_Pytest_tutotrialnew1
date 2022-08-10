from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=s)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
driver.find_element(By.ID,"welcome").click()
driver.find_element(By.XPATH,"//a[text()='Logout']").click()
