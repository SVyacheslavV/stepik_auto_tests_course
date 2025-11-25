import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


with webdriver.Chrome() as browser:
    # browser.get('https://suninjuly.github.io/selects1.html')
    browser.get('https://suninjuly.github.io/selects2.html')
    x = int(browser.find_element(By.ID, 'num1').text)
    y = int(browser.find_element(By.ID, 'num2').text)

    # elements = browser.find_element(By.TAG_NAME, 'h2').find_elements(By.TAG_NAME, 'span')
    # num = eval(f'{elements[1].text} {elements[2].text} {elements[3].text}')
    num = sum((x, y))
    box = browser.find_element(By.ID, 'dropdown')
    box.click()
    select = Select(browser.find_element(By.CSS_SELECTOR,"select"))
    select.select_by_value(str(num))
    
    # без использования select
    # numbers = box.find_elements(By.TAG_NAME, 'option')
    # for n in numbers:
    #     if n.text == str(num):
    #         n.click()
    #         break

    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()
    time.sleep(2)
    alert = browser.switch_to.alert
    print(f'Поздравляю, вы выполнили задание! Скопируйте этот код как ответ на тест Степика: {alert.text.split()[-1]}')