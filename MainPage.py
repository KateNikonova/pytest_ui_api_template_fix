import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException

@allure.epic("UI тесты")
class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие формы(переход на страницу)")
    def open_form(self):
        self._driver.get("https://www.kinopoisk.ru")

    @allure.step("Ввод фразы в поиск")
    def enter_search_name(self, name: str):
        elem_input = self._driver.find_element(By.CSS_SELECTOR, "input[name=kp_query]")
        elem_input.clear()
        elem_input.send_keys(name)

    def submit_search(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    def get_elements_result(self):
        elements = self._driver.find_element(By.CSS_SELECTOR, "")
        return elements

    @allure.step("Поиск фильмов по жанру")
    def search_by_genre_random(self):
        self._driver.find_element(By.ID, "genreListTitle").click()
        self._driver.find_element(By.CSS_SELECTOR, "input[data-name='история']").is_selected()
        self._driver.find_element(By.ID, "genreListTitle").click()
        self._driver.find_element(By.ID,"search").click()

    def get_film_name(self):
        return self._driver.find_element(By.CSS_SELECTOR, ".filmName > span").getText()











