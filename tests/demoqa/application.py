from selene import browser

from tests.demoqa.pages.left_panel_element import LeftPanelElement
from tests.demoqa.pages.simple_page import SimplePage


class Application:
    def __init__(self):
        self.left_panel = LeftPanelElement()
        self.simple_page = SimplePage()

    def open(self):
        browser.open("/")
        return self


app = Application()
