import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("UI тесты")
class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть заданную страницу")
    def open_page(self, url):
        self._driver.get(url)

    @allure.step("Ввод фразы в поиск")
    def enter_search_name(self, name: str):
        search_input = self.wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "input[name=kp_query]")))
        search_input.clear()
        search_input.send_keys(name)

    @allure.step("Подтверждение поиска")
    def submit_search(self):
        search_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=submit]")))
        search_button.click()

    @allure.step("Получение списка фильмов по предварительному поиску")
    def get_search_preview_results(self):
        self.wait.until(
            EC.visibility_of_all_elements_located((
                By.CSS_SELECTOR, "h4.kinopoisk-header-suggest-item__title a")))
        film_links_titles = self._driver.find_elements(
            By.CSS_SELECTOR, "h4.kinopoisk-header-suggest-item__title a")
        return [film_title.text for film_title in film_links_titles]

    @allure.step("Выбор фильма")
    def select_film(self, film_id):
        film_by_id = self.wait.until(
            EC.element_to_be_clickable((By.ID, f"suggest-item-film-{film_id}")))
        film_by_id.click()

    @allure.step("Клип по кнопке 'Оценить фильм'")
    def click_rate_film(self):
        rate_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Оценить фильм']")))
        rate_button.click()

    @allure.step("Клип по кнопке 'Оценить фильм'")
    def rate_film(self, rating):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//button[contains(@aria-label, 'Оценка {rating}')]")))
        button.click()

    @allure.step("Получение рейтинга")
    def get_rating(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[@data-tid='5cb64c50']"))
        )
        return element.text

    @allure.step("Нажатие на кнопку 'Буду смотреть'")
    def click_watch_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Буду смотреть']"))
        )
        button.click()

    @allure.step("Поиск случайного фильма по жанру")
    def search_by_genre_random(self, genre: str):
        self._driver.find_element(By.ID, "genreListTitle").click()
        self._driver.find_element(
            By.CSS_SELECTOR, f"input[data-name='{genre}']").is_selected()
        self._driver.find_element(By.ID, "genreListTitle").click()
        self._driver.find_element(By.ID, "search").click()

    @allure.step("Получение названия произвольного фильма")
    def get_film_title(self):
        film_title_element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.filmName a"))
        )
        return film_title_element.text if film_title_element else None
