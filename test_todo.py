

def test_add_todo(browser):
    browser.goto("https://demo.playwright.dev/todomvc/#/")
    browser.get_by_placeholder("What needs to be done?").click()
    browser.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    browser.get_by_placeholder("What needs to be done?").press("Enter")
    browser.get_by_role("link", name="Completed").click()


def test_add_todo_with_locators(browser):
    browser.goto("https://demo.playwright.dev/todomvc/#/")
    browser.locator("#new-todo").click()
    browser.locator("//*[@id='new-todo']").click()
    # browser.locator("css=.first-class.another-class").click()
    # browser.locator("xpath=//div[contains(@class, 'first-class') and contains(@class, 'another-class')]").click()
