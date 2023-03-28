import time

from TestCases.Base import BaseTest
from Pages.MapAreaSettingPage import MapAreaSetting
from Pages.CanvasPage import CanvasPage

class TestIn(BaseTest):
    def test_Case1(self):
        AreaSetting = MapAreaSetting(self.driver)
        AreaSetting.get_Url()

        text = str()
        for i in AreaSetting.find_elements(MapAreaSetting.BuildingSize):
            text = i.text

        assert text == "Size100 x 100", "Default Checking"


    def test_Case2(self):
        AreaSetting = MapAreaSetting(self.driver)
        AreaSetting.get_Url()

        AreaSetting.click_Cancel()

        time.sleep(2)

        self.assertEqual(self.driver.current_url, "http://15.165.232.220:3000/")

    def test_Case3(self):
        AreaSetting = MapAreaSetting(self.driver)
        AreaSetting.get_Url()

        AreaSetting.click_SizeW()
        AreaSetting.sendKey_SizeW(1000)

        text = str()
        for i in AreaSetting.find_elements(MapAreaSetting.BuildingSize):
            text = i.text

        assert text == "Size1000 x 100", "Default Checking"

    def test_Case4(self):
        AreaSetting = MapAreaSetting(self.driver)
        AreaSetting.get_Url()

        AreaSetting.click_SizeW()
        AreaSetting.sendKey_SizeW(1000000)

        text = str()
        for i in AreaSetting.find_elements(MapAreaSetting.BuildingSize):
            text = i.text

        assert text == "Size99999 x 100", "Default Checking"

    def test_Case5(self):
        AreaSetting = MapAreaSetting(self.driver)
        AreaSetting.get_Url()

        AreaSetting.click_SizeW()
        AreaSetting.sendKey_SizeW(10)

        text = str()
        for i in AreaSetting.find_elements(MapAreaSetting.BuildingSize):
            text = i.text

        assert text == "Size100 x 100", "Default Checking"

    def test_Case6(self):
        AreaSetting = MapAreaSetting(self.driver)
        AreaSetting.get_Url()

        AreaSetting.click_SizeH()
        AreaSetting.sendKey_SizeH(1000)

        text = str()
        for i in AreaSetting.find_elements(MapAreaSetting.BuildingSize):
            text = i.text

        assert text == "Size100 x 1000", "Default Checking"

    def test_Case7(self):
        AreaSetting = MapAreaSetting(self.driver)
        AreaSetting.get_Url()

        AreaSetting.click_SizeH()
        AreaSetting.sendKey_SizeH(100000)

        text = str()
        for i in AreaSetting.find_elements(MapAreaSetting.BuildingSize):
            text = i.text

        assert text == "Size100 x 99999", "Default Checking"

    def test_Case8(self):
        AreaSetting = MapAreaSetting(self.driver)
        AreaSetting.get_Url()

        AreaSetting.click_SizeH()
        AreaSetting.sendKey_SizeH(10)

        text = str()
        for i in AreaSetting.find_elements(MapAreaSetting.BuildingSize):
            text = i.text

        assert text == "Size100 x 100", "Default Checking"

    def test_Case9(self):
        AreaSetting = MapAreaSetting(self.driver)
        AreaSetting.get_Url()

        AreaSetting.click_Sacle()
        AreaSetting.sendKey_Scale(10)

        text = str()
        for i in AreaSetting.find_elements(MapAreaSetting.BuildingScale):
            text = i.text

        assert text == "Scale10cm : 1px"

    def test_Case10(self):
        AreaSetting = MapAreaSetting(self.driver)
        AreaSetting.get_Url()

        AreaSetting.click_Sacle()
        AreaSetting.sendKey_Scale(1000)

        text = str()
        for i in AreaSetting.find_elements(MapAreaSetting.BuildingScale):
            text = i.text

        assert text == "Scale999cm : 1px"

    def test_Case11(self):
        AreaSetting = MapAreaSetting(self.driver)
        AreaSetting.get_Url()

        AreaSetting.click_Sacle()
        AreaSetting.sendKey_Scale(0)

        text = str()
        for i in AreaSetting.find_elements(MapAreaSetting.BuildingScale):
            text = i.text

        assert text == "Scale1cm : 1px"