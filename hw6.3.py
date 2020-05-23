class Worker:

        name = 'Pep'
        surname = 'Guardiola'
        position = 'Trainer'
        _income = {'wage':100000,'bonus':1000}


class Position(Worker):

    def get_full_name(self):
        print(Worker.name,Worker.surname)

    def get_total_income(self):
        print(sum(Worker._income.values()))

emplyee = Position()
emplyee.get_full_name()
emplyee.get_total_income()
print(emplyee.position)



