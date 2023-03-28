from Pages.Base import BasePage
from selenium.webdriver.common.by import By

class MapAreaSetting(BasePage):

    url = "http://15.165.232.220:3000/setting/176"

    none = (By.XPATH, "/html/body/div/div/div/div/section/div[2]")

    Building = (By.CSS_SELECTOR, "#app > div.v-application--wrap > section > div.select-setting-type > div > div.btn-type-map.building.active")
    BuildingSize = (By.XPATH, "/html/body/div/div/div/div/section/div[2]/div/div[1]/ul/li[2]")
    BuildingScale = (By.XPATH, "/html/body/div/div/div/div/section/div[2]/div/div[1]/ul/li[1]")

    sizeW = (By.CSS_SELECTOR, "#app > div.v-application--wrap > section > div.app-panel.app-panel-setting > section > div.-panel.-size > div > div:nth-child(2) > div > div:nth-child(1) > div > input[type=tel]")
    sizeH = (By.CSS_SELECTOR, "#app > div.v-application--wrap > section > div.app-panel.app-panel-setting > section > div.-panel.-size > div > div:nth-child(2) > div > div:nth-child(3) > div > input[type=tel]")

    scale = (By.CSS_SELECTOR, "#app > div.v-application--wrap > section > div.app-panel.app-panel-setting > section > div.-panel.-scale > div > div:nth-child(2) > div > div > input[type=tel]")

    cancelButton = (By.CSS_SELECTOR, "#app > div.v-application--wrap > section > div.app-gnb > div.-gnb.-option > button.btn-common.-mint-outlined")
    completeButton = (By.CSS_SELECTOR, "#app > div.v-application--wrap > section > div.app-gnb > div.-gnb.-option > button.btn-common.-mint")


    levelAddButton = (By.CLASS_NAME, "btn-ico-add")

    def __init__(self, driver):
        super(MapAreaSetting, self).__init__(driver)

    def get_Url(self):
        self.get(self.url)

    def click_Cancel(self):
        self.click(self.cancelButton)

    def click_SizeW(self):
        self.click(self.sizeW)

    def sendKey_SizeW(self, WTxt):
        self.send_keys(self.sizeW, WTxt)
        self.click(self.none)

    def click_SizeH(self):
        self.click(self.sizeH)

    def sendKey_SizeH(self, HTxt):
        self.send_keys(self.sizeH, HTxt)
        self.click(self.none)

    def click_Sacle(self):
        self.click(self.scale)

    def sendKey_Scale(self, scaleTxt):
        self.clear(self.scale)
        self.send_keys(self.scale, scaleTxt)
        self.click(self.none)

    def click_None(self):
        self.click(self.none)

    def click_Complete(self):
        self.click(self.completeButton)

    def click_LevelAdd(self):
        self.click(self.levelAddButton)


