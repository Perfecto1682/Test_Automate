from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # Подключаем менеджер драйвера

# Запуск веб-драйвера с использованием Service и ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Явное ожидание и клик по кнопке "Add Element" 5 раз
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']"))
    )

    for _ in range(5):
        add_button.click()

    # Ожидание появления всех кнопок "Delete" и сбор их в список
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "added-manually"))
    )
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

    # Вывод количества кнопок "Delete"
    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

finally:
    # Закрытие браузера
    driver.quit()
