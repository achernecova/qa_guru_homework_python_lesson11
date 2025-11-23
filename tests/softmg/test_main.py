import allure
from allure_commons.types import Severity

from tests.softmg.about_as_page import AboutCompany
from tests.softmg.cases_page import CasesPage
from tests.softmg.contact_page import ContactPage
from tests.softmg.header_panel import HeaderPanel

@allure.tag("normal")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "chernetsova")
@allure.feature("Работоспособность меню")
@allure.story("Корректный переход на страницу О Компании")
@allure.link("https://softmg.ru/", name="Testing")
def test_open_page_softmg_about():

    with allure.step("Открываем главную страницу сайта softmg"):
        page = HeaderPanel()
        page.open()
    with allure.step("В меню переходим по пункту О компании"):
        page.open_page_about_as()
        page_about = AboutCompany()
    with allure.step("Проверяем, что мы находимся на нужной странице - заголовок соответствует заданному"):
        page_about.data_page()

@allure.tag("normal")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "chernetsova")
@allure.feature("Работоспособность меню")
@allure.story("Корректный переход на страницу Контакты")
@allure.link("https://softmg.ru/", name="Testing")
def test_open_page_softmg_contact():

    with allure.step("Открываем главную страницу сайта softmg"):
        page = HeaderPanel()
        page.open()
    with allure.step("В меню переходим по пункту Контакты"):
        page.open_page_contact()
        page_contact = ContactPage()
    with allure.step("Проверяем, что мы находимся на нужной странице - заголовок соответствует заданному"):
        page_contact.data_page()

@allure.tag("normal")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "chernetsova")
@allure.feature("Работоспособность меню")
@allure.story("Корректный переход на страницу Кейсы")
@allure.link("https://softmg.ru/", name="Testing")
def test_open_page_softmg_cases():

    with allure.step("Открываем главную страницу сайта softmg"):
        page = HeaderPanel()
        page.open()
    with allure.step("В меню переходим по пункту Кейсы"):
        page.open_page_cases()
        page_cases = CasesPage()
    with allure.step("Проверяем, что мы находимся на нужной странице - заголовок соответствует заданному"):
        page_cases.data_page()