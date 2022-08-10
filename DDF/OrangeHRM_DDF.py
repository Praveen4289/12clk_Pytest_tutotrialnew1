from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from DDF import Excel_Utils

s=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=s)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(30)
path="C:\\Users\\pc\\Desktop\\DDF.xlsx"
sheet_Name="Sheet3"
rows=Excel_Utils.row_Count(path,sheet_Name)
for i in range(2,rows+1):
   username=Excel_Utils.read_Excel(path,sheet_Name,i,1)
   password=Excel_Utils.read_Excel(path,sheet_Name,i,2)
   driver.find_element(By.ID,"txtUsername").send_keys(username)
   driver.find_element(By.ID,"txtPassword").send_keys(password)
   driver.find_element(By.ID,"btnLogin").click()
   homePage_title=driver.title
   if homePage_title=="OrangeHRM":
      Excel_Utils.write_Excel(path,sheet_Name,i,3,"pass")
   else:
      Excel_Utils.write_Excel(path,sheet_Name,i,3,"fail")

   driver.find_element(By.ID,"welcome").click()
   driver.find_element(By.XPATH, "//a[text()='Logout']").click()