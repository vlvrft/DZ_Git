class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Заработная плата: {sum(self._income.values())}'


manager = Position("Rufat", "Veliev", "QA", 80000, 30000)
print(f'{manager.get_full_name()} Должность: {manager.position} {manager.get_total_income()}')






