import math
def fact(a):
    for n in range(a)[1:]:
        yield math.factorial(n)
a=0
num = int(input('input number: '))
for el in fact(num+1):
    a += 1
    print(f'{a}!:{el}')

