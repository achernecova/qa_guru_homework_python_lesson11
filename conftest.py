
import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options as ChromeOptions

from utils import attach


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    options = ChromeOptions()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.add_argument("--window-size=1280,900")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })
    options.set_capability("goog:loggingPrefs", {'browser': 'ALL'})  # Включаем логирование браузера

    browser.config.driver_remote_url = "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    browser.config.driver_options = options
    browser.config.timeout = 6

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)

    browser.quit()