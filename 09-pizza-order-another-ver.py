#!/usr/bin/env python3

from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path=r'C:\Users\Achimedes\Downloads\chromedriver_win32\chromedriver.exe')

browser.get('https://www.dominos.com/en/pages/customer/#!/customer/login/')

useremailElm = browser.find_element_by_xpath('//*[@id="Email"]')
useremailElm.send_keys('yourusername@gmail.com')

userpassElm = browser.find_element_by_name('Password')
userpassElm.send_keys('123Pizzaxxxxpassword')

## click button after we enter our credentials
browser.find_element_by_xpath('//*[@id="customerLoginPage"]/div/div/div[2]/div/form/div[14]/div[1]/button').click()

## give page time to load
time.sleep(3)

## move to a new page
browser.get('https://www.dominos.com/en/pages/order/#!/locations/search/')

## get delivery option
browser.find_element_by_xpath('//*[@id="locationSearchForm"]/div/div[1]/label[1]/span[1]').click()

stateElm = browser.find_element_by_name('Region')
stateElm.send_keys('PA')

cityElm = browser.find_element_by_name('City')
cityElm.send_keys('Hershey')

zipElm = browser.find_element_by_name('Postal_Code')
zipElm.send_keys('17022')

stateElm = browser.find_element_by_name('Street')
stateElm.send_keys('101 Chocolate Avenue')

browser.find_element_by_xpath('//*[@id="locationSearchForm"]/div/div[4]/button').click()