class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f'repr: {self.name}'

    def __str__(self) -> str:
        return f'str: {self.name}'
