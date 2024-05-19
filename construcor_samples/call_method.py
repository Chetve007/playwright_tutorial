

class ConstructorCallMethod:

    def __init__(self, value):
        self._call_method()
        self.value = value

    def _call_method(self):
        print(self.value)


# AttributeError: 'ConstructorCallMethod' object has no attribute 'value'
obj = ConstructorCallMethod('Foo')
