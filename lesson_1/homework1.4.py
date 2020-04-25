n = int(input('Введите целое положительное число: '))
i = n
b = 0
while i > 0:
    a = i % 10
    i = i // 10
    if a > b:
        b = a
print(b)