from Pages.Base import BasePage
from selenium.webdriver.common.by import By


class CanvasPage(BasePage):

    CanvasURL = "http://15.165.232.220:3000/map/155"

    toolRect = (By.CSS_SELECTOR, "#app > div > div.app-gnb > div.-gnb.-menu > div.-devide.-tools > div:nth-child(3) > button")

    canvasElem = (By.ID, "frame")
    teCanv = (By.ID, "gridLayer_1")

    def __init__(self, driver):
        super(CanvasPage, self).__init__(driver)

    def get_Url(self):
        # management URL 입력
        self.get(self.CanvasURL)

    def click_Rect(self):
        self.click(self.toolRect)

    def draw_Rect(self):
        # self.click(self.canvasElem)
        self.MousePosition(self.canvasElem, self.teCanv)
