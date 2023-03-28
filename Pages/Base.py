from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        """ URL 이동 """
        self.driver.get(url)

    def currentURL(self, currentURL):
        self.driver.get(currentURL)

    def clear(self, locator):
        """ 텍스트 삭제 """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))

    def click(self, locator):
        """ 클릭 """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))

    def find_element(self, locator):
        """ 엘리먼트 찾기 """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))
        # 로깅 추가 필요함

    def find_elements(self, locator):
        """ 엘리먼트 찾기 (배열로 리턴) """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))

    def send_keys(self, locator, value):
        """ 인풋 필드 값 입력 """
        self.find_element(locator).send_keys(value)

    def MousePosition(self, locator, secLoc):
        """마우스 클릭"""
        drag = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        drop = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(secLoc))
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    def find_Value(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).get_attribuet()
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))

    def not_Exist(self, locator):
        try:
            NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except NoSuchElementException:
            pass




