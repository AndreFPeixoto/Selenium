# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# Setup configurations
service = Service(log_path='nul')  # No logs
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)
driver.get("http://the-internet.herokuapp.com/")

print(driver.current_url)

driver.get("http://the-internet.herokuapp.com/abtest")
print(driver.current_url)

driver.back() # Sometimes does not work
#driver.execute_script("window.history.go(-1)")
driver.forward()