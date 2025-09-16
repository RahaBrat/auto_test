from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# функция для вычисления
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

# 1. Жмем кнопку
browser.find_element(By.CLASS_NAME, "trollface").click()

# 2. Переключаемся на новую вкладку
new_window = browser.window_handles[1]   # вторая вкладка
browser.switch_to.window(new_window)

# 3. Считываем x
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
result = calc(x)

# 4. Вводим ответ
browser.find_element(By.ID, "answer").send_keys(result)

# 5. Отправляем форму
browser.find_element(By.CLASS_NAME, "btn-primary").click()

time.sleep(5)  # чтобы увидеть результат
browser.quit()