class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def full_name(self):
        return self.name + ' ' + self.surname

    def total_income(self):
        return self._income["wage"] + self._income["bonus"]

p = Position ('Oleg', 'Shubin', 'Student', '6000', '1300')
print(p.full_name(), p.total_income())