from selenium import webdriver
from datetime import datetime

driver = webdriver.Chrome("D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
today_dt = datetime.now().strftime("%d-%B-%Y")
print("Today date is: %s" %today_dt)

with open("D:\\output_file.csv", "a+") as opt_file:
    opt_file.write("ID, Name\n")
    for i in range(136, 1000):
        driver.get("https://URL_VALUE" + str(i))
        reg_name = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/h2').text
        print("Id: %d \t Name is: %s" %(i, reg_name))
        opt_file.write("%d, %s\n" %(i, reg_name))
    opt_file.write("\n")
