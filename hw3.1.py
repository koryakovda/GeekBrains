def delenie(a,b):
    c = a / b
    return c

a = float(input('Введите 1 число: '))
b = float(input('Введите 2 число: '))

try:
    d = delenie(a,b)
    print(round(d, 2))
except ZeroDivisionError:
    print('Деление на 0 невозможно')