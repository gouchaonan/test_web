
import pytest
from selenium.webdriver.common.by import By
import time
from test_web_001.test_001.test_ren.test_base_001 import Base001
from test_web_001.test_001.test_ren.test_login import TestLogin001

class AddHuaTi():
    def test_add_huati(self):
        # self.driver.find_element(By.ID, "create-topic").click()
        self.driver.find_element(By.ID, "create-topic").click()
        self.driver.find_element(By.ID, "reply-title").send_keys("pytest 下拉框测试来了")
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".select-kit-header-wrapper").click()
        self.driver.find_element(By.ID, "ember500-filter").send_keys('提问')
        self.driver.find_element(By.ID, "ember787").click()
        self.driver.find_element(By.CSS_SELECTOR, ".uploadbtnno-textbtn-icon").send_keys(
            '/Users/gouchaonan/Desktop/test_1.png')
        self.driver.find_element(By.ID, "ember364").send_keys("元素定位太难了")
        self.driver.find_element(By.CSS_SELECTOR, ".d-button-label").click()

if __name__ == "__main__":
    add_test=AddHuaTi()
    add_test.add_huati()
