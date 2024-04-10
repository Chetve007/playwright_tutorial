

def test_loc(browser):
    browser.goto('https://zimaev.github.io/text_input/')
    browser.get_by_label("Email address").fill("qa@example.com")
    browser.get_by_title("username").fill("Anton")
    browser.get_by_placeholder('password').fill("secret")
    browser.get_by_role('checkbox').click()
