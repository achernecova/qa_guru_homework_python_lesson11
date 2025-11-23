from selene import browser, have


class AboutCompany:

    @staticmethod
    def data_page():
        return browser.element('h1').should(have.exact_text('О компании Soft Media Group'))
