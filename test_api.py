

def test_inventory(browser):
    response = browser.request.get('https://petstore.swagger.io/v2/store/inventory')
    print(response.status)
    print(response.json())


def test_add_user(browser):
    """Посмотреть содержание тела ответа можно с помощью трех методов:
    - response.text()
    - response.json()
    - response.body()
    """
    data = [
              {
                "id": 9743,
                "username": "alex",
                "firstName": "Alexey",
                "lastName": "Chetkoff",
                "email": "chet@mailbox.ru",
                "password": "12345678",
                "phone": "+79999999992",
                "userStatus": 1
              }
            ]
    header = {
        'accept': 'application/json',
        'content-Type': 'application/json'
    }
    response = browser.request.post('https://petstore.swagger.io/v2/user/createWithArray', data=data, headers=header)
    print(response.status)
    print(response.json())
