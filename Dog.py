class Dog:
    """Проста спроба змоделювати собаку."""

    def __init__(self, name, age):
        """Ініціювати атрибути ім'я та вік."""
        self.name = name
        self.age = age

    def sit(self):
        """Симулювати виконання команди 'сидіти'."""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """Симулювати виконання команди 'лежати'."""
        print(f'{self.name} rolled over!')


my_dog = Dog('Berta', 6)
print(my_dog.roll_over())
