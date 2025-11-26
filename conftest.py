import os

import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from dotenv import load_dotenv
from utils import attach

@pytest.fixture(scope="function", autouse=True)
def load_env():
    load_dotenv()

selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")

@pytest.fixture(scope="function", autouse=True)
def setup_browser(browser):
    options = ChromeOptions()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.add_argument("--window-size=1280,900")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })
    # Включение логов браузера
    options.set_capability("goog:loggingPrefs", {'browser': 'ALL'})

    # Укажите URL удаленного WebDriver (Selenoid)
    browser.config.driver_remote_url = "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    browser.config.driver_options = options
    browser.config.timeout = 6

    yield

    # После каждого теста
    browser.driver.maximize_window()
    attach.add_screenshot(browser)
    attach.add_logs(browser)  # Здесь вызов с обработкой поддержки логов
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
