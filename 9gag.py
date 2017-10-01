#!/usr/bin/env python

'''9gag.py - Scrolls 9gag for you!!!!'''

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
SCROLL_TIME = 8

driver = webdriver.Firefox()
driver.get("https://9gag.com/")
assert "9GAG" in driver.title

time.sleep(4)

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_TIME)