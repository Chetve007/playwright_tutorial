import pytest
from playwright.sync_api import expect


def test_contains_text(browser):
    browser.goto("https://zimaev.github.io/tabs/")
    expect(browser.get_by_text("Переход к Dashboard"), "Сообщение не отображается на странице").to_be_visible()


def test_not_contain_text(browser):
    browser.goto("https://zimaev.github.io/tabs/")
    with pytest.raises(AssertionError) as e:
        expect(browser.get_by_text("Тра-та-та"), "Сообщение не отображается на странице").to_be_visible()
    assert 'Сообщение не отображается на странице' in str(e.value)


def test_todo(browser):
    browser.goto('https://demo.playwright.dev/todomvc/#/')
    expect(browser).to_have_url("https://demo.playwright.dev/todomvc/#/")

    input_field = browser.get_by_placeholder('What needs to be done?')
    expect(input_field).to_be_empty()

    input_field.fill("Playwright forever")
    input_field.press('Enter')
    input_field.fill("Playwright better than Selenium ;)")
    input_field.press('Enter')
    todo_items = browser.get_by_test_id('todo-item')
    expect(todo_items).to_have_count(2)

    todo_items.get_by_role('checkbox').nth(0).click()
    expect(todo_items.nth(0)).to_have_class('completed')
