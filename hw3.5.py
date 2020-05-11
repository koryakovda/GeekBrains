def summ(a):
    i = 0
    n = 0
    while i < len(a):
        if a[i] == 'q':
            break
        else:
            n += int(a[i])
            i += 1
    return n

itog = []
while True:
    my_string = str(input('Введите элементы строки или введите "q" чтобы завершить подсчет: '))
    my_list = list(my_string.split())
    if 'q' in my_list:
        itog.append(summ(my_list))
        print('Сумма этого ввода: ', summ(my_list))
        print('Сумма общая: ', summ(itog))
        break
    else:
        itog.append(summ(my_list))
        print('Сумма этого ввода: ', summ(my_list))
        print('Сумма общая: ', summ(itog))

