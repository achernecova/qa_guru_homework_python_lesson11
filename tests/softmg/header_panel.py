from selene import browser
from selenium.webdriver.common.by import By

from tests.softmg.about_as_page import AboutCompany
from tests.softmg.cases_page import CasesPage
from tests.softmg.contact_page import ContactPage


class HeaderPanel:
    def __init__(self):
        self.element_about = browser.element("ul a[href='/about-company/']")
        self.element_contact = browser.element("ul a[href='/contacts/']")
        self.element_cases = browser.element("ul a[href='/examples/']")
        self.elements_block = browser.element(
            (By.XPATH, "(//*[@class='group-header'])[1]")
        )
        self.text_box_in_submenu = browser.element("#item-0")

    def open(self):
        browser.open("https://softmg.ru/")
        self.open_page_about_as()


    def open_page_about_as(self):
        self.element_about.click()
        return AboutCompany

    def open_page_contact(self):
        self.element_contact.click()
        return ContactPage

    def open_page_cases(self):
        self.element_cases.click()
        return CasesPage


