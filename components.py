from selenium.webdriver.common.by import By # Для find element
from selenium.common.exceptions import NoSuchElementException



class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        # self.driver.find_element(By.CSS_SELECTOR, self.locator).click()
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True


    def get_text(self):
        return str(self.find_element().text)
