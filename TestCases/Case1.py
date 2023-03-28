import time

from TestCases.Base import BaseTest
from Pages.MapManagementPage import MapMangamentPage
from Pages.MapAreaSettingPage import MapAreaSetting
from Pages.CanvasPage import CanvasPage

class TestIn(BaseTest):

    def test_Case1(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.click_Xbutton()

        self.assertEqual(Management.not_Exist(Management.MapManifestPopup) == 'None', False)

    def test_Case2(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.click_cancel()

        self.assertEqual(Management.not_Exist(Management.MapManifestPopup) == 'None', False)

    def test_Case3(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.title_Input("Case3_Test")
        Management.click_Complete()

        Management.get_Url()
        spltted = str()
        for i in Management.find_elements(Management.mapList):
            if 'Case3_Test' in i.text:
                spltted = i.text.split('/n')[0]
                return spltted

        self.assertEqual('Case3_Test', spltted == "Case3_Test")

    def test_Case4(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.clear_title()
        Management.click_Complete()

        Management.get_Url()

        spltted = str()
        for i in Management.find_elements(Management.mapList):
            if 'Untitled' in i.text:
                spltted = i.text.split('/n')[0]
                return spltted

        self.assertEqual('Untitled', spltted == "Untitled")

    def test_Case5(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.click_Use()
        Management.creaft_Draft()
        Management.click_Complete()

        time.sleep(2)

        self.assertIn("http://15.165.232.220:3000/setting/", BaseTest.currentURL(self))

    def test_Case6(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.click_Use()
        Management.creaft_Archive()
        Management.click_Complete()

        time.sleep(2)

        self.assertIn("http://15.165.232.220:3000/setting/", BaseTest.currentURL(self))

    def test_Case7(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.click_Use()
        Management.creaft_Archive()
        Management.click_Complete()

        time.sleep(2)

        self.assertIn("http://15.165.232.220:3000/setting/", BaseTest.currentURL(self))

    def test_Case8(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.click_MainKor()

        assert Management.check_SubKor() == "false"

    def test_Case9(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.click_MainEng()

        assert Management.check_SubEng() == "false"

    def test_Case10(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.click_MainSpn()

        assert Management.check_SubSpn() == "false"

    def test_Case11(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.click_MainSpn()

        assert Management.check_SubJPN() == "false"

    def test_Case12(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.legalnotice_True()
        Management.legalnotice_input()
        Management.click_Complete()

        time.sleep(2)

        self.assertIn("http://15.165.232.220:3000/setting/", BaseTest.currentURL(self))

    def test_Case13(self):
        Management = MapMangamentPage(self.driver)
        Management.get_Url()
        Management.click_manifestOpen()
        Management.legalnotice_True()
        Management.clear_legalnotice()
        Management.click_Complete()

        time.sleep(2)

        self.assertIn("http://15.165.232.220:3000/setting/", BaseTest.currentURL(self))