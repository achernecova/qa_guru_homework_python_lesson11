from selene import browser
from selenium.webdriver.common.by import By

from tests.softmg.about_as_page import AboutCompany


class HeaderPanel:
    def __init__(self):
        self.element = browser.element("ul a[href='/about-company/']")
        self.elements_block = browser.element(
            (By.XPATH, "(//*[@class='group-header'])[1]")
        )
        self.text_box_in_submenu = browser.element("#item-0")

    def open(self):
        browser.open("https://softmg.ru/")
        self.open_page_about_as()


    def open_page_about_as(self):
        self.element.click()
        return AboutCompany


