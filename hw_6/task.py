import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):  # <-- добавляем request
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        request.cls.driver = driver  # Привязываем driver к классу
        request.cls.login_page = LoginPage(driver)
        request.cls.inventory_page = InventoryPage(driver)
        request.cls.cart_page = CartPage(driver)
        request.cls.checkout_page = CheckoutPage(driver)

        yield
        driver.quit()

    def test_checkout_total_price(self):
        self.login_page.success_login("standard_user", "secret_sauce")

        self.inventory_page.add_item_to_cart("Sauce Labs Backpack")
        self.inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        self.inventory_page.add_item_to_cart("Sauce Labs Onesie")

        self.inventory_page.go_to_cart()

        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_checkout_form("John", "Doe", "12345")

        total_price = self.checkout_page.get_total_price()
        assert total_price == "$58.29", f"Итоговая сумма неверна: {total_price}"
