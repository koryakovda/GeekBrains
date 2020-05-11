x = float(input('Введите  действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))

# # 1 Var
# def my_func(x,y):
#     z = x ** y
#     return z
# out = my_func(x,y)
# print(out)

# 2 Var
def my_func(x,y):
    n = 1
    while y < 0:
        n = n * x
        y = y + 1
        out = 1 / n
    return out
print(my_func(x,y))

