import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

# функция для расчёта x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:  # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://suninjuly.github.io/execute_script.html') # открываем url
    # time.sleep(2) # делаем паузу для наглядности
    x = browser.find_element(By.ID, 'input_value').text # получаем значение x из элемента id='input_value'
    y = calc(x) # находим значение y
    browser.find_element(By.ID, 'answer').send_keys(y) # вставляем значение y в элемент id='answer'
    browser.find_element(By.ID, 'robotCheckbox').click() # отмечаем checkbox id='robotCheckbox'
    # time.sleep(2) # делаем паузу для наглядности
    radiobutton = browser.find_element(By.ID, 'robotsRule') # находим элемент id='robotsRule'
    # прокручиваем страницу пока radiobutton id='robotsRule' станет виден
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click() # отмечаем radiobutton id='robotsRule'
    # time.sleep(2) # делаем паузу для наглядности
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary') # ищем кнопку class='btn.btn-primary'
    # прокручиваем страницу пока кнопка class='btn.btn-primary' станет видна
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click() # кликаем кнопку
    # time.sleep(2) # делаем паузу для наглядности
    alert = browser.switch_to.alert
    print(f'Поздравляю, вы выполнили задание! Скопируйте этот код как ответ на тест Степика: {alert.text.split()[-1]}')