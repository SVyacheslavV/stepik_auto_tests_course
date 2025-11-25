import time
import math
import os # Импортируем "os" для чтения переменного окружения

from dotenv import load_dotenv # из "dotenv", импортируем "load_dotenv"

load_dotenv() # Подгружаем из ".env"

from selenium import webdriver
from selenium.webdriver.common.by import By


# функция для вычисления y
def calk(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser: # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
    browser.get('https://suninjuly.github.io/redirect_accept.html') # открываем url
    time.sleep(5) # делаем паузу для наглядности
    # browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(1) # делаем паузу для наглядности

    windows = browser.window_handles
    print(windows)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    print(x)
    y = calk(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    time.sleep(2)
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1] # получаем значение из модального окна
    print(f'Поздравляю, вы выполнили задание! Скопируйте этот код как ответ на тест Степика: {answer}')

    # Нажимаем на кнопку "Ok"
    alert.accept()

    # Переходим на главную страницу, авторизуемся, затем на страницу с заданием
    browser.get("https://stepik.org/catalog")
    time.sleep(3)  # делаем паузу для наглядности
    browser.find_element(By.ID, "ember955").click()  # кликаем кнопку Вход с id="ember955"
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

    browser.get("https://stepik.org/lesson/184253/step/6")  # переходим на страницу с задачей
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

