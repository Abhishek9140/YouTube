from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#If you want Firefox, then use this line
driver = webdriver.Firefox()

#If you want Chrome, then use this line
driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/login")
driver.find_element_by_id("username").send_keys("YOUR-EMAIL-ID")
driver.find_element_by_id("password").send_keys("YOUR-PASSWORD")
driver.find_element_by_id("username").send_keys(Keys.ENTER)
