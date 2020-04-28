old_list = [7, 4, 3, 3, 2]
a = int(input('Введите натуральное число: '))
for el in old_list:
    if a == el:
        old_list.reverse()
        old_list.insert(old_list.index(el),a)
        old_list.reverse()
        break
    if a > el:
        old_list.insert(old_list.index(el),a)
        break
    if a < old_list[-1]:
        old_list.append(a)
        break
print(old_list)
