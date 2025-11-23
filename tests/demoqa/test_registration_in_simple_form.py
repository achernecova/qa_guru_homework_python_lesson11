from tests.demoqa import users
from tests.demoqa.application import app
from tests.demoqa.users import User


def test_registration_in_simple_form_with_app_manager():
    app.left_panel.open()
    app.simple_page.fill_full_name(users.first_user)

    # app.simple_page.should_have_simple_register(users.first_user)


def test_registration_in_simple_form_with_app_manager_with_user():
    app.left_panel.open()
    user = User(
        fullname="Alexandra",
        email="achernecova@inbox.ru",
        current_address="Москва",
        permanent_address="Москва",
    )
    app.simple_page.fill_full_name(user)
