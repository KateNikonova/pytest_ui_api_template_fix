import allure
import pytest
from selenium import webdriver
from pages.MainPage import MainPage


@allure.epic("UI тесты")
@allure.title("Поиск фильмов по названию")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется , что введённое значение есть в названии первого фильма")
@allure.severity("Critical")
@pytest.mark.parametrize("film_title", ["Король Лев", "Титаник", "Зеленая миля"])
def test_positive_search_for_name(film_title):
    with allure.step("Открытие сайта(переход на главную страницу)"):
        driver = webdriver.Chrome()
        main_page = MainPage(driver)
        main_page.open_form()

    with allure.step("Ввод названия фильма в поисковую строку"):
        main_page.enter_search_name(film_title)

    with allure.step("Получить название фильмы"):
        list_elements = main_page.get_search_preview_results()

    with allure.step("Проверить, что введённое значение есть в названии первого фильма"):
        assert film_title in list_elements

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.epic("UI тесты")
@allure.title("Поиск фильмов по жанру")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется")
@allure.severity("Critical")
@pytest.mark.parametrize("film_genre", ["комедия", "аниме", "музыка"])
def test_positive_search_for_genre(film_genre):
    with allure.step("Открытие сайта(переход на главную страницу)"):
        driver = webdriver.Chrome()
        main_page = MainPage(driver)
        main_page.open_form()

    with allure.step("В поисковой строке нажатие на 'поиск'"):
        main_page.submit_search()

    with allure.step("В поисковой строке нажатие на 'поиск'"):
        main_page.search_by_genre_random(film_genre)
        film_title = main_page.get_film_title()
        assert film_title, "Название фильма пустое!"

    with allure.step("Закрыть браузер"):
        driver.quit()
