import time
import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv # из "dotenv", импортируем "load_dotenv"

load_dotenv() # Подгружаем из ".env"

"""Часть 1. Решение задачи"""

# функция для вычисления y
def calk(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/explicit_wait2.html')

    button = browser.find_element(By.ID, 'book') # ищем кнопку с id='book'

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button.click() # кликаем кнопку
    # прокручиваем страницу до видимости кнопки
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    x = browser.find_element(By.ID, 'input_value').text # получаем значение x из элемента id='input_value'
    print(x)
    y = calk(x) # вычисляем значение y
    browser.find_element(By.ID, 'answer').send_keys(y) # вставляем значение y в элемент с id='answer'
    browser.find_element(By.ID, 'solve').click() # кликаем кнопку с id='solve'
    time.sleep(2) # делаем паузу для наглядности
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1] # получаем значение из модального окна
    print(f'Поздравляю, вы выполнили задание! Скопируйте этот код как ответ на тест Степика: {answer}')
    alert.accept() # Нажимаем на кнопку "Ok"

    """Часть 2. Отправка решения на сайт"""

    # Переходим на главную страницу, авторизуемся, затем на страницу с заданием
    browser.get("https://stepik.org/catalog")
    time.sleep(3)  # делаем паузу для наглядности
    # кликаем кнопку Вход class='ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button'
    browser.find_element(
        By.CLASS_NAME, 'ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button').click()
    time.sleep(2)  # делаем паузу для наглядности
    s_username = browser.find_element(By.ID, "id_login_email")  # ищем поле для ввода логина
    s_username.send_keys(os.getenv('login'))  # вводим логин из файла .env
    time.sleep(2)  # делаем паузу для наглядности
    s_password = browser.find_element(By.ID, "id_login_password")  # ищем поле для ввода пароля
    s_password.send_keys(os.getenv('password'))  # вводим пароль из файла .env
    time.sleep(2)  # делаем паузу для наглядности

    # Ищем кнопку для авторизации
    browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader').click()
    time.sleep(5)  # делаем паузу для наглядности

    browser.get("https://stepik.org/lesson/181384/step/8")  # переходим на страницу с задачей
    time.sleep(5)  # делаем паузу для наглядности

    # Находим поле для ввода ответа
    textarea = browser.find_element(By.TAG_NAME, "textarea")

    # Скролл до текстового поля, иначе элемент не находится
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)
    time.sleep(5)  # делаем паузу для наглядности
    # Вставляем текст ответа в найденное поле
    textarea.send_keys(answer)

    # Отправляем ответ
    browser.find_element(By.CLASS_NAME, "submit-submission").click()

    time.sleep(3)  # делаем паузу для наглядности
    print('Ответ успешно отправлен!')
