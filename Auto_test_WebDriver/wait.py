from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x: str) -> str:
    # Формула из известных задач Stepik
    return str(math.log(abs(12 * math.sin(int(x)))))

url = "http://suninjuly.github.io/explicit_wait2.html"

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get(url)

    # 1) Ждем, пока цена станет $100 (таймаут >= 12 сек)
    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2) Жмем на Book
    book_btn = driver.find_element(By.ID, "book")
    book_btn.click()

    # 3) Решаем задачу и отправляем
    # Иногда поле/кнопка ниже видимой области — скроллим к ним на всякий
    x_value = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "input_value"))
    ).text

    answer = calc(x_value)
    answer_input = driver.find_element(By.ID, "answer")
    driver.execute_script("arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(answer)

    solve_btn = driver.find_element(By.ID, "solve")
    driver.execute_script("arguments[0].scrollIntoView(true);", solve_btn)
    solve_btn.click()

    # (опционально) забираем код из алерта
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Ответ/код:", alert.text)
    alert.accept()

finally:
    driver.quit()
