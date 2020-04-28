list = []
name_list = []
price_list = []
amount_list = []
unit_list = []
additem = input('Хотите добавить новый товар? (y/n): ')
while additem == 'y':
    num = int(input('Введите номер товара по порядку: '))
    name = input('Введите название товара: ')
    name_list.append(name)
    price = int(input('Введите цену за единицу товара: '))
    price_list.append(price)
    amount = int(input('Введите количество товара: '))
    amount_list.append(amount)
    unit = input('Введите единицы измерения: ')
    unit_list.append(unit)
    params = {'название': name, 'цена': price, 'количество': amount, 'eд': unit}
    analitics = {'Название': name_list, 'цена': price_list,'количество': amount_list, 'eд': unit_list}
    merge = (num, params)
    # list_d.append(params)
    print('Вы создали новый товар', merge)
    list.append(merge)
    additem = input('Добавить еще один?(y/n): ')
if additem != 'y':
    print('Структура', list)
    print('Аналитика',analitics)

