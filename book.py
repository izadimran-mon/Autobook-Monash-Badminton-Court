from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome(executable_path='/Users/izadi/Downloads/chromedriver_win32/chromedriver')
driver.get('https://fmu-rbs.monash.edu.my/book/venue/6')

# wait for sign in page to pop up

# sign into okta
okta_username = ""
okta_password = ""

username_element = driver.find_element_by_id('okta-signin-username')
username_element.send_keys(okta_username)

password_element = driver.find_element_by_id('okta-signin-password')
password_element.send_keys(okta_password)
# click on sign in
password_element.submit()

# wait for okta-verify 2FA push
try:
    WebDriverWait(driver, 20).until(EC.url_to_be('https://monashuni.okta.com/signin/verify/okta/push'))
    send_push = driver.find_element_by_class_name('o-form-button-bar')
    send_push.submit()
except TimeoutException:
    print("Too long")

print(driver.session_id)
# wait for booking system to pop up
WebDriverWait(driver, 20).until(EC.url_to_be('https://fmu-rbs.monash.edu.my/book/venue/6'))
elem = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[1]/td[2]')
elem.click()
# elem = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[2]/td[2]')
# elem.click()
