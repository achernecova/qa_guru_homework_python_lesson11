from tests.softmg.about_as_page import AboutCompany
from tests.softmg.header_panel import HeaderPanel


def test_open_page_softmg():
    page = HeaderPanel()
    page.open()
    page.open_page_about_as()
    page_about = AboutCompany()
    page_about.data_page()