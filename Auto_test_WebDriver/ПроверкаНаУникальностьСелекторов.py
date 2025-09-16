from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Сайты для проверки
links = [
    "http://suninjuly.github.io/registration1.html",
    "http://suninjuly.github.io/registration2.html"
]

for link in links:
    print(f"\nПроверяем страницу: {link}")
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполнение обязательных полей (уникальные селекторы)
        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("ivan.petrov@mail.ru")

        # Клик по кнопке
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверка результата
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations! You have successfully registered!" == welcome_text

        print(f"✅ Тест пройден для: {link}")

    except Exception as e:
        print(f"❌ Тест упал для: {link}\nПричина: {e}")

    finally:
        time.sleep(3)
        browser.quit()
