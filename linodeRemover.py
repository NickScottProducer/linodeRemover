#requires selenium

import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoAlertPresentException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
main_window = driver.current_window_handle



driver.get('https://www.linode.com')

def goto_login():
	elem = driver.find_element_by_css_selector('#main-nav > div > div.collapse.navbar-collapse.navbar-top-collapse > ul > li:nth-child(7) > a')
	elem.click()

def login():
	un = driver.find_element_by_css_selector('#auth_username')
	un.click()
	un.send_keys('#yourusername')#note
	pw = driver.find_element_by_css_selector('#auth_password')
	pw.click()
	pw.send_keys('#yourpassword')#note
	submit = driver.find_element_by_css_selector('#login > input')
	submit.click()


def remove():
	elem = driver.find_element_by_css_selector('#tablekit-table-1 > tbody > tr.list_entry.rowodd > td.list_options > a:nth-child(2)')
	elem.click()
	elem = driver.find_element_by_css_selector('#confirm')
	elem.click()
	elem = driver.find_element_by_css_selector('#remove > input.button')
	elem.click()

goto_login()
login()
for _ in range(500):#number of servers you want to remove in the parenthesis
	remove()
