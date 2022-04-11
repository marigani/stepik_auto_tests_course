from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
        
    input1 = browser.find_element_by_css_selector(".form-group [name = 'firstname']")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element_by_css_selector(".form-group [name = 'lastname']")
    input2.send_keys("Ivanov")

    input3 = browser.find_element_by_css_selector(".form-group [name = 'email']")
    input3.send_keys("Ivanov@ya.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'name_file.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".container button")
    button.click()

       

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла