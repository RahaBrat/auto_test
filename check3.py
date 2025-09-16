from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()


try:
    browser.get(url)
    num1 = browser.find_element(By.ID, "num1").text 
    num2 = browser.find_element(By.ID, "num2").text
    result = str(int(num1) + int(num2))
    dropdown = Select(browser.find_element(By.ID, "dropdown"))
    dropdown.select_by_value(result)


    browser.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(5)