# сама панель - поиск css по классу .left-pannel
# бургер Element (//*[@class='group-header'])[1]

from selene import browser
from selenium.webdriver.common.by import By

from tests.demoqa.simple_page import SimplePage


# Нашли левую панель.
# Клик по бургеру - Element.
# Клик в Text Box - id = item-0
# Вернуть страницу с Text Box


class LeftPanelElement:
    def __init__(self):
        self.element = browser.element(".left-pannel")
        self.elements_block = browser.element(
            (By.XPATH, "(//*[@class='group-header'])[1]")
        )
        self.text_box_in_submenu = browser.element("#item-0")

    def open(self):
        browser.open("https://demoqa.com/forms")
        self.open_page_elements_text_box()

    def open_page_elements_text_box(self):
        self.element.click()
        self.elements_block.click()
        self.text_box_in_submenu.click()
        return SimplePage
