

class Animal:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        pass


class Dog(Animal):

    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age

    def make_sound(self):
        return "Woof!"


dog = Dog('Sam', 'English Bulldog', 3)
print(dog.name)
print(dog.breed)
print(dog.age)
print(dog.make_sound())
