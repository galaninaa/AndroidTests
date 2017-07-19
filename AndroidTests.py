import unittest
from appium import webdriver
import argparse
import sys
import xmlrunner
import os
from time import sleep
import TestVariables as TV
import TestMethods as TM



def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device_name',
                        default='84B7N16804000866')
    parser.add_argument('-pl', '--platform', default='Android')
    parser.add_argument('-l', '--link', default='localhost')
    parser.add_argument('-p', '--port', default='4723')
    parser.add_argument('-f', '--folder', default='Android')
    parser.add_argument('-app_path', '--app_path', default=TV.AppPath)
    parser.add_argument('-plV', '--platformVersion', default='7.1.2')
    return parser

parser = create_parser()
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
        parser = create_parser()
        namespace = parser.parse_args(sys.argv[1:])
        device_name = namespace.device_name
        platform = namespace.platform
        app_path = namespace.app_path
        "Setup for the test"
        desired_caps = {'platformName': platform, 'platformVersion': platformVersion, 'app': app_path,
                        'deviceName': device_name, 'waitForAppScript': '$.delay(3500)', 'noReset': True,
                        'fullReset': False, "appActivity": 'com.talkatone.vedroid.TalkatoneTabsMain'}

        self.driver = webdriver.Remote(
            'http://' + str(link) + ':' + str(port) + '/wd/hub', desired_caps)
        print "##########################################################"
        print "Set up - OK!"
        print self.driver.session_id
        # TM.preLogin(self.driver)

        sleep(20)

    def tearDown(self):
        """Tear down the test"""
        print "\n##########################################################"
        print "##########################################################"
        print "/\/\//\/\/\//\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ "
        print "##########################################################"
        self.driver.quit()
        print"\n"

    def test_Calls_MoreOptions(self):
        test_name = 'Calls > More Options Validation'
        print "Test: ", test_name

        sleep(2)
        calls = TM.findLifeOrDead(TV.Calls, self.driver)
        calls.click()
        sleep(2)
        m_o = TM.findLifeOrDead(TV.MoreOptions, self.driver)
        m_o.click()
        sleep(2)
        TM.findLifeOrDead(TV.More_Options.Settings, self.driver)
        TM.findLifeOrDead(TV.More_Options.Help, self.driver)
        TM.findLifeOrDead(TV.More_Options.Credits, self.driver)
        TM.findLifeOrDead(TV.More_Options.ClearCallHistory, self.driver)

    def test_Messages_MoreOptions(self):
        test_name = 'Messages > More Options Validation'
        print "Test: ", test_name

        sleep(2)
        messages = TM.findLifeOrDead(TV.Messages, self.driver)
        messages.click()
        sleep(2)
        m_o = TM.findLifeOrDead(TV.MoreOptions, self.driver)
        m_o.click()
        sleep(2)
        TM.findLifeOrDead(TV.More_Options.Settings, self.driver)
        TM.findLifeOrDead(TV.More_Options.Help, self.driver)
        TM.findLifeOrDead(TV.More_Options.Credits, self.driver)
        TM.findLifeOrDead(TV.More_Options.ClearMessageHistory, self.driver)

    def test_Contacts_MoreOptions(self):
        test_name = 'Contacts > More Options Validation'
        print "Test: ", test_name

        sleep(2)
        contacts = TM.findLifeOrDead(TV.Contacts, self.driver)
        contacts.click()
        sleep(2)
        m_o = TM.findLifeOrDead(TV.MoreOptions, self.driver)
        m_o.click()
        sleep(2)
        TM.findLifeOrDead(TV.More_Options.Settings, self.driver)
        TM.findLifeOrDead(TV.More_Options.Help, self.driver)
        TM.findLifeOrDead(TV.More_Options.Credits, self.driver)
        TM.findLifeOrDead(TV.More_Options.DisplayOptions, self.driver)

    def test_Favourites_MoreOptions(self):
        test_name = 'Favourites > More Options Validation'
        print "Test: ", test_name

        sleep(2)
        favorites = TM.findLifeOrDead(TV.Favorites, self.driver)
        favorites.click()
        sleep(2)
        m_o = TM.findLifeOrDead(TV.MoreOptions, self.driver)
        m_o.click()
        sleep(2)
        TM.findLifeOrDead(TV.More_Options.Settings, self.driver)
        TM.findLifeOrDead(TV.More_Options.Help, self.driver)
        TM.findLifeOrDead(TV.More_Options.Credits, self.driver)

    def test_Settings_Screen(self):
        test_name = 'Settings > Validation Settings screen'
        print "Test: ", test_name
        TM.OpenSetings(self.driver)

        buttons = [TV.Settings.BurnNumberButton, TV.Settings.ShareNumberButton, TV.Settings.IternationalCallsSubState,
                   TV.Settings.PaidCredits, TV.Settings.BuyCredits, TV.Settings.RemoveAdsSwitch,
                   TV.Settings.IternationalCallsSubStateMore]
        for element in buttons:
            on_screen = TM.findLifeOrDead(element, self.driver)
            print "Element ", element, "  is on screen"

        all_settings_elements = TV.Settings.giveAllSettingsPath(TV.Settings.MenuItems)

        for menu_item_key in TV.Settings.MenuItems[1:7]:
            self.driver.find_element_by_xpath(all_settings_elements[menu_item_key])
            print "Element ", all_settings_elements[menu_item_key], " with number ", menu_item_key, " is on screen"

        all_small_elements = TV.Settings.giveAllSettingsPath(TV.Settings.SmallMenuItems)

        for SmallMenuItem in TV.Settings.SmallMenuItems:
            print SmallMenuItem
            self.driver.find_element_by_xpath(all_small_elements[SmallMenuItem])
            print "Element ", SmallMenuItem, " is on screen"

        start_scroll = self.driver.find_element_by_xpath(all_settings_elements['Texting'])
        end_scroll = self.driver.find_element_by_xpath(all_settings_elements['Credits'])

        self.driver.drag_and_drop(start_scroll, end_scroll)

        for menu_item_key in TV.Settings.MenuItems[7:]:
            self.driver.find_element_by_xpath(all_settings_elements[menu_item_key])
            print "Element ", all_settings_elements[menu_item_key], " with number ", menu_item_key, " is on screen"

        contact_us = self.driver.find_element_by_xpath(TV.Settings.ContactUs['xpath'])
        print "Element ", TV.Settings.ContactUs['xpath'], " with text ", contact_us.text, " is on screen"

    def test_Settings_GetANewNumber(self):
        test_name = 'Settings > Get A New Number'
        print "Test: ", test_name

        TM.OpenSetings(self.driver)
        TM.TapOnSettingsItem('Get a New Number', self.driver)
        sleep(5)

    def test_Settings_Credits(self):
        test_name = 'Settings > Credits'
        print "Test: ", test_name

        TM.OpenSetings(self.driver)
        TM.TapOnSettingsItem('Credits', self.driver)
        sleep(5)

    def test_Settings_RemoveAds(self):
        test_name = 'Settings > Remove Ads'
        print "Test: ", test_name

        TM.OpenSetings(self.driver)
        TM.TapOnSettingsItem('Remove Ads', self.driver)
        sleep(5)

    def test_Settings_InternationalCalls(self):
        test_name = 'Settings > International Calls'
        print "Test: ", test_name

        TM.OpenSetings(self.driver)
        TM.TapOnSettingsItem('International Calls', self.driver)
        sleep(5)

    def test_Settings_NotificationsSounds(self):
        test_name = 'Settings > Notifications & Sounds'
        print "Test: ", test_name

        TM.OpenSetings(self.driver)
        TM.TapOnSettingsItem('Notifications & Sounds', self.driver)
        sleep(5)


if __name__ == '__main__':
    print "START!"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuto)
    print "SUITE"
    unittest.TextTestRunner().run(suite)

    # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/Users/galaninaa/test-reports/' ))
    # os.path.dirname(__file__)+'/'+str(folder) + '/' + 'report' +
    # str(datetime.datetime.now().date()))

    # for running with report
    #       runner = xmlrunner.XMLTestRunner()
    #       runner. run(suite)
