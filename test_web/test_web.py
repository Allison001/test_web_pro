import time
from selenium import webdriver


class TestWeb():

    def test_web(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        time.sleep(5)
        self.driver.implicitly_wait(4)
        self.driver.quit()