revenue = int(input('Введите прибыль: ')) # выручка
costs = int(input('Введите издержки: ')) # издержки
profit = revenue - costs # прибыль
profitability = profit / revenue
if revenue >= costs:
    print('выручка больше издержек')
    print('рентабельность выручки: ',profitability)
else:
    print('издержки больше выручки')
employees = int(input('Введите количество сотрудников: '))
employee_profit = profit / employees
print('прибыль фирмы в расчете на одного сотрудника: ',employee_profit)