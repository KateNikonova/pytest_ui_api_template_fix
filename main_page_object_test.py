import allure
from selenium import webdriver
from pytest_ui_api_template.MainPage import MainPage


@allure.epic("UI тесты")
@allure.title("Поиск фильмов по названию")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется , что введённое значение есть в названии первого фильма")
@allure.severity("Critical")
def test_positive_search_for_name():
    with allure.step("Открытие сайта(переход на главную страницу)"):
        driver = webdriver.Chrome()
        main_page = MainPage(driver)
        main_page.open_form()

    with allure.step("Ввод названия фильма в поисковую строку"):
        name = "Король лев"
        main_page.enter_search_name(name)

    with allure.step("Получить название первого фильма"):
        list_elements = main_page.get_elements_result()
        name_1 = list_elements[0].text
        allure.attach(name_1, "Название первого фильма")

    with allure.step("Проверить , что введённое значение есть в названии первого фильма"):
        assert name.lower() in name_1.lower()

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.epic("UI тесты")
@allure.title("Поиск фильмов по жанру")
@allure.feature("Позитивные проверки")
@allure.description("В результате проверяется")
@allure.severity("Critical")
def test_positive_search_for_genre():
    with allure.step("Открытие сайта(переход на главную страницу)"):
        driver = webdriver.Chrome()
        main_page = MainPage(driver)
        main_page.open_form()

    with allure.step("В поисковой строке нажатие на 'поиск'"):
        main_page.submit_search()

    with allure.step("В поисковой строке нажатие на 'поиск'"):
        main_page.search_by_genre_random()
        print(main_page.get_film_name)












