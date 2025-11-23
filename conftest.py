import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope="function")
def setup_browser():
    chrome_options = Options()
    chrome_options.set_capability("browserName", "chrome")
    chrome_options.set_capability("browserVersion", "128.0")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })
    driver = webdriver.Chrome(options=chrome_options)
    # Передаем драйвер в Selene
    browser.config.driver = driver

    browser.config.driver_remote_url = "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    browser.config.driver_options = chrome_options
    browser.config.timeout = 6

    yield driver

    # аттачи
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    # attach.add_video(browser)
    attach.add_html(browser)

    browser.quit()

