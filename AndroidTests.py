import unittest
from appium import webdriver
import argparse
import sys
import xmlrunner
import os
from time import sleep
import TestVariables as TV
import TestMethods as TM


def createParser():
    parser = argparse.ArgumentParser()
    # e7eddca32184875d43aa17f09e268fb4cfe26eec')
    parser.add_argument('-d', '--device_name',
                        default='84B7N16804000866')
    parser.add_argument('-pl', '--platform', default='Android')
    parser.add_argument('-l', '--link', default='localhost')
    parser.add_argument('-p', '--port', default='4723')
    parser.add_argument('-f', '--folder', default='Android')
    parser.add_argument('-app_path', '--app_path', default = TV.AppPath)
    parser.add_argument('-plV', '--platformVersion', default='7.1.2')
    return parser


parser = createParser()
namespace = parser.parse_args()
device_name = namespace.device_name
platform = namespace.platform
port = namespace.port
folder = namespace.folder
link = namespace.link
platformVersion = namespace.platformVersion
Phone_number = TV.AccountData['number']

class TestAuto(unittest.TestCase):
    def setUp(self):
        parser = createParser()
        namespace = parser.parse_args(sys.argv[1:])
        device_name = namespace.device_name
        platform = namespace.platform
        app_path = namespace.app_path
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = platform
        desired_caps['platformVersion'] = platformVersion
        desired_caps['app'] = app_path
        desired_caps['deviceName'] = device_name
        desired_caps['waitForAppScript'] = '$.delay(3500)'
        desired_caps['noReset'] = True
        desired_caps['fullReset'] = False


        desired_caps["appActivity"] = 'com.talkatone.vedroid.TalkatoneTabsMain'
        self.driver = webdriver.Remote(
            'http://' + str(link) + ':' + str(port) + '/wd/hub', desired_caps)
        print "##########################################################"
        print "Set up - OK!"
        print self.driver.session_id
        #TM.preLogin(self.driver)

        sleep(20)

    def tearDown(self):
        "Tear down the test"
        print "\n##########################################################"
        print "##########################################################"
        print "/\/\//\/\/\//\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ "
        print "##########################################################"
        self.driver.quit()
        print"\n"

    def test_SettingsScreen(self):
        TestName = 'Settings > Validation Settings screen'
        print "Test: ", TestName

        sleep(2)
        self.driver.find_element_by_accessibility_id(TV.MoreOptions['accessibility id']).click()
        sleep(2)
        self.driver.find_element_by_xpath(TV.More_Options.Settings['xpath']).click()
        sleep(10)

        Header = self.driver.find_element_by_id(TV.Settings.Header['id'])
        print "Header: ", Header.text, " is on screen"

        ScrollView = self.driver.find_element_by_id(TV.Settings.SettingsScrollViewContainer['id'])
        print "ScrollView is on screen"

        AccountData = [TV.Settings.AccountData, TV.Settings.AccountName, TV.Settings.AccountEmail,
                       TV.Settings.AccountPhone]
        for element in AccountData:
            OnScreen = self.driver.find_element_by_id(element['id'])
            print "Element ", element, " with text ", OnScreen.text, " is on screen"

        Buttons = [TV.Settings.BurnNumberButton, TV.Settings.ShareNumberButton, TV.Settings.IternationalCallsSubState,
                   TV.Settings.PaidCredits, TV.Settings.BuyCredits, TV.Settings.RemoveAdsSwitch,
                   TV.Settings.IternationalCallsSubStateMore]
        for element in Buttons:
            OnScreen = self.driver.find_element_by_id(element['id'])
            print "Element ", element, "  is on screen"

        AllSettingsElements = TV.Settings.giveAllSettingsPath(TV.Settings.MenuItems)
        for MenuItemNum in range(len(AllSettingsElements)//2 + 1):
            self.driver.find_element_by_xpath(AllSettingsElements[MenuItemNum])
            print "Element ",AllSettingsElements[MenuItemNum], " with number ", MenuItemNum, " is on screen"


        AllSmallElements = TV.Settings.giveAllSettingsPath(TV.Settings.SmallMenuItems)

        for SmallMenuItem in AllSmallElements:
            print SmallMenuItem
            self.driver.find_element_by_xpath(SmallMenuItem)
            print "Element ", SmallMenuItem, " is on screen"

        StartScroll = self.driver.find_element_by_xpath(AllSettingsElements[len(AllSettingsElements)//2])
        EndScroll = self.driver.find_element_by_xpath(AllSettingsElements[0])

        self.driver.drag_and_drop(StartScroll,EndScroll)

        for MenuItemNum in range(len(AllSettingsElements)//2,len(AllSettingsElements)):
            self.driver.find_element_by_xpath(AllSettingsElements[MenuItemNum])
            print "Element ", AllSettingsElements[MenuItemNum], " with number ", MenuItemNum, " is on screen"

        ContactUs = self.driver.find_element_by_xpath(TV.Settings.ContactUs['xpath'])
        print "Element ", TV.Settings.ContactUs['xpath'], " with text ", ContactUs.text, " is on screen"

    def test_SettingsGetANewNumber(self):
        TestName = 'Settings > Get A New Number'
        print "Test: ", TestName

        sleep(2)
        self.driver.find_element_by_accessibility_id(TV.MoreOptions['accessibility id']).click()
        sleep(2)
        self.driver.find_element_by_xpath(TV.More_Options.Settings['xpath']).click()
        sleep(10)

        Header = self.driver.find_element_by_id(TV.Settings.Header['id'])
        print "Header: ", Header.text, " is on screen"

        ScrollView = self.driver.find_element_by_id(TV.Settings.SettingsScrollViewContainer['id'])
        print "ScrollView is on screen"

        AllSettingsElements = TV.Settings.giveAllSettingsPath(TV.Settings.MenuItems)

        item = self.driver.find_element_by_xpath(AllSettingsElements[0])
        print "Element ", AllSettingsElements[0], " with text ", item.text, " is on screen"
        item.click()
        sleep(5)

    def test_SettingsCredits(self):
        TestName = 'Settings > Credits'
        print "Test: ", TestName
        sleep(2)
        self.driver.find_element_by_accessibility_id(TV.MoreOptions['accessibility id']).click()
        sleep(2)
        self.driver.find_element_by_xpath(TV.More_Options.Settings['xpath']).click()
        sleep(10)

        Header = self.driver.find_element_by_id(TV.Settings.Header['id'])
        print "Header: ", Header.text, " is on screen"

        ScrollView = self.driver.find_element_by_id(TV.Settings.SettingsScrollViewContainer['id'])
        print "ScrollView is on screen"

        AllSettingsElements = TV.Settings.giveAllSettingsPath(TV.Settings.MenuItems)

        item = self.driver.find_element_by_xpath(AllSettingsElements[1])
        print "Element ", AllSettingsElements[1], " with text ", item.text, " is on screen"
        item.click()
        sleep(5)

    def test_SettingsRemoveAds(self):
        TestName = 'Settings > Remove Ads'
        print "Test: ", TestName

        sleep(2)
        self.driver.find_element_by_accessibility_id(TV.MoreOptions['accessibility id']).click()
        sleep(2)
        self.driver.find_element_by_xpath(TV.More_Options.Settings['xpath']).click()
        sleep(10)

        Header = self.driver.find_element_by_id(TV.Settings.Header['id'])
        print "Header: ", Header.text, " is on screen"

        ScrollView = self.driver.find_element_by_id(TV.Settings.SettingsScrollViewContainer['id'])
        print "ScrollView is on screen"

        AllSettingsElements = TV.Settings.giveAllSettingsPath(TV.Settings.MenuItems)
        item = self.driver.find_element_by_xpath(AllSettingsElements[2])
        print "Element ", AllSettingsElements[2], " with text ", item.text, " is on screen"
        item.click()
        sleep(5)

if __name__ == '__main__':
    print "START!"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuto)
    print "SUITE"
    unittest.TextTestRunner().run(suite)

    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/Users/galaninaa/test-reports/' ))
    # outfile_ = open("/Users/galaninaa/test-reports/"+ str(folder)+'/' + 'report '+ str(datetime.datetime.now()) + '.xml', "w")
    # os.path.dirname(__file__)+'/'+str(folder) + '/' + 'report' +
    # str(datetime.datetime.now().date()))

    #for running with report
    #       runner = xmlrunner.XMLTestRunner()
    #       runner. run(suite)