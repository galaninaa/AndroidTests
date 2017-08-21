import unittest
from appium import webdriver
import argparse
import sys
import xmlrunner
import os
from time import sleep
import TestMethods as tm
import TestVariables as tv
import adb_info
import subprocess



def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--device_name',
                        default='d73bc030')
    parser.add_argument('-pl', '--platform', default='Android')
    parser.add_argument('-l', '--link', default='localhost')
    parser.add_argument('-p', '--port', default='4723')
    parser.add_argument('-f', '--folder', default='Android')
    parser.add_argument('-app_path', '--app_path', default=tv.app_path)
    parser.add_argument('-plV', '--platform_version', default='4.4.2')
    return parser

parser = create_parser()
namespace = parser.parse_args()
device_name = namespace.device_name
platform = namespace.platform
port = namespace.port
folder = namespace.folder
link = namespace.link
platform_version = namespace.platform_version
app_path = namespace.app_path
phone_number = tv.account_data['number']


class TestAuto(unittest.TestCase):
    def setUp(self):
        "Setup for the test"
        desired_caps = {'platformName': platform, 'platformVersion': platform_version, 'app': app_path,
                        'deviceName': device_name, 'waitForAppScript': '$.delay(3500)', 'noReset': True,
                        'fullReset': False, "appActivity": 'com.talkatone.vedroid.TalkatoneTabsMain'}

        self.driver = webdriver.Remote(
            'http://' + str(link) + ':' + str(port) + '/wd/hub', desired_caps)
        print "\n.*....*.*****.*....*....*...*******.*****..****..*******."
        print ".**...*.*......*...*...*.......*....*.....*.........*...."
        print ".*.*..*.*****...*.*.*.*........*....*****..***......*...."
        print ".*..*.*.*.......*.*.*.*........*....*.........*.....*...."
        print ".*...**.*****....*...*.........*....*****.****......*...."

        print "Set up - OK!"
        print self.driver.session_id
        # TM.preLogin(self.driver)

        sleep(0)

    def tearDown(self):
        """Tear down the test"""
        print "##########################################################"
        self.driver.quit()
        print"\n"

    '''

    def test_Calls_MoreOptions(self):
        test_name = 'Calls > More Options Validation'
        print "Test: ", test_name

        sleep(2)
        calls = tm.find_life_or_dead(tv.calls, self.driver)
        calls.click()
        sleep(2)
        m_o = tm.find_life_or_dead(tv.more_options, self.driver)
        m_o.click()
        sleep(2)
        tm.find_life_or_dead(tv.More_Options.settings, self.driver)
        tm.find_life_or_dead(tv.More_Options.help, self.driver)
        tm.find_life_or_dead(tv.More_Options.credits, self.driver)
        tm.find_life_or_dead(tv.More_Options.clear_call_history, self.driver)

    def test_Messages_MoreOptions(self):
        test_name = 'Messages > More Options Va                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            lidation'
        print "Test: ", test_name

        sleep(2)
        messages = tm.find_life_or_dead(tv.messages, self.driver)
        messages.click()
        sleep(2)
        m_o = tm.find_life_or_dead(tv.more_options, self.driver)
        m_o.click()
        sleep(2)
        tm.find_life_or_dead(tv.More_Options.settings, self.driver)
        tm.find_life_or_dead(tv.More_Options.help, self.driver)
        tm.find_life_or_dead(tv.More_Options.credits, self.driver)
        tm.find_life_or_dead(tv.More_Options.clear_message_history, self.driver)

    def test_Contacts_MoreOptions(self):
        test_name = 'Contacts > More Options Validation'
        print "Test: ", test_name

        sleep(2)
        contacts = tm.find_life_or_dead(tv.contacts, self.driver)
        contacts.click()
        sleep(2)
        m_o = tm.find_life_or_dead(tv.more_options, self.driver)
        m_o.click()
        sleep(2)
        tm.find_life_or_dead(tv.More_Options.settings, self.driver)
        tm.find_life_or_dead(tv.More_Options.help, self.driver)
        tm.find_life_or_dead(tv.More_Options.credits, self.driver)
        tm.find_life_or_dead(tv.More_Options.display_options, self.driver)

    def test_Favourites_MoreOptions(self):
        test_name = 'Favourites > More Options Validation'
        print "Test: ", test_name

        sleep(2)
        favorites = tm.find_life_or_dead(tv.favorites, self.driver)
        favorites.click()
        sleep(2)
        m_o = tm.find_life_or_dead(tv.more_options, self.driver)
        m_o.click()
        sleep(2)
        tm.find_life_or_dead(tv.More_Options.settings, self.driver)
        tm.find_life_or_dead(tv.More_Options.help, self.driver)
        tm.find_life_or_dead(tv.More_Options.credits, self.driver)

    def test_Settings_Screen(self):
        test_name = 'Settings > Validation Settings screen'
        print "Test: ", test_name
        tm.open_settings(self.driver)

        buttons = [tv.Settings.burn_number_button, tv.Settings.share_number_button, tv.Settings.iternational_calls_sub_state,
                   tv.Settings.paid_credits, tv.Settings.buy_credits, tv.Settings.remove_ads_switch,
                   tv.Settings.iternational_calls_sub_state_more]
        for element in buttons:
            on_screen = tm.find_life_or_dead(element, self.driver)
            print "Element ", element, "  is on screen"

        all_settings_elements = tm.give_all_path(tv.Settings.menu_items)

        for menu_item_key in tv.Settings.menu_items[1:7]:
            self.driver.find_element_by_xpath(all_settings_elements[menu_item_key])
            print "Element ", all_settings_elements[menu_item_key], " with text ", menu_item_key, " is on screen"

        try:
            all_small_elements = tm.give_all_path(tv.Settings.small_menu_items)

            for small_menu_item in tv.Settings.small_menu_items:
                sleep(5)
                self.driver.find_element_by_xpath(all_small_elements[small_menu_item])
                print "Element ", small_menu_item, " is on screen"
        except:
            all_small_elements = tm.give_all_path(tv.Settings.small_menu_items_active_no_ads)

            for small_menu_item in tv.Settings.small_menu_items_active_no_ads:
                sleep(5)
                self.driver.find_element_by_xpath(all_small_elements[small_menu_item])
                print "Element ", small_menu_item, " is on screen"

        start_scroll = self.driver.find_element_by_xpath(all_settings_elements['Texting'])
        end_scroll = self.driver.find_element_by_xpath(all_settings_elements['Credits'])

        self.driver.drag_and_drop(start_scroll, end_scroll)

        for menu_item_key in tv.Settings.menu_items[7:]:
            self.driver.find_element_by_xpath(all_settings_elements[menu_item_key])
            print "Element ", all_settings_elements[menu_item_key], " with number ", menu_item_key, " is on screen"

        contact_us = self.driver.find_element_by_xpath(tv.Settings.contact_us['xpath'])
        print "Element ", tv.Settings.contact_us['xpath'], " with text ", contact_us.text, " is on screen"

    def test_Settings_GetANewNumber(self):
        test_name = 'Settings > Get A New Number'
        print "Test: ", test_name

        tm.open_settings(self.driver)
        tm.tap_on_settings_items('Get a New Number', self.driver,tv.Settings.menu_items)
        sleep(5)

    def test_Settings_Credits(self):
        test_name = 'Settings > Credits'
        print "Test: ", test_name

        tm.open_settings(self.driver)
        tm.tap_on_settings_items('Credits', self.driver,tv.Settings.menu_items)
        sleep(5)

    def test_Settings_RemoveAds(self):
        test_name = 'Settings > Remove Ads'
        print "Test: ", test_name

        tm.open_settings(self.driver)
        tm.tap_on_settings_items('Remove Ads', self.driver,tv.Settings.menu_items)
        sleep(5)

    def test_Settings_InternationalCalls(self):
        test_name = 'Settings > International Calls'
        print "Test: ", test_name

        tm.open_settings(self.driver)
        tm.tap_on_settings_items('International Calls', self.driver,tv.Settings.menu_items)
        sleep(5)

    def test_Settings_NotificationsSounds(self):
        test_name = 'Settings > Notifications & Sounds'
        print "Test: ", test_name

        tm.open_settings(self.driver)
        tm.tap_on_settings_items('Notifications & Sounds', self.driver,tv.Settings.menu_items)
        sleep(5)

        tm.find_life_or_dead(tv.Settings.SoundsAndNotifications.ringtone,self.driver)
        tm.find_life_or_dead(tv.Settings.SoundsAndNotifications.message_notification_sounds, self.driver)
        tm.find_life_or_dead(tv.Settings.SoundsAndNotifications.notification_bar, self.driver)
        tm.find_life_or_dead(tv.Settings.SoundsAndNotifications.display_ongoing_notification, self.driver)
        tm.find_life_or_dead(tv.Settings.SoundsAndNotifications.push_notifications_label, self.driver)

        rington = tm.find_life_or_dead(tv.Settings.SoundsAndNotifications.rington_label,self.driver)
        rington.click()
        sleep(5)
        pathes = tm.parse_all_elevents(self.driver,'RadioButton')

        for path in pathes:
            self.driver.find_element_by_xpath(path).click()

        #tm.tap_tone(tv.Settings.SoundsAndNotifications.rington_tones,self.driver)

        back =  tm.find_life_or_dead(tv.navigate_up, self.driver)
        back.click()

        incoming = tm.find_life_or_dead(tv.Settings.SoundsAndNotifications.incoming_label, self.driver)
        incoming.click()
        sleep(5)
        pathes = tm.parse_all_elevents(self.driver,'RadioButton')

        for path in pathes:
            self.driver.find_element_by_xpath(path).click()

        back = tm.find_life_or_dead(tv.navigate_up, self.driver)
        back.click()

        outgoing = tm.find_life_or_dead(tv.Settings.SoundsAndNotifications.outgoing_label, self.driver)
        outgoing.click()
        sleep(5)
        pathes = tm.parse_all_elevents(self.driver,'RadioButton')

        for path in pathes:
            self.driver.find_element_by_xpath(path).click()

        back = tm.find_life_or_dead(tv.navigate_up, self.driver)
        back.click()

    def test_Settings_Miscellaneous(self):
        test_name = 'Settings > Miscellaneous'
        print "Test: ", test_name

        tm.open_settings(self.driver)

        all_settings_elements = tm.give_all_path(tv.Settings.menu_items)

        start_scroll = self.driver.find_element_by_xpath(all_settings_elements['Texting'])
        end_scroll = self.driver.find_element_by_xpath(all_settings_elements['Credits'])
        self.driver.drag_and_drop(start_scroll, end_scroll)

        tm.tap_on_settings_items('Miscellaneous', self.driver,tv.Settings.menu_items)
        sleep(5)
        tm.get_header(self.driver)
        for element in tv.Settings.Miscellaneous.settings_miscellaneous_settings:
            tm.tap_on_settings_items(element,self.driver,path=tv.Settings.Miscellaneous.settings_miscellaneous_settings)
            tm.get_header(self.driver)
            sleep(4)
            back = tm.find_life_or_dead(tv.navigate_up,self.driver)
            back.click()

    def test_Settings_Passcode(self):
        test_name = 'Settings > Passcode'
        print "Test: ", test_name

        tm.open_settings(self.driver)

        all_settings_elements = tm.give_all_path(tv.Settings.menu_items)

        start_scroll = self.driver.find_element_by_xpath(all_settings_elements['Texting'])
        end_scroll = self.driver.find_element_by_xpath(all_settings_elements['Credits'])
        self.driver.drag_and_drop(start_scroll, end_scroll)

        tm.tap_on_settings_items('Passcode', self.driver, tv.Settings.menu_items)
        sleep(5)

        tm.get_header(self.driver)
        self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.talkatone.android:id/label" and @text="Passcode"]')
        switch = self.driver.find_element_by_id('com.talkatone.android:id/switchWidget')
        print 'Switch: ', switch.text
        switch.click()
        sleep(10)

        buttons = tm.parse_all_elevents(self.driver, 'Button')

        for button in buttons:
            self.driver.find_element_by_xpath(button)

        for x in range(4):
            self.driver.find_element_by_xpath(buttons[1]).click()

        sleep(5)

        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Re-enter a passcode"]')

        for x in range(4):
            self.driver.find_element_by_xpath(buttons[1]).click()
        sleep(5)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Change Passcode"]')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Require Passcode"]')
        switch = self.driver.find_element_by_id('com.talkatone.android:id/switchWidget')
        print 'Switch: ', switch.text
        switch.click()
        self.driver.find_element_by_xpath(
            '//android.widget.TextView[@resource-id="com.talkatone.android:id/label" and @text="Passcode"]')

    def test_Settings_Texting(self):
        test_name = 'Settings > Passcode'
        print "Test: ", test_name

        tm.open_settings(self.driver)

        all_settings_elements = tm.give_all_path(tv.Settings.menu_items)
        tm.tap_on_settings_items('Texting', self.driver, tv.Settings.menu_items)
        sleep(5)

        tm.get_header(self.driver)
        self.driver.find_element_by_xpath(
            '//android.widget.TextView[@resource-id="com.talkatone.android:id/label" and @text="Signature"]')
        self.driver.find_element_by_id('com.talkatone.android:id/switchWidget')
        self.driver.find_element_by_xpath(
            '//android.widget.TextView[@resource-id="com.talkatone.android:id/label" and @text="Save to Camera Roll"]')

'''
    def test_Calls_Voicemail(self):
        test_name = 'Calls > Voicemail'
        print "Test: ", test_name

        sleep(2)
        calls = tm.find_life_or_dead(tv.calls, self.driver)
        calls.click()
        sleep(2)
        voicemail = tm.find_life_or_dead(tv.voicemail, self.driver)
        voicemail.click()
        sleep(2)
        #tm.get_header(self.driver)
        tm.find_life_or_dead(tv.navigate_up, self.driver)
        tm.find_life_or_dead(tv.Voicemail.call_back, self.driver)
        tm.find_life_or_dead(tv.Voicemail.delete, self.driver)
        tm.find_life_or_dead(tv.Voicemail.speaker, self.driver)


if __name__ == '__main__':
    adb_info.android_dev_list()

    devices = adb_info.android_dev_list()

    for device in devices:
        #subprocess.call([adb, "-s", device, "install", "-r", build_path])
        platform_version, app_version = adb_info.android_version(device)
        device_name = device

        print "Tests started for device: ", device_name
        print "Talkatone version: ", app_version
        print "OS version: ", platform_version

        suite = unittest.TestLoader().loadTestsFromTestCase(TestAuto)
        print "SUITE"
        unittest.TextTestRunner().run(suite)

    # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/Users/galaninaa/test-reports/' ))
    # os.path.dirname(__file__)+'/'+str(folder) + '/' + 'report' +
    # str(datetime.datetime.now().date()))

    # for running with report
    #       runner = xmlrunner.XMLTestRunner()
    #       runner. run(suite)
