import unittest
from appium import webdriver
import argparse
import sys
import xmlrunner
import os
from time import sleep
import TestVariables as tv
import TestMethods as tm
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

    def tearDown(self):
        """Tear down the test"""
        print "##########################################################"
        self.driver.quit()
        print"\n"

    def test_Keypad_Make_a_50_calls(self):
        test_name = 'Keyapad > Make a 50 calls'
        print "Test: ", test_name
        print "I'll waiting incoming call."
        sleep(10)
        count = 0
        while count < 50:
            try:
                sleep(10)
                accept = self.driver.find_element_by_id(tv.acs.accept_call)
                accept.click()
                print 'This is the call number ', count+1
                count += 1
                sleep(25)
                self.driver.find_element_by_id(tv.acs.avatar).click()
                print ' Call in progress, time of call is: ', self.driver.find_element_by_id(tv.acs.call_time).text
                sleep(25)
                self.driver.find_element_by_id(tv.acs.avatar).click()
                print ' Call in progress, time of call is: ', self.driver.find_element_by_id(tv.acs.call_time).text
                sleep(25)
                stop_time = self.driver.find_element_by_id(tv.acs.call_time).text
                self.driver.find_element_by_id(tv.acs.clear_call_button)
                print ' Call was stoppeds, time of call is: ', stop_time
            except:
                print 'I\'ll wait the call a few seconds more...'
                sleep(5)


if __name__ == '__main__':
    devices = 0
    while devices == 0:
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
