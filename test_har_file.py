from playwright.sync_api import expect


def test_replace_from_har(browser):
    browser.goto("https://reqres.in/")
    browser.route_from_har("example.har")
    users_single = browser.locator('li[data-id="users-single"]')
    users_single.click()
    response = browser.locator('[data-key="output-response"]')
    expect(response).to_contain_text("chetverikov")
