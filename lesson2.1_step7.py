import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# функция для расчёта x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://suninjuly.github.io/get_attribute.html')  # открываем url
    # x = browser.find_element(By.ID, 'treasure').get_attribute('valuex') # поиск по class
    x = browser.find_element(By.TAG_NAME, 'img').get_attribute('valuex') # поиск по тегу
    print(f'x = {x}')
    y = calc(x)
    print(f'y = {y}')
    browser.find_element(By.ID, 'answer').send_keys(y)
    time.sleep(2)
    browser.find_element(By.ID, 'robotCheckbox').click()
    time.sleep(2)
    browser.find_element(By.ID, 'robotsRule').click()
    time.sleep(2)
    # browser.find_element(By.CLASS_NAME, 'btn.btn-default').click() # поиск по class
    # browser.find_element(By.TAG_NAME, 'button').click() # поиск по тегу
    browser.find_element(By.CSS_SELECTOR, '[type= "submit"]').click()  # поиск по значению атрибута
    time.sleep(2)
    alert = browser.switch_to.alert
    print(f'Поздравляю, вы выполнили задание! Скопируйте этот код как ответ на тест Степика: {alert.text.split()[-1]}')
