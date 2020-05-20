with open('numbers.txt','w') as f:
    f.write(input('input numbers:'))
with open('numbers.txt','r') as f:
    a = f.read()
    b = a.split()
    my_list = []
    for i in b:
        my_list.append(float(i))
    print(sum(my_list))
