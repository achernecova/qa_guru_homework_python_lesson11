from time import sleep

from selene import browser, have


class SimplePage:

    def fill_full_name(self, data_user_simple_form):
        browser.element("#userName").type(data_user_simple_form.fullname)
        browser.element("#userEmail").type(data_user_simple_form.email)
        browser.element("#currentAddress").type(data_user_simple_form.current_address)
        browser.element("#permanentAddress").type(data_user_simple_form.permanent_address)
        browser.element("#submit").click()
        self.should_have_simple_register(data_user_simple_form)
        sleep(5)

    def should_have_simple_register(self, data_user_simple_form):
        browser.element(".mb-1#name").should(
            have.exact_text(f"Name:{data_user_simple_form.fullname}")
        )
        browser.element(".mb-1#email").should(
            have.exact_text(f"Email:{data_user_simple_form.email}")
        )
        browser.element(".mb-1#currentAddress").should(
            have.text(f"Current Address :{data_user_simple_form.current_address}")
        )
        browser.element(".mb-1#permanentAddress").should(
            have.text(f"Permananet Address :{data_user_simple_form.permanent_address}")
        )
