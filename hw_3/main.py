import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestITCareerHub:

    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://itcareerhub.de/ru")
        yield
        self.driver.quit()

    def test_elements_displayed(self):
        assert self.driver.find_element(By.CSS_SELECTOR, "img[alt='ITCareerHub']").is_displayed()
        assert self.driver.find_element(By.LINK_TEXT, "Программы").is_displayed()
        assert self.driver.find_element(By.LINK_TEXT, "Способы оплаты").is_displayed()
        assert self.driver.find_element(By.LINK_TEXT, "Новости").is_displayed()
        assert self.driver.find_element(By.LINK_TEXT, "О нас").is_displayed()
        assert self.driver.find_element(By.LINK_TEXT, "Отзывы").is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, "button[lang='ru']").is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, "button[lang='de']").is_displayed()

    def test_click_phone_icon_and_check_text(self):
        phone_icon = self.driver.find_element(By.CSS_SELECTOR, ".phone-icon")
        phone_icon.click()
        assert "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами" in self.driver.page_source
