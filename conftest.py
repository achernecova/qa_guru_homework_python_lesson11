# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# @pytest.fixture(scope='function')
# def setup_browser():
#     options = Options()
#
#     options.set_capability("browserName", "chrome")
#     options.set_capability("browserVersion", "128.0")
#     options.set_capability("selenoid:options", {
#         "enableVNC": True,
#         "enableVideo": True
#     })
#
#     driver = webdriver.Remote(
#         command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=options
#     )
#
#     yield driver
#
#     driver.quit()


import pytest
from allure_commons._allure import attach
from selene import browser
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    options = ChromeOptions()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.add_argument("--window-size=1920,1080")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    browser.config.driver_remote_url = "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    browser.config.driver_options = options
    browser.config.timeout = 6

    yield

    # аттачи
    attach.add_screenshot(browser.driver)
    attach.add_logs(browser.driver)
    attach.add_video(browser.driver)
    attach.add_html(browser.driver)

    browser.quit()

# import pytest
# from selene import browser
# from selenium.webdriver.chrome.options import Options as ChromeOptions
#
#
# @pytest.fixture(scope="function", autouse=True)
# def setup_browser():
#     options = ChromeOptions()
#     options.set_capability("browserName", "chrome")
#     options.set_capability("browserVersion", "128.0")
#     options.set_capability(
#         "selenoid:options",
#         {
#             "enableVNC": True,
#             "enableVideo": True,
#             "screenResolution": "1920x1080x24",
#         },
#     )
#
#     browser.config.driver_remote_url = "http://localhost:4444/wd/hub"
#     browser.config.driver_options = options
#     browser.config.base_url = "https://demoqa.com"
#     browser.config.timeout = 6
#
#     yield
#     browser.quit()