# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# Setup configurations
service = Service(log_path='nul')  # No logs
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)
driver.get("http://the-internet.herokuapp.com/javascript_alerts")

alert_button = driver.find_element(By.XPATH, "//ul/li[3]/button")
print(alert_button.text)
action.click(on_element=alert_button)
action.perform()

alert = Alert(driver)
print(alert.text)
# alert.accept()
# alert.dismiss()
alert.send_keys("Ryuma")
alert.accept()
