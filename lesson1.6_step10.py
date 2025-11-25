from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = 'https://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.TAG_NAME, 'input').send_keys("Ivan")
    browser.find_element(By.CLASS_NAME, "form-control.second").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "form-control.third").send_keys("my_mail@yandex.ru")

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
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()