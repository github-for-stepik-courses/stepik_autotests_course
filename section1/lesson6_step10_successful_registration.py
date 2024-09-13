from selenium.webdriver.common.by import By

from setup import create_browser, create_random_generator

browser = create_browser()

random = create_random_generator()

browser.get('https://suninjuly.github.io/registration1.html')

first_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
first_name_input.send_keys(random.first_name())
last_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
last_name_input.send_keys(random.last_name())
email_input = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
email_input.send_keys(random.email())
browser.find_element(By.CSS_SELECTOR, 'button').click()

welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
assert 'Congratulations! You have successfully registered!' == welcome_text
