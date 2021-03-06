import unittest
from appium import webdriver
import argparse
from time import sleep
import TestVariables as tv
import TestMethods as tm
import adb_info
from appium.webdriver.common.touch_action import TouchAction



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


    def test_Keypad_Send_a_50_Messages(self):
        test_name = 'Messaging testing'
        print "Test: ", test_name
        tm.clear_messages(self.driver)
        empty_screen = True

        while empty_screen == True:
            try:
                self.driver.find_element_by_id('com.talkatone.android:id/avatar').click()
                empty_screen = False
            except:
                sleep(5)
        received_msg_incoming = ''
        print 'Chat screen is opened...'
        sleep(10)
        print('Becouse appium doesn\'t work with our message screen - I will do some special thing!')
        self.driver.tap([(975, 73), (1080, 199)])
        print 'I taped something on screen'
        sleep(5)
        self.driver.back()
        received_msg = 'This is the message '
        sent_msg = int(0)
        error_counter = 0
        while sent_msg < 50:

            try:
                received_msg_text = received_msg + str(sent_msg)
                print 'I\'ll wait incoming message with text: ', received_msg_text
                sleep(5)
                Message = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.talkatone.android:id/message_text" and @text="' + received_msg_text +'"]')
                received_msg_incoming = Message.text

                print "Received messages: ", received_msg_incoming
                sent_msg_text = received_msg_incoming + ' answer'

                self.driver.find_element_by_id('com.talkatone.android:id/msgText').send_keys(sent_msg_text)
                sleep(2)
                self.driver.find_element_by_id('com.talkatone.android:id/btnSend').click()
                sleep(2)

                sent_msg_obj = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.talkatone.android:id/message_text" and @text="' + sent_msg_text +'"]')
                print "Sent messages: ", sent_msg_obj.text

                sent_msg += int(1)
                error_counter = 0
                #tm.clear_chat(self.driver)
            except:
                sleep(10)
                print "No messages!..Wait..."
                error_counter += 1
                print 'Error counter was increased. Error counter = ', error_counter
                if error_counter > 5:
                    waiting_for_answer = False
                    print 'Error counter  was maximum increased.'
                    tm.clear_chat(self.driver)
                    break



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

    # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/Users/galaninaa/test-reports/' ))
    # os.path.dirname(__file__)+'/'+str(folder) + '/' + 'report' +
    # str(datetime.datetime.now().date()))

    # for running with report
    #       runner = xmlrunner.XMLTestRunner()
    #       runner. run(suite)
