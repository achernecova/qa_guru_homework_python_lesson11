import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    options = ChromeOptions()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    browser.config.driver_remote_url = "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    browser.config.driver_options = options
    browser.config.timeout = 6

    yield

    browser.quit()
    # аттачи
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # # attach.add_video(browser)
    # attach.add_html(browser)
