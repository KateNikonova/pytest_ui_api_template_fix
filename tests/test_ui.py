import allure
import pytest
from pages.MainPage import MainPage
from config import *


@allure.epic("UI тесты")
@allure.title("Поиск фильмов по названию")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется , что введённое значение есть в названии первого фильма")
@allure.severity("Critical")
@pytest.mark.parametrize("film_title", ["Король Лев", "Титаник", "Зеленая миля"])
@pytest.mark.positive
@pytest.mark.smoke
def test_fast_search_by_film_title(browser, film_title):
    with allure.step("Переход на главную страницу)"):
        main_page = MainPage(browser)
        main_page.open_page(base_url)

    with allure.step("Ввод названия фильма в поисковую строку"):
        main_page.enter_search_name(film_title)

    with allure.step("Получить название фильмы"):
        list_elements = main_page.get_search_preview_results()

    with allure.step("Проверить, что введённое значение есть в названии первого фильма"):
        assert film_title in list_elements, f"Ожидалось, что фильм {film_title} будет в результатах поиска"


@allure.epic("UI тесты")
@allure.title("Поиск фильмов по жанру")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется")
@allure.severity("Critical")
@pytest.mark.parametrize("film_genre", ["комедия", "аниме", "музыка"])
@pytest.mark.positive
@pytest.mark.smoke
def test_search_for_genre(browser, film_genre):
    with allure.step("Переход на главную страницу)"):
        main_page = MainPage(browser)
        main_page.open_page(base_url)

    with allure.step("В поисковой строке нажатие на 'поиск'"):
        main_page.submit_search()

    with allure.step("В поисковой строке нажатие на 'поиск'"):
        main_page.search_by_genre_random(film_genre)
        film_title = main_page.get_film_title()
        assert film_title, "Название фильма пустое!"


# Оценить фильм:
@allure.epic("UI тесты")
@allure.title("Оценка фильма")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется")
@allure.severity("Critical")
@pytest.mark.parametrize("film_title, film_id, rating", [("Век Адалин", 522876, 10)])
@pytest.mark.positive
def test_rate_film(browser, film_title, film_id, rating):
    with allure.step("Переход на главную страницу)"):
        main_page = MainPage(browser)
        main_page.open_page(base_url)

# 1. Ввести название фильма "Век Адалин"
    with allure.step("Ввод названия фильма в поисковую строку"):
        main_page.enter_search_name(film_title)

# 2. Провалиться в найденный фильм.
    with allure.step("Клик по первому названию"):
        main_page.select_film(film_id)

# 3. Нажать кнопку оценить фильм.
    with allure.step("Нажать на 'Оценить фильм'"):
        main_page.click_rate_film()

# 4. Выбрать 10
    with allure.step("Оценить фильм"):
        main_page.rate_film(rating)

# 5. Проверить, что оценка 10
    with allure.step("Проверка рейтинга"):
        rating = main_page.get_rating()
        assert rating == 10, f"Ожидалось, что рейтинг будет 10, но получено: {rating}"



# Добавить фильм в "буду смотреть".
@allure.epic("UI тесты")
@allure.title("Добавить фильм в ' Буду смотреть'")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется")
@allure.severity("Critical")
@pytest.mark.parametrize("film_title, film_id", [("Фантомас", 47984)])
@pytest.mark.positive
def test_rate_film(browser, film_title, film_id):
    with allure.step("Переход на главную страницу)"):
        main_page = MainPage(browser)
        main_page.open_page(base_url)

# 1. Ввести название фильма "Фантомас"
    with allure.step("Ввод названия фильма в поисковую строку"):
        main_page.enter_search_name(film_title)

# 2. Провалиться в найденный фильм.
    with allure.step("Клик по первому названию"):
        main_page.select_film(film_id)

# 3 Нажать на кнопку буду смотреть.
    with allure.step("Клик на кнопку '+ Буду смотреть'"):
        main_page.click_watch_button()

# Проверить добавлен ли фильм в папку
    with allure.step("Переход на страницу с папками"):
        main_page.open_page(folder_url)


# Удалить фильм с папки  "буду смотреть ".
# 1.На своей странице навести на иконку с фото профиля, нажать на "Фильмы".
# 2. В папке " буду смотреть " поставить галочку (выбрать фильм).
# 3. Нажать удалить.
# 4. Проверить, что фильм удалён  или в этой папке нет фильма с таким названием.