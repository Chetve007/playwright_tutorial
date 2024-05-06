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
