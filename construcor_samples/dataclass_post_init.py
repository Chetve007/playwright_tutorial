from dataclasses import dataclass, field


@dataclass
class ConstructorDataclassPostInit:
    """__post_init__ вызывается после основного конструктора.
    Используется вместе с декоратором @dataclass и позволяет делать доп. действия
    после инициализации параметров определенных в dataclass
    """

    value: int
    extra: int = field(init=False)

    def __post_init__(self):
        self.extra = self.value * 3


obj = ConstructorDataclassPostInit(3)
print(obj.value, obj.extra)
