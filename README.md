# **Tutorial**

1. Download reqs: `pip install playwright pytest pytest-playwright`
2. Download browsers: `playwright install` (if you want particular browser - `playwright install chrome`)
3. Launch codegen: `playwright codegen demo.playwright.dev/todomvc/#/` (Help - `playwright codegen --help`)
More popular comands:
- choose size of browser window: `playwright codegen --viewport-size=800,600 https://demo.playwright.dev/todomvc/#/`
- save script in file: `playwright codegen -o lesson.py https://demo.playwright.dev/todomvc/#/`

4. Main playwright commands:
- `pytest --headed --browser webkit --browser firefox` (--headed --browser)
- `pytest --browser-channel=msedge --headed`
- `pytest --slowmo 1000`
- `pytest --device="iPhone 13 Mini"`
- `--output` Каталог для артефактов, создаваемых тестами (по умолчанию: test-results).
- `--tracing` Записывать ли трассировку для каждого теста. on, off или retain-on-failure (по умолчанию: off)
- `--video` Записывать ли видео для каждого теста. on, off или retain-on-failure (по умолчанию: off)
- `--screenshot` Должен ли автоматически делаться снимок экрана после каждого теста. on, off или only-on-failure (по умолчанию: off)
- `--full-page-screenshot` - Следует ли делать скриншот всей страницы при ошибке. По умолчанию снимается только область просмотра. Требуется, чтобы параметр --screenshot был включен (по умолчанию: off)

5. Skip test by browser (pytest marks):
- `@pytest.mark.skip_browser("firefox")`
- `@pytest.mark.only_browser("chromium")`

6. Псевдоклассы CSS в Рlaywright (https://zimaev.github.io/table-1/)
- page.locator("td:right-of(td p:text('Software engineer'))")
- page.locator("td:left-of(td p:text('Software engineer'))")
- page.locator("td:above(td p:text('Consultant'))")
- page.locator("td:below(td p:text('Consultant'))")
- page.locator("td:near(td p:text('Consultant'))") - рядом (в пределах 50 CSS пикселей) с любым из элементов, соответствующих внутреннему селектору (button:near(:text("Username"), 120) соответствует кнопке, которая находится на расстоянии не более 120 пикселей)
- page.locator("td:below(td p:text('Software engineer'), 100)") - ниже в пределах 100 пикселей
- page.locator('button:has-text("Log in"), button:has-text("Sign in")').click() - элемент с тегом <button>, которая содержит текст "Log in" или "Sign in"
- page.locator("button").locator("nth=0").click() - сузить запрос до n-го совпадения, используя локатор nth= (Первый элемент)
- page.locator("button").locator("nth=-1").click() - Последний элемент
- page.locator("button:visible").click() - :visible, псевдокласс в CSS-селекторах для выбора видимого элемента
