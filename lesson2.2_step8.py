import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

# данные для ввода
data = {'firstname': 'Вася', 'lastname': 'Пупкин', 'email': 'v_pupkin@.yandex.ru'}

# Создаём текстовый документ
# with open('lesson2.2_step8.txt', 'w', encoding='utf-8') as file:
#     text = f'Имя: {data['firstname']}\nФамилия: {data['lastname']}\nЭлектронная почта: {data['email']}'
#     file.write(text)

lst = ['firstname', 'lastname', 'email']
d = {}

# Открываем документ
with open('lesson2.2_step8.txt', 'r', encoding='utf-8') as file:
    for el in lst:
        line = file.readline().strip()
        d.setdefault(el, line.split()[-1])
    print(f'Словарь с данными для ввода {d}')

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/file_input.html')
    # time.sleep(1)
    browser.find_element(By.NAME, 'firstname').send_keys(d['firstname'])
    # time.sleep(1)
    browser.find_element(By.NAME, 'lastname').send_keys(d['lastname'])
    # time.sleep(1)
    browser.find_element(By.NAME, 'email').send_keys(d['email'])
    # time.sleep(2)
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'lesson2.2_step8.txt')  # добавляем к этому пути имя файла

    # element = browser.find_element(By.ID, "file") # поиск по id="file"
    element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')  # поиск по сс селектору
    element.send_keys(file_path)

    # browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click() # поиск по id='btn.btn-primary'
    # browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click() # поиск по сс селектору
    browser.find_element(By.TAG_NAME, 'button').click()  # поиск по тегу 'button'
    time.sleep(5)
    alert = browser.switch_to.alert
    print(f'Поздравляю, вы выполнили задание! Скопируйте этот код как ответ на тест Степика: {alert.text.split()[-1]}')
