import unittest
import selenium.webdriver as driver
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C://chromedriver.exe")
driver.get("http://www.google.ru")
xzcdxgfd = driver.find_element_by_name("q")
xzcdxgfd.send_keys("kek")
time.sleep(5)
driver.close()