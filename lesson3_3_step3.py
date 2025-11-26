from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import pytest

# данные пользователя которые будем вводить
data = {'first name': 'Ivan', 'last name': 'Petrov', 'email': 'my_mail@yandex.ru'}

link1 = "http://suninjuly.github.io/registration1.html"
link2 = 'https://suninjuly.github.io/registration2.html'


def get_atr(link):
    text = link.get_attribute('placeholder')
    key = [text.split()[-1], ' '.join(text.split()[-2:])][text.split()[-1] == 'name']
    print(f'{key}: {data[key]}')
    return data[key]


def fill_out_the_form(link):
    # Создание объекта ChromeOptions для дополнительных настроек браузера
    options_chrome = webdriver.ChromeOptions()
    # Добавление аргумента '--headless' для запуска браузера в фоновом режиме
    options_chrome.add_argument('--headless')
    # Инициализация драйвера Chrome с указанными опциями
    # Использование менеджера контекста 'with' для автоматического закрытия браузера после выполнения кода
    with webdriver.Chrome(options=options_chrome) as browser:
    # with webdriver.Chrome() as browser:
        browser.get(link)
        # Код заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        first_name.send_keys(get_atr(first_name))
        time.sleep(1)
        last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')

        last_name.send_keys(get_atr(last_name))
        time.sleep(1)
        email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')

        email.send_keys(get_atr(email))
        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text



def test_1():
    assert fill_out_the_form(link1) == "Congratulations! You have successfully registered!"

def test_2():
    assert fill_out_the_form(link2) == "Congratulations! You have successfully registered!"


if __name__ == "__main__":
    pytest.main()