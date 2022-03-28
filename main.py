from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import csv

path = "/Users/arpithirani/Documents/chromedriver"
driver = webdriver.Chrome(path)
driver.get('https://buffalo.navigate.eab.com/app/#/authentication/remote/')

driver.implicitly_wait(5)

login_page = driver.find_element(by=By.LINK_TEXT, value="Login with your school account")
login_page.click()

driver.implicitly_wait(0.5)

username = driver.find_element(by=By.NAME, value="j_username")
username.send_keys("arpithir")

password = driver.find_element(by=By.NAME, value="j_password")
password.send_keys("Plumshirt494*")

button = driver.find_element(by=By.ID, value="login-button")
button.click()

driver.implicitly_wait(15)

appointment_button = driver.find_element(by=By.LINK_TEXT, value="Appointments")
appointment_button.click()

driver.implicitly_wait(0.5)

schedule_appointment_button = driver.find_element(by=By.ID, value="create_new_appointment_header_button")
schedule_appointment_button.click()

driver.implicitly_wait(0.5)

# appointment_type_dropdown = Select(driver.find_element())

# def get_cookies(file):
#     with open(file, encoding='utf-8-sig') as f:
#         dict_reader = csv.DictReader(f)
#         list = list(dict_reader)
#     return list
#
# cookie = get_cookies("navigate_cookies.CSV")
#
# id = driver.session_id
#
# driver.add_cookie(id)
#
# for i in cookie:
#     driver.add_cookie(i)
#
# driver.refresh()






