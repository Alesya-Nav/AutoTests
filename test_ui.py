import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
def test_CheckTitle():
    browser=webdriver.Chrome()
    browser.get('https://www.liferay.com/')
    sleep(2)
    element=browser.find_element(By.XPATH,"//a[@class='contact-sales tablet w-button']")
    element.click()
    title=browser.find_element(By.TAG_NAME,'h1')
    assert title.text == 'Talk to a Sales Expert'
    browser.quit()
test_CheckTitle()