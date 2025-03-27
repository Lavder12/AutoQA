from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_image_loading():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    try:
        # Ждем загрузки всех изображений (ждем, когда исчезнет спиннер загрузки)
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "spinner"))
        )

        # Находим третье изображение и получаем его атрибут alt
        images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
        third_image_alt = images[2].get_attribute("alt")

        # Проверяем значение атрибута
        assert third_image_alt == "award", f"Атрибут alt третьего изображения не равен 'award'. Текущее значение: {third_image_alt}"
        print("Тест пройден: атрибут alt третьего изображения равен 'award'")

    finally:
        driver.quit()


test_image_loading()