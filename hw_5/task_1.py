import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_iframe_text(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    iframe = browser.find_element(By.ID, "my-iframe")
    browser.switch_to.frame(iframe)
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    expected_text = "semper posuere integer et senectus justo curabitur."
    found = any(expected_text in p.text for p in paragraphs)
    assert found, f"Текст '{expected_text}' не найден в iframe"
    print("\nТест пройден: текст найден в iframe")
