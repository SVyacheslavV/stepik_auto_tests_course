import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/find_link_text')
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(By.LINK_TEXT, text)
    link.click()
    time.sleep(2)
    browser.find_element(By.TAG_NAME, 'input').send_keys("Ivan")
    browser.find_element(By.NAME, 'last_name').send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "form-control.city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(2)
    alert = browser.switch_to.alert
    print(f'Поздравляю, вы выполнили задание! Скопируйте этот код как ответ на тест Степика: {alert.text.split()[-1]}')