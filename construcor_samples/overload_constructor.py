

class Employee:

    def __init__(self, name):
        self.name = name

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


# sarah = Employee('Sarah')
# print(ira.name)
# TypeError: Employee.__init__() missing 1 required positional argument: 'surname'

john = Employee('John', 'Malkovich')
print(john.name)
print(john.last_name)
