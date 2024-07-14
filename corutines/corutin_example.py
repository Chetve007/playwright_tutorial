

def greet():
    while 1:
        name = yield
        print(f'Hello {name}')


g = greet()
g.send(None)

g.send('Alex')

g.send('Nastia')
