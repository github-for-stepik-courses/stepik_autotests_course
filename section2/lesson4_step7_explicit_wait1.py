from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from setup import create_browser

browser = create_browser()

browser.get('https://suninjuly.github.io/wait2.html')

verify_button = browser.find_element(By.CSS_SELECTOR, '#verify')
WebDriverWait(browser, 5).until(ec.element_to_be_clickable(verify_button)).click()

message = browser.find_element(By.CSS_SELECTOR, '#verify_message').text
assert 'successful' in message
