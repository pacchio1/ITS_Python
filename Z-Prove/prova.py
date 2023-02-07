from selenium import webdriver
from selenium.webdriver.common.by import By
import time
print(dir(webdriver))
# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://www.w3schools.com/')
# Select the id box
element = driver.find_element(By.ID,"search2")
element.send_keys("array")
#element = driver.find_element(By.ID, "lname")
#element.send_keys("ciao")

time.sleep(3)
submit_assignment = driver.find_element(By.ID,'learntocode_searchbtn')
submit_assignment.click()

time.sleep(10)
