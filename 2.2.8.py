from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # Проверяется, что поле required + поиск по placeholder
    input1 = browser.find_element_by_css_selector("[name=firstname]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[name=lastname]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[name=email]")
    input3.send_keys("IP@mail.ru")

    element = browser.find_element_by_css_selector("#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'Text1.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()