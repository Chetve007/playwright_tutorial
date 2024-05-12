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

7. Если у вас есть список одинаковых элементов, и единственным способом различить их является порядок,
вы можете выбрать конкретный элемент из списка с помощью `locator.first`, `locator.last` или `locator.nth(index)`.
Если вам необходимо узнать количество элементов, соответствующих указанному селектору - используйте метод `count()`. Пример:
``page.get_by_role("button").count()``

8. Playwright поставляется со встроенными механизмами ожидания
Attached - элемент присоединен к DOM. Элемент считается прикрепленным, если он подключен к DOM или ShadowRoot.
Editable - элемент редактируемый. Элемент считается редактируемым, если он включен и у него не установлено свойство "read only".
Enabled - элемент включен. Считается включенным, если у тегов button, select, input, textare не имеют свойства disabled.
Receive Events - получает события, не заслоняемые другими элементами.
Stable - элемент стабилен. Элемент считается стабильным, если он сохраняет ту же  область после двух или более последовательных кадров анимации.
Visible -  элемент является видимым.

Явное ожидание элемента: `page.wait_for_selector()`

9. Ввод текста и клик
- `locator.click(**kwargs)`
`click(button='right')` - <"левая"|"правая"|"средняя">
`сlick(force=True)` - обходить проверки на возможность действия.
- `locator.fill(текст, **kwargs)`
пример - `page.locator("#exampleInputEmail1").fill("admin@example.com")`
- `locator.type(текст, **kwargs)` - В отличие от  fill(), метод type() передает данные посимвольно.
пример - `page.locator("#exampleInputEmail1").type("admin@example.com")`
- `locator.press(key, **kwargs)` - Функциональные клавиши(F1 - F12, Backspace, Tab, Delete, Escape, ArrowDown, End, Enter, Home, Insert, PageDown, PageUp, ArrowRight, ArrowUp и так далее.)

10. PWDEBUG и Playwright Inspector
Чтобы запустить тест в  Playwright Inspector в режиме дебаг, вам необходимо указать перед тестовой командой префикс PWDEBUG=1
``` bash
PWDEBUG=1 pytest -k 'test_todo'
```
``` powershell
$env:PWDEBUG=1
pytest -k 'test_todo'
```

Chrome DevTools
Playwright позволяет вам выделять селекторы в консоли браузера с помощью объекта playwright. Для того чтобы объект playwright стал  доступен в консоли DevTools, запустить тест в режиме отладки с PWDEBUG=console.
Для того чтобы искать элементы  используя селекторы css и xpath используйте следующий синтаксис
`playwright.$(selector)`: выделяет первое вхождение селектора.
`playwright.$$(селектор)`: выделяет все вхождения селектора. 

Используя данную функцию и селектор, вас переместит во вкладу элементы и отобразит данный селектор в DOM.
`playwright.inspect(selector)`

Вы можете сгенерировать локатор. Для этого выберите на вкладке нужный вам элемент и введи в консоле playwright.generateLocator($0)
`playwright.generateLocator($0)`

Логирование API Playwright

Иногда нам нужно  увидеть выполнение команд глазами нашего инструмента автоматизации. В этом может помочь добавление журналов регистрации, которые пошагово показывают каждую команду по мере ее выполнения.
`DEBUG=pw:api`

11. Trace Viewer
Playwright Trace Viewer — еще одна функция Playwright, которую можно использовать для отладки автотестов.
Это инструмент с графическим интерфейсом, который помогает просматривать записанные во время выполнения теста.
Вы можете открывать трассировки локально с помощью CLI или в онлайн на https://trace.playwright.dev/
Чтобы записать трассировку, вам необходимо с помощью CLI  передать атрибут  --tracing и  выбрать вариант записи.

Команда для запуска всех тестов и сохранением трассировки только неудачных
`pytest --tracing=retain-on-failure`

Для просмотра выполните команду playwright show-trace и укажите адрес с записанному архиву трассировки
`playwright show-trace trace.zip`
Trace Viewer состоит из 4 основных областей:
- Timeline  - временная шкала, показывающая скриншоты состояния страницы по мере выполнения действий
- Actions - панель со списком действий в текущем тестовом сценарии
- Snapshots - сохраненные снимки DOM для каждого действия.
- Action Details - детальная информация по местоположение источника, выполнение + сетевые журналы для каждого действия

12. page.pause()
После того как вы познакомились с Playwright Inspector и вам он понравился, вам захочется использовать его во 
время отладки теста. Но запускать и проходить весь тест в режиме debug, и каждый раз менять переменной среды не очень
удобно. Для того чтобы избежать это, можно использовать функцию `page.pause()`

Вызовите данную функцию перед шагом который вам нужно проверить.
Playwright приостановит выполнение скрипта, откроет Playwright Inspector и будет ждать,
пока пользователь либо нажмет кнопку «Resume», либо выполнит команду playwright.resume() в консоли DevTools.

Если вам необходимо приостановить выполнение кода на какое-то время, вы можете взять тайм-аут
`page.wait_for_timeout(3000)`
