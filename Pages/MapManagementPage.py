from Pages.Base import BasePage
from selenium.webdriver.common.by import By


class MapMangamentPage(BasePage):

    main_url = "http://15.165.232.220:3000/"

    mapList = (By.CSS_SELECTOR, "#app > div.v-application--wrap > section > ul")

    MapManifestPopup = (By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]")

    manifestOpen = (By.CSS_SELECTOR, "#app > div > section > button")

    Xbtn = (By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > div.popup-content > div.top > button")

    mapUseList = (By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > div.popup-content > div.content > div:nth-child(1) > div > div:nth-child(1) > div.input.col > div")
    mapUseDraft = (By.XPATH, "/html/body/div/div/div/div[4]/div/div[1]")
    mapUsePublish = (By.XPATH, "/html/body/div/div/div/div[4]/div/div[2]")
    mapUseArchive = (By.XPATH, "/html/body/div/div/div/div[4]/div/div[3]")

    titleInput = (By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/input")

    mainLanguage = (By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[1]")

    mainKor = (By.XPATH, "/html/body/div/div/div/div[4]/div/div[1]")
    mainEng = (By.XPATH, "/html/body/div/div/div/div[4]/div/div[2]")
    mainSpn = (By.XPATH, "/html/body/div/div/div/div[4]/div/div[3]")
    mainJpn = (By.XPATH, "/html/body/div/div/div/div[4]/div/div[4]")

    subKor = (By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > div.popup-content > div.content > div:nth-child(2) > div > div:nth-child(2) > div.input.col > section > div:nth-child(3) > div > div > div.v-input__slot > div > i")
    subEng = (By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > div.popup-content > div.content > div:nth-child(2) > div > div:nth-child(2) > div.input.col > section > div:nth-child(4) > div > div > div.v-input__slot > div > i")
    subSpn = (By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > div.popup-content > div.content > div:nth-child(2) > div > div:nth-child(2) > div.input.col > section > div:nth-child(5) > div > div > div.v-input__slot > div > i")
    subJpn = (By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > div.popup-content > div.content > div:nth-child(2) > div > div:nth-child(2) > div.input.col > section > div:nth-child(6) > div > div > div.v-input__slot > div > i")

    legalNoticeButton = (By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > div.popup-content > div.content > div:nth-child(2) > div > div:nth-child(3) > div.input.col > div > div")

    legalNoticeInput = (By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/textarea")

    completeBtn = (By.XPATH, "/html/body/div/div/div/div[3]/div/div[2]/button[2]")
    cancelBtn = (By.XPATH, "/html/body/div/div/div/div[3]/div/div[2]/button[1]")


    def __init__(self, driver):
        super(MapMangamentPage, self).__init__(driver)

    def get_Url(self):
        # management URL 입력
        self.get(self.main_url)

    def click_manifestOpen(self):
        # manifest Open 버튼 클릭
        self.click(self.manifestOpen)

    def click_Xbutton(self):
        # X 버튼 클릭
        self.click(self.Xbtn)

    def click_MainKor(self):
        # 메인 언어 한국어 설정
        self.click(self.mainLanguage)
        self.click(self.mainKor)

    def click_MainEng(self):
        # 메인 언어 English 설정
        self.click(self.mainLanguage)
        self.click(self.mainEng)

    def click_MainSpn(self):
        # 메인 언어 English 설정
        self.click(self.mainLanguage)
        self.click(self.mainSpn)

    def click_MainJpn(self):
        # 메인 언어 English 설정
        self.click(self.mainLanguage)
        self.click(self.mainJpn)

    def check_SubKor(self):
        return self.find_element(self.subKor).get_attribute("aria-hidden")

    def check_SubEng(self):
        return self.find_element(self.subEng).get_attribute("aria-hidden")

    def check_SubSpn(self):
        return self.find_element(self.subSpn).get_attribute("aria-hidden")

    def check_SubJPN(self):
        return self.find_element(self.subJpn).get_attribute("aria-hidden")

    def clear_title(self):
        # Title 입력 삭제
        self.click(self.titleInput)
        self.clear(self.titleInput)

    def title_Input(self, Txt):
        # 타이틀 입력
        self.send_keys(self.titleInput, Txt)

    def check_Title(self, Txt):
        for i in self.find_elements(self.mapList):
            if Txt in i.text:
                assert (i.text == Txt)
                return i.text

    def click_Complete(self):
        # Complete 클릭
        self.click(self.completeBtn)

    def click_cancel(self):
        # Cancel 클릭
        self.click(self.cancelBtn)

    def check_Untitled(self):
        for i in self.find_elements(self.mapList):
            if 'Untitled' in i.text:
                assert (i.text == "Untitled")
                return

    def click_Use(self):
        self.click(self.mapUseList)

    def creaft_Draft(self):
        self.click(self.mapUseDraft)

    def creaft_Publish(self):
        # Publish Map 생성
        self.click(self.mapUsePublish)

    def creaft_Archive(self):
        # Archive Map 생성
        self.click(self.mapUseArchive)

    def legalnotice_True(self):
        # legalnotice True 전환
        self.click(self.legalNoticeButton)

    def legalnotice_False(self):
        # leganotice False 전환
        self.click(self.legalNoticeButton)

    def legalnotice_input(self):
        self.click(self.legalNoticeInput)
        self.send_keys(self.legalNoticeInput, "현재 테스트 자동화로 법적 고지 입력 테스트 중입니다.")

    def clear_legalnotice(self):
        self.click(self.legalNoticeInput)
        self.clear(self.legalNoticeInput)

