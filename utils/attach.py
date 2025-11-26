import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

# def add_logs(browser):
#     log = "".join(f'{text}\n' for text in browser.driver.get_log("browser"))
#     allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')
#
#     # try:
#     #     logs = browser.driver.get_log('browser')
#     #     text = "\n".join([f"{l['level']}: {l['message']}" for l in logs])
#     #     allure.attach(text, "browser_logs", AttachmentType.TEXT, ".log")
#     # except Exception:
#     #     pass

def add_logs(browser):
    try:
        driver = browser.driver
        # Проверка наличия метода get_log
        if hasattr(driver, 'get_log'):
            logs = driver.get_log("browser")
            log_text = "".join(f'{entry["message"]}\n' for entry in logs)
            allure.attach(log_text, 'browser_logs', AttachmentType.TEXT)
        else:
            # Логи недоступны
            allure.attach("Логи не доступны для текущего драйвера", name="browser_logs", attachment_type=AttachmentType.TEXT)
    except Exception as e:
        print(f"Ошибка при получении логов: {e}")
        allure.attach(f"Произошла ошибка при получении логов: {e}", name="error_log", attachment_type=AttachmentType.TEXT)

def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'html', AttachmentType.HTML, '.html')

def add_video(browser):
    video_url = 'https://selenoid.autotests.cloud/video' + browser.driver.session_id + '.mp4'
    html = "<html><body><video width='100%' controls autoplay><source src='" \
    + video_url + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video' + browser.driver.session_id, AttachmentType.HTML, '.mp4')