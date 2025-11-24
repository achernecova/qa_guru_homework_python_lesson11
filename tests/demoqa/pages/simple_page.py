from time import sleep

import allure
from selene import browser, have


class SimplePage:

    def fill_full_name(self, data_user_simple_form):
        with allure.step("Заполнили поле UserName"):
            browser.element("#userName").type(data_user_simple_form.fullname)
        with allure.step("Заполнили поле email"):
            browser.element("#userEmail").type(data_user_simple_form.email)
        with allure.step("Заполнили поле с текущим адресом"):
            browser.element("#currentAddress").type(data_user_simple_form.current_address)
        with allure.step("Заполнили поле с адресом регистрации"):
            browser.element("#permanentAddress").type(data_user_simple_form.permanent_address)
        with allure.step("Нажали кнопку регистрации"):
            browser.element("#submit").click()
        self.should_have_simple_register(data_user_simple_form)
        sleep(5)

    def should_have_simple_register(self, data_user_simple_form):
        with allure.step("Проверили имя"):
            browser.element(".mb-1#name").should(
                have.exact_text(f"Name:{data_user_simple_form.fullname}")
            )
        with allure.step("Проверили email"):
            browser.element(".mb-1#email").should(
                have.exact_text(f"Email:{data_user_simple_form.email}")
            )
        with allure.step("Проверили текущий адрес"):
            browser.element(".mb-1#currentAddress").should(
                have.text(f"Current Address :{data_user_simple_form.current_address}")
            )
        with allure.step("Проверили адрес регистрации"):
            browser.element(".mb-1#permanentAddress").should(
                have.text(f"Permananet Address :{data_user_simple_form.permanent_address}")
            )
