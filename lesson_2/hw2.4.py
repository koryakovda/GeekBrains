my_string = str(input('Введите элементы строки: '))
my_list = list(my_string.split())
for ind,el in enumerate(my_list):
    print(ind,el[:10])
