a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))

def summ(a,b,c):
    my_list = [a, b, c]
    my_list.sort()
    z = int(my_list[1]) + int(my_list[2])
    return z
out = summ(a,b,c)
print('Сумма наибольших чисел равна: ',out)
