

class Animal:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        return "Bark"


dog = Dog('Pong', 'French Bulldog')
print(dog.name)
print(dog.breed)
print(dog.make_sound())
