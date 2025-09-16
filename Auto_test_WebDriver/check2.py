from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/get_attribute.html"
chrome = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    chrome.get(link)
    x_element = chrome.find_element(By.ID, "treasure")
    valuex = x_element.get_attribute("valuex")
    x = valuex
    y = calc(x)
    chrome.find_element(By.ID, "answer").send_keys(y) 
    chrome.find_element(By.ID, "robotCheckbox").click()
    chrome.find_element(By.ID, "robotsRule").click()
    time.sleep(2)
    chrome.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(10)
    chrome.quit()




