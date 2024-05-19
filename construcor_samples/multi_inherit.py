

class A:

    def __init__(self, a):
        self.a = a


class B:

    def __init__(self, b):
        self.b = b


class C(A, B):

    def __init__(self, a, b, c):
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = c


c = C(5, 10, 15)
print(c.a)
print(c.b)
print(c.c)
