from selenium.webdriver.common.by import By

from setup import create_browser, calculation, get_alert_text

browser = create_browser()

browser.get('https://suninjuly.github.io/alert_accept.html')

browser.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()

browser.switch_to.alert.accept()

formula_text = browser.find_element(By.CSS_SELECTOR, 'label .nowrap').text.strip()
x_text = browser.find_element(By.CSS_SELECTOR, '#input_value').text.strip()
result = calculation(formula_text, x_text)

browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
browser.find_element(By.CSS_SELECTOR, 'button').click()

get_alert_text(browser)
