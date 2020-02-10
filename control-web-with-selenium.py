#! python3

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com/')
element = browser.find_element_by_css_selector('.main > ul:nth-child(16) > li:nth-child(1) > a:nth-child(1)')
element.click()

searchElem = browser.find_element_by_css_selector('')
searchElem.send_keys('some key words')
searchElem.submit()

browser.back()
browser.forward()
browser.refresh()
browser.quit()