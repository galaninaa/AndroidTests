from time import sleep
import TestVariables as TV


def preLogin(driver):
    current_page = str(driver.page_source)
    driver.find_element_by_xpath('//android.widget.Button[@text="Sign in"]').click()
    email = driver.find_element_by_xpath('//android.widget.EditText')
    sleep(1)
    account_email = TV.AccountData['email']
    email.send_keys(str(account_email))
    driver.find_element_by_xpath('//android.widget.Button[@text="CONTINUE"]').click()


def findLifeOrDead(victim, driver):
    print victim.keys()
    element = None
    for keys in victim.keys():
        if keys == 'id':
            try:
                element = driver.find_element_by_id(victim[keys])
                print "Find by id"
                break
            except:
                print "Could not find by id..."
        if keys == 'xpath':
            try:
                element = driver.find_element_by_xpath(victim[keys])
                print "Find by xpath"
                break
            except:
                print "Could not find by xpath..."
        if keys == 'accessibility id':
            try:
                element = driver.find_element_by_accessibility_id(victim[keys])
                print "Find by accessibility id"
                break
            except:
                print "Could not find by accessibility id..."
    return element


def OpenSetings(driver):
    print "Let's open Settings"
    MO = findLifeOrDead(TV.MoreOptions, driver)
    MO.click()
    print "More Options was tapped"
    sleep(4)
    Settings = findLifeOrDead(TV.More_Options.Settings, driver)
    Settings.click()
    print "Settings was tapped"
    sleep(4)
    Header = findLifeOrDead(TV.Settings.Header, driver)
    print "Header: ", Header.text, " is on screen"

    ScrollView = findLifeOrDead(TV.Settings.SettingsScrollViewContainer, driver)
    print "ScrollView is on screen"

    AccountData = [TV.Settings.AccountData, TV.Settings.AccountName, TV.Settings.AccountEmail,
                   TV.Settings.AccountPhone]
    for element in AccountData:
        OnScreen = findLifeOrDead(element, driver)
        print "Element ", element, " with text ", OnScreen.text, " is on screen"


def TapOnSettingsItem(item, driver):
    # item - is key from TV.Settings.MenuItems
    AllSettingsElements = TV.Settings.giveAllSettingsPath(TV.Settings.MenuItems)
    element = driver.find_element_by_xpath(AllSettingsElements[item])
    print "Element ", AllSettingsElements[item], " with text ", element.text, " is on screen"
    element.click()
    print "Element was clicked"
