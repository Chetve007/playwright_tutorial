import pytest


def test_loc(browser):
    browser.goto('https://zimaev.github.io/text_input/')
    browser.get_by_label("Email address").fill("qa@example.com")
    browser.get_by_title("username").fill("Anton")
    browser.get_by_placeholder('password').fill("secret")
    browser.get_by_role('checkbox').click()


def test_or(browser):
    """locator.or_ используется для поиска элемента, который соответствует хотя бы одному из заданных селекторов."""
    selector = browser.locator("input").or_(browser.locator("text"))
    selector.fill("Hello Stepik")


def test_locator_and(browser):
    """locator.and_ используется для поиска элемента, который соответствует всем заданным селекторам."""
    browser.goto("https://zimaev.github.io/locatorand/")
    selector = browser.get_by_role("button", name="Sing up").and_(browser.get_by_title("Sing up today"))
    selector.click()


def test_locator_chain(browser):
    browser.goto("https://zimaev.github.io/navbar/")
    browser.locator("#navbarNavDropdown >> li:has-text('Company')").click()
    # or
    # nav_bar = browser.locator('div#navbarNavDropdown')
    # nav_bar.locator("li:has-text('Company')").click()


def test_locator_filter(browser):
    """ Функция filter() принимает несколько аргументов:
        - has
        - has_not
        - has_text
        - has_not_text
    """
    browser.goto("https://zimaev.github.io/filter/")
    row_locator = browser.locator("tr")
    row_locator.filter(has_not=browser.get_by_role("button")).count()
    row_locator.filter(has_not_text="helicopter")

    # or можно комбинировать, пример:
    # row_locator = browser.locator("tr")
    # (row_locator
    #  .filter(has_text="text in column 1")
    #  .filter(has=browser.get_by_role("button", name="column 2 button"))
    #  .click())

    # количество элементов
    # row_locator = browser.locator("tr")
    # total = row_locator.filter(has_not=browser.get_by_role("button")).count()

    # browser.locator("li").filter(has_text='Company').click()
    # browser.locator('li').filter(has=browser.locator('.dropdown-toggle')).click()


@pytest.mark.parametrize('how', ('all', 'count'))
def test_locator_elements(browser, how):
    """Начиная с версии playwright 1.29 появился специализированный метод locator.all()
    для перебора всех совпадающих элементов.
    """
    browser.goto('https://zimaev.github.io/checks-radios/')
    checkboxes = browser.locator("input")
    match how:
        case 'all':
            [checkbox.check() for checkbox in checkboxes.all()]
        case 'count':
            [checkboxes.nth(ind).click() for ind in range(checkboxes.count())]


@pytest.mark.parametrize('action', ('fill', 'type'))
def test_check_input_data(browser, action):
    browser.goto('https://ya.ru/')
    locator = browser.get_by_placeholder('Найдётся всё')
    data = 'Саратов'
    if action == 'fill':
        locator.fill(data)
    else:
        locator.type(data)
    locator.press('Enter')
