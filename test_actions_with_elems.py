import os

import pytest


def test_drag_and_drop(browser):
    browser.goto('https://zimaev.github.io/draganddrop/')
    browser.drag_and_drop("#drag", "#drop")


def test_dialogs(browser):
    """Диалоговые окна.
    По умолчанию диалоговые окна автоматически закрываются Playwright, поэтому необязательно их обрабатывать.
    """
    browser.goto("https://zimaev.github.io/dialog/")
    browser.get_by_text("Диалог Alert").click()
    browser.get_by_text("Диалог Confirmation").click()
    browser.get_by_text("Диалог Prompt").click()


@pytest.mark.parametrize('action', ('accept', 'dismiss'))
def test_dialogs_confirmation(browser, action):
    """В данном примере анонимная функция, в качестве параметра принимает экземпляр класса Dialog.
    Далее метод dialog.accept() заставляет Playwright нажимать на кнопку OK в диалоговом окне.
    По умолчанию  диалоговые окна данного вида, Playwright обрабатывает отказом(т.е нажимаем на Отмена).

    Диалоговые окно завершаются автоматически, если нет слушателя page.on("dialog").
    """
    browser.goto("https://zimaev.github.io/dialog/")
    browser.on("dialog", lambda dialog: dialog.accept() if action == 'accept' else dialog.dismiss())
    browser.get_by_text("Диалог Confirmation").click()


def test_upload_file(browser):
    browser.goto('https://zimaev.github.io/upload/')
    browser.set_input_files("#formFile", "data/some_file.txt")
    browser.locator("#file-submit").click()


@pytest.mark.parametrize('option', ('first', 'second'))
def test__upload_file_by_filechooser(browser, option):
    """Вы можете зарегистрировать обработчик события "filechooser" и так же загрузить файл.
    Рассмотрены 2 варианта.

    Указывай всегда абс. путь к файлу
    os.path.abspath(pathlib.Path('rut_project', 'file.pdf'))
    чтобы работало на любых ОС
    """
    browser.goto('https://zimaev.github.io/upload/')

    match option:
        case 'first':
            browser.on("filechooser", lambda file_chooser: file_chooser.set_files("data/some_file.txt"))
            browser.locator("#formFile").click()
        case 'second':
            with browser.expect_file_chooser() as fc_info:
                browser.locator("#formFile").click()
            file_chooser = fc_info.value
            file_chooser.set_files("data/some_file.txt")


def test_download(browser):
    """Скачать файл.

    Если вы понятия не имеете, что инициирует загрузку используйте следующую запись.
        page.on("download", lambda download: print(download.path()))

    Довольно типичный случай загрузки файла с веб-сайта - это нажатие кнопки или гиперссылки.
    Если вы знаете в результате чего происходит загрузка, в этом случае необходимо использовать
    метод expect_download() с менеджером контекста.
        with page.expect_download() as download_info:
            page.locator("a:has-text(\"Download\")").click()

    Когда загрузка будет завершена, будет возвращена информация о загрузке и download_info примет результат загрузки.
    Вы можете получить значения  результата загрузки с помощью download_info.value.
    Сохраним информацию в переменную download
        download = download_info.value

    Какую информацию вы получаете?
        download.cancel() - отменяет загрузку
        download.delete() - удаляет загруженный файл
        download.failure() - возвращает ошибку загрузки, если таковая имеется.
        download.page - возвращает объект страницы, к которой принадлежит загрузка.
        download.path() - возвращает путь к загруженному файлу
        download.save_as(path) - скопирует загруженный файл по указанному пути
        download.suggested_filename - возвращает имя файла
        download.url - возвращает загруженный URL-адрес
    """
    browser.goto("https://demoqa.com/upload-download", wait_until='commit')

    with browser.expect_download() as download_info:
        browser.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./data/"
    download.save_as(os.path.join(destination_folder_path, file_name))


def test_get_elem_value(browser):
    """Получение значений элемента.

    element.inner_text()
    element.text_content()

    Используйте all_inner_text() и all_text_contents()
    когда вам надо получить текст всех схожих элементов (например строк таблицы).
    В результате использования данных методов вернется массив значений для всех соответствующих элементов.

    В чем различия inner_text и text_content:
    - textContent получает содержимое всех элементов, включая <script> и <style>, тогда как innerText этого не делает.
    - innerText умеет считывать стили и не возвращает содержимое скрытых элементов, тогда как textContent этого не делает.

    Также кроме текста, можно получить HTML-код элемента.
        element = page.locator('a:has-text("playwright")')
        print(element.inner_html())
    """
    browser.goto('https://zimaev.github.io/table/')
    row = browser.locator("tr")
    print(row.all_inner_texts())
    print(row.all_text_contents())


def test_take_screenshot(browser):
    """Создание скриншотов. Аргументы:

    - full_page (bool): Определяет, следует ли создать скриншот всей страницы (True) или только видимой области (False).
    По умолчанию значение False.

    - type (str): Задает формат изображения. Доступные варианты включают 'jpeg' и 'png'. По умолчанию 'png'.

    - quality (int): Качество сжатия изображения для формата 'jpeg'. Должно быть число от 0 до 100.
    По умолчанию не определено.

    - clip (dict): Задает область для создания скриншота, указав координаты x, y, ширину и высоту. Например:
        page.screenshot(path="clipped_image.png", clip={"x": 50, "y": 0, "width": 400, "height": 300})

    - omit_background (bool): Позволяет убрать фон изображения. Если True, фон на скриншоте будет прозрачным,
    что актуально в случае формата 'png'. По умолчанию значение False.

    - timeout (float | int): Задает максимальное время ожидания (в миллисекундах) перед созданием скриншота.
    Установите значение как "0", чтобы ждать неограниченное время. По умолчанию 30000 миллисекунд (30 секунд).
    """
    browser.goto('https://zimaev.github.io/table/')

    browser.screenshot(path="data/screenshot.png")
    browser.screenshot(path="data/screenshot_type.jpeg", type="jpeg")
    browser.screenshot(path="data/screenshot_full.png", full_page=True, omit_background=True)

    browser.get_by_text('Mark Otto @mdo').screenshot(path="data/screenshot_element.png")


def test_new_tab(browser):
    """Работа с несколькими вкладками(Tabs).

    Playwright открывает новые вкладки в контексте браузера. Каждый сеанс playwright начинается
    с иерархии браузер(Browser) -> контекст(Context) -> страница(Page).
    """
    browser.goto("https://zimaev.github.io/tabs/")

    with browser.context.expect_page() as tab:
        browser.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
    assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"

    sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    assert sign_out.is_visible()
