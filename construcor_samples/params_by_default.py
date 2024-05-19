

class Example:
    """Если параметр по умолчанию является изменяемым объектом (список, словарь) -
    это может привести к неожиданному поведению
    """

    def __init__(self, values=[]):
        self.values = values


obj1 = Example()
obj2 = Example()

obj1.values.append(3)

print(obj2.values)

obj2.values.append(7)

print(obj1.values)
