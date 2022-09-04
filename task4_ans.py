class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("кх-кх")


class Cat(Animal):
    def sound(self):
        super().sound()
        print(f"МЯУ! Я {self.name}")


class Dod(Animal):
    def sound(self):
        super().sound()
        print(f"ГАВ! Я {self.name}")
