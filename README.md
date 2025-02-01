## Финальный проект 

### Описание 

<Ссылка на проект по ручному тестированию>

### Используемые библиотеки
- allure
- pytest
- requests
- selenium
- webdriver-manager

### Структура проекта
- **pages/**
    - **ApiClass.py** 
    - **MainPage.py**
- **tests/**
    - **test_api.py**
    - **test_ui.py**
- **README.md** 
- **requirements.txt** 
- **pytest.ini**
- **.gitignore**

### Инструкция по работе с проектом 
- Запуск тестов UI по команде: `pytest -v --alluredir=allure-results tests\test_ui.py`
- Генерация отчета по команде: `allure serve allure-results`
