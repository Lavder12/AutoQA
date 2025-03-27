from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_button_text_change():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/textinput")

    try:
        # Находим поле ввода и вводим текст
        input_field = driver.find_element(By.ID, "newButtonName")
        input_field.send_keys("ITCH")

        # Находим кнопку и кликаем
        button = driver.find_element(By.ID, "updatingButton")
        button.click()

        # Проверяем, что текст кнопки изменился
        assert button.text == "ITCH", f"Текст кнопки не изменился на 'ITCH'. Текущий текст: {button.text}"
        print("Тест пройден: текст кнопки успешно изменился на 'ITCH'")

    finally:
        driver.quit()


test_button_text_change()