import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        # chrome_options.add_argument("disable-gpu")
        chrome_options.add_argument("--incognito")
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def setUp(self) -> None:
        pass

    def tearDown(self):
        # driver = self.driver
        # driver.get("http://15.165.232.220:3000/")
        pass

    def delCookie(self) -> None:
        driver = self.driver
        driver.delete_all_cookies()
        pass

    def currentURL(self):
        driver = self.driver
        variable = driver.current_url
        driver.get(variable)
        print(variable)
        return variable

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownCls was on")
        time.sleep(5)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
