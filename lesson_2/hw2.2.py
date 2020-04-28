my_list = list(input('Введите элементы списка: '))
i = 0
j = 1
print('Ваша строка до изменения: ', my_list)
b = len(my_list) // 2
# print(len(my_list))
# print(b)
while j < b * 2:
    my_list[i], my_list[j] = my_list[j], my_list[i]
    i += 2
    j += 2
print('Ваша строка после изменения: ', list(my_list))
