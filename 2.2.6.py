from selenium import webdriver
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    # Проверяется, что поле required + поиск по placeholder
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    checkbox1 = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox1.click()
    radiobutton1 = browser.find_element_by_css_selector("#robotsRule")
    radiobutton1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()