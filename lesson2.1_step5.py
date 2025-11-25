import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# функция для расчёта x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://suninjuly.github.io/math.html')  # открываем url
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    print(f'x = {x}')
    y = calc(x)
    print(f'y = {y}')
    browser.find_element(By.ID, 'answer').send_keys(y)  # вставляем значение y в id='answer'
    time.sleep(2)
    browser.find_element(By.ID, 'robotCheckbox').click()  # кликаем checkbox
    time.sleep(2)
    # browser.find_element(By.ID, 'robotsRule').click() # поиск по id='robotsRule'
    browser.find_element(By.CSS_SELECTOR, '[value="robots"]').click()  # поиск по значению атрибута value="robots"
    time.sleep(2)
    # browser.find_element(By.CLASS_NAME, 'btn.btn-default').click() # пробел в значении заменяем на точку!
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()  # поиск по значению атрибута
    # browser.find_element(By.TAG_NAME, 'button').click() # поиск по тегу
    time.sleep(2)
    alert = browser.switch_to.alert
    print(f'Поздравляю, вы выполнили задание! Скопируйте этот код как ответ на тест Степика: {alert.text.split()[-1]}')
