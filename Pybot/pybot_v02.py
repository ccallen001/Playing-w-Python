from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(
    '/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver')

driver.get('https://www.reddit.com/')

driver.find_element_by_name('user').send_keys('PybotV01')
driver.find_element_by_name('passwd').send_keys('pybotv01')

driver.execute_script("document.querySelector('.submit button').click()")

time.sleep(2)

driver.get('https://www.reddit.com/r/pythonforengineers')

for i in range(1, 6):
    time.sleep(2)

    driver.find_elements_by_css_selector('a.title')[i].click()

    driver.find_element_by_css_selector(
        'div > div.md > textarea').send_keys('I\'m back, baby!')
    driver.find_element_by_css_selector('button.save').click()

    time.sleep(2)

    driver.back()
