# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# Setup configurations
service = Service(log_path='nul')  # No logs
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)
driver.get("http://127.0.0.1:5500/html/selector_lab.html")

# Locate single elements
login_form = driver.find_element(By.ID, "login_form")
print(login_form.tag_name)
username_input = driver.find_element(By.NAME, "username")
print(username_input.tag_name)
login_form_xpath = driver.find_element(By.XPATH, "//form[1]")
print(login_form_xpath.tag_name)
continue_link = driver.find_element(By.LINK_TEXT, "Continue")
print(continue_link.tag_name)
continue_partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Conti")
print(continue_partial_link.text)
header = driver.find_element(By.TAG_NAME, "h1")
print(header.text)
content_class = driver.find_element(By.CLASS_NAME, "content")
print(content_class.text)
content_css_selector = driver.find_element(By.CSS_SELECTOR, "p.content")
print(content_css_selector.text)

# Locate multiple elements
password_inputs = driver.find_elements(By.NAME, "password")
print(len(password_inputs))
login_form_inputs = driver.find_elements(By.XPATH, "//form[1]/input")
print(len(login_form_inputs))
continue_links = driver.find_elements(By.LINK_TEXT, "Continue")
print(len(continue_links))
c_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "C")
print(len(c_links))
p_tags = driver.find_elements(By.TAG_NAME, "p")
print(len(p_tags))
content_classes = driver.find_elements(By.CLASS_NAME, "content")
print(len(content_classes))
content_css_selectors = driver.find_elements(By.CSS_SELECTOR, "p.content")
print(len(content_css_selectors))

driver.quit()
