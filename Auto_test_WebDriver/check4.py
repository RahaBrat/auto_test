from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(url)
    # Находим элемент с x и извлекаем его текст
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # Вводим ответ в поле
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);") 
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, "btn").click()
finally:
  time.sleep(10)