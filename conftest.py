import allure
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    with allure.step("Открытие браузера"):
        driver = webdriver.Chrome()
        yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()