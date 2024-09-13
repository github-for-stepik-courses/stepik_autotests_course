from selenium.webdriver.common.by import By

from setup import create_browser

browser = create_browser()

browser.get('https://suninjuly.github.io/wait1.html')
browser.find_element(By.CSS_SELECTOR, '#verify').click()

message = browser.find_element(By.CSS_SELECTOR, '#verify_message').text
assert 'successful' in message
