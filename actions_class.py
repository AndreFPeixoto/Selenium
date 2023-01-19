from selenium.webdriver.common.by import By

class ActionsLab:
    url = "http://the-internet.herokuapp.com"

    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    def test_clicks(self):
        self.driver.get(ActionsLab.url + "/add_remove_elements/")
        add_element_button = self.driver.find_element(By.TAG_NAME, "button")
        for i in range(5):
            self.action.click(on_element=add_element_button)
        self.action.perform()

    def test_click_and_hold(self):
        self.driver.get(ActionsLab.url + "/shifting_content/menu")
        contact_us_item = self.driver.find_element(By.LINK_TEXT, "Contact Us")
        self.action.click_and_hold(on_element=contact_us_item)
        self.action.perform()

    def test_context_click(self):
        self.driver.get(ActionsLab.url + "/context_menu")
        context_div = self.driver.find_element(By.ID, "hot-spot")
        self.action.context_click(on_element=context_div)
        self.action.perform()

    def test_double_click(self):
        self.driver.get(ActionsLab.url + "/tables")
        element = self.driver.find_element(By.XPATH, "//div[@class='example']/h3[1]")
        self.action.double_click(on_element=element)
        self.action.perform()

    def test_drag_and_drop(self):
        self.driver.get(ActionsLab.url + "/drag_and_drop")
        source_element = self.driver.find_element(By.ID, "column-a")
        dest_element = self.driver.find_element(By.ID, "column-b")
        self.action.drag_and_drop(source_element, dest_element)
        self.action.perform()