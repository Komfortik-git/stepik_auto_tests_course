#browser.switch_to.window(window_name)
#Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

#new_window = browser.window_handles[1]
#Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

#first_window = browser.window_handles[0]
#После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def test_function():
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        time.sleep(3)
        submit = browser.find_element (By.CSS_SELECTOR,'button[type="submit"]')
        submit.click()
        #Получаем имя первой вкладки(старого окна)
        original_window = browser.current_window_handle
        #Поулчаем список вссех открытых окон
        all_windows = browser.window_handles
        # Новое окно будет вторым в списке(индексы начинаются с нуля)
        new_window = [w for w in all_windows if w != original_window][0]
        #Переключаемся на новое окно
        browser.switch_to.window(new_window)


        x_element = browser.find_element(By.ID, 'input_value')
        x=x_element.text
        print(x)
        result=calc(x)

        print(result)
        input1 = browser.find_element(By.ID, 'answer')
        input1.send_keys(result)

        submit = browser.find_element (By.CSS_SELECTOR,'button[type="submit"]')
        submit.click()
        time.sleep(5)


    finally:
        browser.quit()
