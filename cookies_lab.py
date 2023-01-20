# Imports
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# Setup configurations
service = Service(log_path='nul')  # No logs
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)
driver.get("http://the-internet.herokuapp.com/")

driver.add_cookie({"name": "foo", "value": "bar"})
driver.get_cookie("foo")
print(driver.get_cookies())
driver.delete_cookie("foo")
driver.delete_all_cookies()
