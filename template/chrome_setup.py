# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Setup configurations
PATH = "C:\Driver\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Do not close window
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
action = ActionChains(driver)
driver.get("https://google.com")
