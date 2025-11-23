from selene import browser, have


class CasesPage:

    @staticmethod
    def data_page():
        return browser.element('h1').should(have.exact_text('Кейсы'))