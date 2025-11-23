from selene import browser

from tests.demoqa.left_panel_element import LeftPanelElement
from tests.demoqa.simple_page import SimplePage


class Application:
    def __init__(self):
        self.left_panel = LeftPanelElement()
        self.simple_page = SimplePage()

    def open(self):
        browser.open("/")
        return self


app = Application()
