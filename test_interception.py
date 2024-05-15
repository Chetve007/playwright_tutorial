from playwright.sync_api import Route, Request, expect


def test_listen_network(browser):
    browser.on("request", lambda request: print(">>", request.method, request.url))
    browser.on("response", lambda response: print("<<", response.status, response.url))
    browser.goto('https://osinit.ru/')


# def handle(route: Route, request: Request):
#     if request.method == "POST":
#         print(request.post_data_json)
#         route.continue_()
#     route.continue_()
#
#
# page.route("**/*", handle)
# page.goto("file:///way_to_file/index.html")


def test_interrupt_request(browser):
    """
    page.route - функция позволяющая обрабатывать сетевые запросы.
    В отличие от page.on метод route может изменять сетевые запросы и ответы

    **/*.{png,jpg,jpeg} - шаблон url для соответствия маршрутизации.
    В качестве шаблона можно использовать RegExp, либо целый url.

    lambda route: route.abort() - это функция обработчик для маршрутизируемых запросов.
    Встроенный в playwright метод route.abort() прерывает запрос по маршруту.
    """
    browser.on("request", lambda request: print(">>", request.method, request.url))
    browser.route(r"**/*.{png,jpg,jpeg}", lambda route: route.abort())
    browser.goto("https://reqres.in/")


def test_network(browser):
    """Помимо прерывания запросов, playwright дает возможность их модифицировать.
    Для этого используете метод route.continue_ и аргументом post_data
    """
    browser.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
    browser.goto('https://reqres.in/')
    browser.get_by_text(' Register - successful ').click()


def test_mock_tags(browser):
    """Для подмены ответа используется метод route.fulfill в котором указывается путь до json с подменными данными.
    Или сам json.
    """
    # browser.route("**/api/tags", lambda route: route.fulfill(path="data.json"))
    browser.route("**/api/tags", lambda route: route.fulfill(json={'tags': ['some', 'where', 'tags']}))
    browser.goto('https://demo.realworld.io/')


def test_intercepted(browser):
    """Другой вариант решения данной задачи - использование метода route.fetch
    и опции json для route.fulfill (добавлены в версии 1.29)

    Мокинг данных в данном случае делится на три этапа
    - Получить исходные данные с сервера.
    - Изменить полученные данные в формате json к нужному для вас значению.
    - Выполнить запрос с измененными данными.

    Метод route.fetch выполняет запрос на сервер и получает результат на данный запрос.
    Вы можете работать с полученным ответом как с json объектом.  С помощью метода route.fulfill и опции json,
    отправьте запрос с исправленным телом ответа.
    """
    def handle_route(route: Route):
        response = route.fetch()
        json = response.json()
        json["tags"] = ["open", "solutions"]
        route.fulfill(json=json)

    browser.route("**/api/tags", handle_route)

    browser.goto("https://demo.realworld.io/")
    sidebar = browser.locator('css=div.sidebar')
    expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])
