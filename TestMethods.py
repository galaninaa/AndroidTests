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

def