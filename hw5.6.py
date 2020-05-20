with open('6.txt','r') as f:
    my_dict = {}
    for line in f:
        numbers_list = []
        a = line.replace('(',' ')
        b = a.split()
        numbers = b[1::2]
        subject = str(b[:1])
        for i in numbers:
            numbers_list.append(int(i))
        summ = sum(numbers_list)
        my_dict[subject]=[summ]
    print(my_dict)