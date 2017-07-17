import unittest
from appium import webdriver
import xmlrunner
import argparse
import sys
import os
from time import sleep
from lxml import etree


def createParser():
    parser = argparse.ArgumentParser()
    # e7eddca32184875d43aa17f09e268fb4cfe26eec')
    parser.add_argument('-d', '--device_name',
                        default='84B7N16804000866')
    parser.add_argument('-pl', '--platform', default='Android')
    parser.add_argument('-l', '--link', default='localhost')
    parser.add_argument('-p', '--port', default='4727')
    parser.add_argument('-f', '--folder', default='Android')
    parser.add_argument('-app_path', '--app_path', default = None)
    return parser


parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
device_name = namespace.device_name
platform = namespace.platform
port = namespace.port
folder = namespace.folder
link = namespace.link
Phone_number = ''

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
        desired_caps['app'] = app_path
        desired_caps['deviceName'] = device_name
        desired_caps['waitForAppScript'] = '$.delay(3500)'
        desired_caps['uuid'] = device_name
        desired_caps['launchTimeout'] = '3500'
        desired_caps['noReset'] = True
        desired_caps["appActivity"] = 'com.talkatone.vedroid.amzlogin.loginscreens.TktnLoginWelcome'
        self.driver = webdriver.Remote(
            'http://' + str(link) + ':' + str(port) + '/wd/hub', desired_caps)
        print "set up - OK!"
        sleep(10)
        print self.driver.session_id
        sleep(20)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_Test(self):
        self.driver.f