from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os


def main():
    try:
        # Настройка Chrome
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")

        # Автоматическая установка драйвера
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Открытие страницы
        driver.get("https://itcareerhub.de/ru")
        time.sleep(3)  # Даем время для полной загрузки

        # Находим блок по классу и data-атрибуту
        payment_block = driver.find_element(
            By.CSS_SELECTOR,
            "div.t396__filter[data-artboard-recid='860584261']"
        )

        # Прокрутка и визуальное выделение
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", payment_block)
        driver.execute_script("arguments[0].style.boxShadow='0 0 0 3px red';", payment_block)
        time.sleep(1)  # Ждем завершения анимации

        # Создаем папку для скриншотов
        os.makedirs('screenshots', exist_ok=True)

        # Делаем скриншот только нужного блока
        screenshot_path = os.path.join('screenshots', 'payment_methods_precise.png')
        payment_block.screenshot(screenshot_path)

        print(f"Точный скриншот блока сохранен: {screenshot_path}")

    except Exception as e:
        print(f"Ошибка: {str(e)}")
        print("Попробуйте:")
        print("1. Проверить интернет-соединение")
        print("2. Обновить Chrome: chrome://settings/help")
        print("3. Запустить скрипт снова")
    finally:
        if 'driver' in locals():
            driver.quit()


if __name__ == "__main__":
    main()