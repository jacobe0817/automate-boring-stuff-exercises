from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
login_field = browser.find_element(by=By.CSS_SELECTOR, value='#identifierId')
login_field.send_keys('jacob.david.epp@gmail.com')
next_button = browser.find_element(by=By.CSS_SELECTOR, value='.VfPpkd-LgbsSe-OWXEXe-k8QpJ > div:nth-child(3)')
next_button.click()