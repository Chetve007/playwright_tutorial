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
