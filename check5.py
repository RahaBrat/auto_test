from selenium import webdriver
from selenium.webdriver.common.by import By 
import os
import time
from faker import Faker

fake = Faker()
url = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
try:
    browser.get(url)
#Вставляем в поле рандомные значения 
    inputs = browser.find_elements(By.CSS_SELECTOR, ".form-group input")
    answers = [fake.first_name(), fake.last_name(), fake.email()]

    for field, answer in zip(inputs, answers):
        field.send_keys(answer)

#добавляем файл
    file_path = os.path.abspath("file.txt")
    upload = browser.find_element(By.ID, "file")
    upload.send_keys(file_path) 
#нажимаем на кнопку 
    browser.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(15)
    browser.quit()