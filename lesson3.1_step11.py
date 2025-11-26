import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

link = 'https://github.com/SVyacheslavV/stepik_auto_tests_course'

with webdriver.Chrome() as browser:
    """ Отправка ссылки на репозиторий на сайт Степик"""

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

    browser.get("https://stepik.org/lesson/187065/step/11")  # переходим на страницу с задачей
    time.sleep(8)  # делаем паузу для наглядности

    # Находим поле для ввода ответа
    textarea = browser.find_element(By.TAG_NAME, "textarea")

    # Скролл до текстового поля, иначе элемент не находится
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)
    time.sleep(5)  # делаем паузу для наглядности

    textarea.send_keys(link)  # Вставляем ссылку на репозиторий в найденное поле

    # Отправляем ответ
    # browser.find_element(By.CLASS_NAME, "submit-submission").click()

    time.sleep(3)  # делаем паузу для наглядности
    print('Ссылка на репозиторий успешно отправлена!')
