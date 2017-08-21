from time import sleep
import TestVariables as tv

from lxml import etree
from StringIO import StringIO


def pre_login(driver):
    current_page = str(driver.page_source)
    driver.find_element_by_xpath('//android.widget.Button[@text="Sign in"]').click()
    email = driver.find_element_by_xpath('//android.widget.EditText')
    sleep(1)
    account_email = tv.account_data['email']
    email.send_keys(str(account_email))
    driver.find_element_by_xpath('//android.widget.Button[@text="CONTINUE"]').click()


def find_life_or_dead(victim, driver):
    print victim.keys()
    element = None
    print 'Let\'s find: ', victim
    for keys in victim.keys():
        if keys == 'id':
            try:
                element = driver.find_element_by_id(victim[keys])
                print "     Find by id"
                break
            except:
                print "     Could not find by id..."
        if keys == 'xpath':
            try:
                element = driver.find_element_by_xpath(victim[keys])
                print "     Find by xpath"
                break
            except:
                print "     Could not find by xpath..."
        if keys == 'accessibility id':
            try:
                element = driver.find_element_by_accessibility_id(victim[keys])
                print "     Find by accessibility id"
                break
            except:
                print "     Could not find by accessibility id..."
    return element


def open_settings(driver):
    print "Let's open Settings"
    m_o = find_life_or_dead(tv.more_options, driver)
    m_o.click()
    print "     More Options was tapped"
    sleep(4)
    settings = find_life_or_dead(tv.More_Options.settings, driver)
    settings.click()
    print "     Settings was tapped"
    sleep(4)
    get_header(driver)
    scroll_view = find_life_or_dead(tv.Settings.settings_scroll_view_container, driver)
    print "ScrollView is on screen"

    account_data = [tv.Settings.account_data, tv.Settings.account_name, tv.Settings.account_email,
                    tv.Settings.account_phone]
    for element in account_data:
        on_screen = find_life_or_dead(element, driver)
        print "Element ", element, " with text ", on_screen.text, " is on screen"


def tap_on_settings_items(item,driver,path):
    # item - is key from TV.Settings.MenuItems
    all_settings_elements = give_all_path(path)
    element = driver.find_element_by_xpath(all_settings_elements[item])
    print "Element ", all_settings_elements[item], " with text ", element.text, " is on screen"
    element.click()
    print "Element was clicked"

def get_header(driver):
    sleep(5)
    header = find_life_or_dead(tv.Settings.header, driver)
    print "header: ", header.text, " is on screen"

def tap_tone(tones, driver):
    print "Let's tap tone!"
    tones_list = give_all_path(tones, 'RadioButton')
    print tones_list
    for tone in tones_list:
        print tone
        driver.find_element_by_xpath(tones_list[tone]).click()
        sleep(0.5)
    driver.find_element_by_xpath(tones_list[tones[1]]).click()


def give_all_path(menu_items, item_type ='TextView'):
    all = {}
    for all_element in menu_items:
        all[all_element] = '//android.widget.'+item_type+'[@text="' + all_element + '"]'
    return all


def parse_all_elevents(driver,type):
    pathes = []
    xml = str(driver.page_source).format(unicode)
    tree = etree.parse(StringIO(xml))
    elements = tree.xpath(
        '//android.widget.' + type)


    print elements
    for element in elements:
        pathes.append(tree.getpath(element))
    return pathes

def clear_messages(driver):

    messages_tab = find_life_or_dead(tv.messages,driver)
    messages_tab.click()
    sleep(5)
    try:
        driver.find_element_by_id('com.talkatone.android:id/empty_text')
    except:
        more_opt = find_life_or_dead(tv.more_options,driver)
        more_opt.click()
        sleep(5)
        clear_messages_history = driver.find_element_by_xpath('//android.widget.TextView[@text = "Clear Message History"]')
        clear_messages_history.click()
        sleep(5)
        driver.find_element_by_id('android:id/button1').click()
    print "Cleared!"




