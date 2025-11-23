import pytest
from allure_commons._allure import attach
from selene import browser
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach


@pytest.fixture(scope="function")
def setup_browser():
    options = ChromeOptions()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    # options.add_argument("--window-size=1920,1080")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    browser.config.driver_remote_url = "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.driver_options = options
    browser.config.timeout = 6

    yield

    # аттачи
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # # attach.add_video(browser)
    # attach.add_html(browser)

    browser.quit()