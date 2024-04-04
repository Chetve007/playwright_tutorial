# **Tutorial**

1. Download reqs: `pip install playwright pytest pytest-playwright`
2. Download browsers: `playwright install` (if you want particular browser - `playwright install chrome`)
3. Launch codegen: `playwright codegen demo.playwright.dev/todomvc/#/` (Help - `playwright codegen --help`)
More popular comands:
- choose size of browser window: `playwright codegen --viewport-size=800,600 https://demo.playwright.dev/todomvc/#/`
- save script in file: `playwright codegen -o lesson.py https://demo.playwright.dev/todomvc/#/`