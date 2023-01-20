# Search for content in Geeks for Geeks

# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# Setup configurations
service = Service(log_path='nul')
driver = webdriver.Firefox(service=service)
driver.get("https://www.geeksforgeeks.org/")
action = ActionChains(driver)

# Locate elements
search_location = "//div[@class='ant-col']/div[@class='ant-row ant-row-center gfg_home_page_search_input']/span/span/"
search_input = driver.find_element(
    By.XPATH, search_location + "span[@class='ant-input-affix-wrapper ant-input-affix-wrapper-lg']/input")
search_button = driver.find_element(
    By.XPATH, search_location + "span[@class='ant-input-group-addon']/button")

# Perform action -> Search in Geeks for Geeks
query = "Ansible"
search_input.send_keys(query)
action.click(on_element=search_button)
action.perform()
