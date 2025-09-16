from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
url = "http://suninjuly.github.io/alert_accept.html"

browser.get(url)
# Находим кнопку и кликаем
button = browser.find_element(By.CLASS_NAME, "btn-primary")
button.click()

# Переключаемся на алерт и жмём "ОК"
alert = browser.switch_to.alert
alert.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

 # Находим элемент с x и извлекаем его текст
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
# Вводим ответ в поле
input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(y)


browser.find_element(By.CLASS_NAME, "btn").click()

time.sleep(5)
