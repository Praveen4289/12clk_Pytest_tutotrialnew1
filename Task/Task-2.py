from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from DDF import Excel_Utils

s = Service()
driver = webdriver.Chrome(service=s)
driver.get("https://demo.guru99.com//test//newtours//register.php")
driver.maximize_window()
driver.implicitly_wait(30)
path = "C:\\Users\\PK\Desktop\\Mercury Register Details.xlsx"
sheet_Name = "Sheet1"
rows = Excel_Utils.row_Count(path, sheet_Name)
try:
    for i in range(2, rows + 1):
        # Required Data From EXCEL
        firstname = Excel_Utils.read_Excel(path, sheet_Name, i, 1)
        lastname = Excel_Utils.read_Excel(path, sheet_Name, i, 2)
        phonenumber = Excel_Utils.read_Excel(path, sheet_Name, i, 3)
        email = Excel_Utils.read_Excel(path, sheet_Name, i, 4)
        address = Excel_Utils.read_Excel(path, sheet_Name, i, 5)
        city = Excel_Utils.read_Excel(path, sheet_Name, i, 6)
        state = Excel_Utils.read_Excel(path, sheet_Name, i, 7)
        postalcode = Excel_Utils.read_Excel(path, sheet_Name, i, 8)
        country = Excel_Utils.read_Excel(path, sheet_Name, i, 9)
        username = Excel_Utils.read_Excel(path, sheet_Name, i, 10)
        password = Excel_Utils.read_Excel(path, sheet_Name, i, 11)
        conf_pass = Excel_Utils.read_Excel(path, sheet_Name, i, 12)
        # Required Web Elements
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys(firstname)
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys(lastname)
        driver.find_element(By.XPATH, "//input[@name='phone']").send_keys(phonenumber)
        driver.find_element(By.XPATH, "//input[@id='userName']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='address1']").send_keys(address)
        driver.find_element(By.XPATH, "//input[@name='city']").send_keys(city)
        driver.find_element(By.XPATH, "//input[@name='state']").send_keys(state)
        driver.find_element(By.XPATH, "//input[@name='postalCode']").send_keys(postalcode)
        driver.find_element(By.XPATH, "//select[@name='country']").send_keys(country)
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys(conf_pass)
        driver.find_element(By.XPATH, "//input[@name='submit']").click()
        Validation1 = driver.find_element(By.XPATH, "//a[normalize-space()='SIGN-OFF']").text
        if Validation1 == "SIGN-OFF":
            Excel_Utils.write_Excel(path, sheet_Name, i, 13, "Details Submited to portal successfuly")
            driver.find_element(By.XPATH, "//a[normalize-space()='REGISTER']").click()
        else:
            Excel_Utils.write_Excel(path, sheet_Name, i, 13, "Failed to Submit Details")
except:
    pass
driver.quit()
