from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    """
    Класс для работы с магазином.

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

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию.

        :param username: Имя пользователя.
        :param password: Пароль пользователя.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_items_to_cart(self) -> None:
        """
        Добавляет товары в корзину.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
        ).click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']").click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self) -> None:
        """
        Нажимает кнопку Checkout для оформления заказа.
        """
        self.driver.find_element(By.ID, "checkout").click()

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа.

        :param first_name: Имя пользователя.
        :param last_name: Фамилия пользователя.
        :param postal_code: Почтовый индекс.
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self) -> str:
        """
        Получает итоговую сумму заказа.

        :return: Итоговая сумма в виде строки.
        """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text.split("$")[-1]
