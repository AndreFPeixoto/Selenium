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
driver.get("https://google.com")
