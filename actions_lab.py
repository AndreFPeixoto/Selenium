# Imports
from selenium import webdriver
from actions_class import ActionsLab
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# Setup configurations
service = Service(log_path='nul')  # No logs
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)

lab = ActionsLab(driver=driver, action=action)
# lab.test_clicks()
# lab.test_click_and_hold()
# lab.test_context_click()
# lab.test_double_click()
# lab.test_drag_and_drop()
# lab.test_key_down()
lab.test_send_keys()