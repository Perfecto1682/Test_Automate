from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс для работы с страницей калькулятора.

    :param driver: WebDriver instance для управления браузером.
    """

    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str) -> None:
        """
        Открывает указанную страницу.

        :param url: URL страницы.
        """
        self.driver.get(url)

    def set_delay(self, delay: int) -> None:
        """
        Устанавливает задержку перед выполнением вычислений.

        :param delay: Значение задержки в секундах.
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "input[value='5']")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def calculate_sum(self) -> None:
        """
        Нажимает кнопки 7, +, 8 и = для выполнения вычислений.
        """
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(1)").click()  # Кнопка 7
        self.driver.find_element(By.CSS_SELECTOR, ".operator.btn.btn-outline-success").click()  # Кнопка +
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(2)").click()  # Кнопка 8
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning").click()  # Кнопка =

    def get_result(self) -> str:
        """
        Ожидает и возвращает результат вычислений.

        :return: Результат вычислений в виде строки.
        """
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
