from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "https://suninjuly.github.io/math.html"
chrome = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    chrome.get(link)
    # Находим элемент с x и извлекаем его текст
    x_element = chrome.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # Вводим ответ в поле
    input_field = chrome.find_element(By.ID, "answer")
    input_field.send_keys(y)
    chrome.find_element(By.ID, "robotCheckbox").click()
    chrome.find_element(By.ID, "robotsRule").click()
    chrome.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(30)
    chrome.quit()
