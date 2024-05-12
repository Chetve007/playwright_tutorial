import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser():
    """
    Данную фикстуру можно заменить:
    Аддон pytest-playwright реализует несколько фикстур.
    Наиболее широко используемой из которых является фикстура - "page".
    Фикстура page предоставляет новую веб-страницу для запуска теста и функции для работы с ней.
    По умолчанию pytest-playwright делает браузер headless(безголовым).
    Если вы хотите выполнить в режиме headed, передайте параметр - `pytest --headed`
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)  # channel="msedge or chrome",
        context = browser.new_context()  # создает изолированный сеанс браузера (viewport={"width": 800, "height": 600})
        context.tracing.start(screenshots=True, snapshots=True)  # for tracing
        page = context.new_page()
        yield page
        context.tracing.stop(path="trace.zip")  # for tracing
        context.storage_state(path="storage_state")
        page.close()
        context.close()
        browser.close()


# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     """Работает только с фикстурами pytest-playwright. При этом надо удалить свою фикстуру 'browser'"""
#     return {
#         **browser_context_args,
#         "storage_state": {
#             "cookies": [
#                 {
#                     "name": "stepik",
#                     "value": "sd4fFfv!x_cfcstepik",
#                     "url": "https://example.com"  # Замените на нужный URL
#                 },
#             ]
#         },
#         "viewport": {
#             "width": 720,
#             "height": 480
#         }
#     }
