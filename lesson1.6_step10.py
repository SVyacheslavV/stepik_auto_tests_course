from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# данные пользователя которые будем вводить
data = {'first name': 'Ivan', 'last name': 'Petrov', 'email': 'my_mail@yandex.ru'}

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = 'https://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # labels_tag = browser.find_elements(By.TAG_NAME, 'label')
    # input_tag = browser.find_elements(By.TAG_NAME, 'input')
    # for ind, label in enumerate(labels_tag):
    #     value = label.text
    #     if value[-1] == '*':
    #         v = value[:-1]
    #         input_tag[ind].send_keys(data[v])


    first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    text = first_name.get_attribute('placeholder')
    key = [text.split()[-1], ' '.join(text.split()[-2:])][text.split()[-1] == 'name']
    print(f'{key}: {data[key]}')
    first_name.send_keys(data[key])
    time.sleep(1)
    last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    text = last_name.get_attribute('placeholder')
    key = [text.split()[-1], ' '.join(text.split()[-2:])][text.split()[-1] == 'name']
    print(f'{key}: {data[key]}')
    last_name.send_keys(data[key])
    time.sleep(1)
    email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    text = email.get_attribute('placeholder')
    key = [text.split()[-1], ' '.join(text.split()[-2:])][text.split()[-1] == 'name']
    print(f'{key}: {data[key]}')
    email.send_keys(data[key])
    time.sleep(1)


    # browser.find_element(By.ID, "country").send_keys("Russia")

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

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    print(welcome_text_elt.text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()