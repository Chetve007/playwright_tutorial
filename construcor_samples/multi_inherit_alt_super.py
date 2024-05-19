

class A:

    def __init__(self, a):
        self.a = a


class B(A):

    def __init__(self, a, b):
        super().__init__(a)
        self.b = b


class C(B):

    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c


c = C(1, 2, 3)
print(c.a)
print(c.b)
print(c.c)
