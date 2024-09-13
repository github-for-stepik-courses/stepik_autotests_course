from selenium.webdriver.common.by import By

from setup import create_browser

browser = create_browser()

browser.get('https://suninjuly.github.io/text_input_task.html')

browser.find_element(By.CSS_SELECTOR, 'input').send_keys('get()')
browser.find_element(By.CSS_SELECTOR, 'button').click()
