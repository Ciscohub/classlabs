#!/usr/bin/env python3

# python3 -m pip install selenium

# download gecko webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://dominos.com/en/")

time.sleep(2)
click_sign_in = driver.find_element_by_xpath("/html/body/header/nav[1]/div[1]/div[3]/a")
click_sign_in.click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="Email"]').click()
driver.find_element_by_xpath('//*[@id="Email"]').send_keys("sams.test.dev@gmail.com")

time.sleep(1)
driver.find_element_by_xpath('//*[@id="Password"]').click()
driver.find_element_by_xpath('//*[@id="Password"]').send_keys("yummypizza" + Keys.RETURN)
time.sleep(3)

driver.find_element_by_xpath('/html/body/header/nav[1]/div[1]/ul/li[2]/a').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/form/div/div[1]/label[1]/span[1]/img').click()
time.sleep(1)

driver.find_element_by_xpath('html/body/div[2]/div[3]/div/div/div[2]/form/div/div[2]/div[3]/div[1]/select/option[3]').click()
time.sleep(1)







