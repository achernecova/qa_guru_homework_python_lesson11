import allure
from allure_commons.types import Severity

from tests.demoqa.pages import users
from tests.demoqa.application import app
from tests.demoqa.pages.users import User

@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.feature("Успешная регистрация пользователя")
@allure.title("Заполнение формы с использованием appl manager")
@allure.link("https://github.com", name="Testing")
def test_registration_in_simple_form_with_app_manager():
    app.left_panel.open()
    app.simple_page.fill_full_name(users.first_user)

    # app.simple_page.should_have_simple_register(users.first_user)

@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.feature("Успешная регистрация пользователя")
@allure.title("Заполнение формы с использованием данных из дата-класса")
@allure.link("https://github.com", name="Testing")
def test_registration_in_simple_form_with_app_manager_with_user():
    app.left_panel.open()
    user = User(
        fullname="Alexandra",
        email="achernecova@inbox.ru",
        current_address="Москва",
        permanent_address="Москва",
    )
    app.simple_page.fill_full_name(user)
