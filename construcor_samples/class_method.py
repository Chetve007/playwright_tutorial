

class ConstrucorClassMethod:
    """
    Создание объектов через классовые методы.
    Необходимо, если есть различные методы инициализации объектов со сложной логикой
    или когда необъодимо выполнить сложную логику перед созданием объекта.
    """

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_alternate_construct(cls, alt_value):
        value = alt_value * 2
        return cls(value)


clazz = ConstrucorClassMethod.from_alternate_construct(3)
print(clazz.value)
