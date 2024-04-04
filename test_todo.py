

def test_add_todo(browser) -> None:
    browser.goto("https://demo.playwright.dev/todomvc/#/")
    browser.get_by_placeholder("What needs to be done?").click()
    browser.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    browser.get_by_placeholder("What needs to be done?").press("Enter")
    browser.get_by_role("link", name="Completed").click()
