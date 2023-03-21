import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class Base001:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # 最大化浏览器
        self.driver.implicitly_wait(3)
        vars = {}

    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main()