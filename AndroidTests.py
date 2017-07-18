import unittest
from appium import webdriver
import xmlrunner
import argparse
import sys
import os
from time import sleep
from lxml import etree
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
    parser.add_argument('-app_path', '--app_path', default = '/Users/builder/Documents/builds/apk/Release/talkatoneandroid-5.6.4-rc2.apk')
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
        desired_caps["appActivity"] = 'com.talkatone.vedroid.amzlogin.loginscreens.TktnLoginWelcome'
        self.driver = webdriver.Remote(
            'http://' + str(link) + ':' + str(port) + '/wd/hub', desired_caps)
        print "set up - OK!"
        sleep(10)
        print self.driver.session_id
        TM.preLogin()

        sleep(20)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_Test(self):
        sleep(2)
        self.driver.find_element_by_accessibility_id(TV.MoreOptions['accessibility id']).click()
        sleep(2)
        self.driver.find_element_by_xpath(TV.More_Options.Credits).click
        sleep(2)