from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.globalsqa.com/demo-site/draganddrop/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

photo = driver.find_element(By.XPATH, "//ul[@id='gallery']/li[1]")
trash = driver.find_element(By.ID, "trash")

actions = ActionChains(driver)
actions.drag_and_drop(photo, trash).perform()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='trash']/ul/li")))

photos_in_trash = len(driver.find_elements(By.XPATH, "//div[@id='trash']/ul/li"))
photos_in_gallery = len(driver.find_elements(By.XPATH, "//ul[@id='gallery']/li"))

assert photos_in_trash == 1, "Ошибка: В корзине нет фотографий!"
assert photos_in_gallery == 3, "Ошибка: В основной области осталось не 3 фотографии!"

print("Тест успешно пройден: Фотография перемещена в корзину, в галерее осталось 3 фотографии.")

driver.quit()
