with open('4.txt','r') as f:
    for line in f:
        if 'One' in line:
            a = line.replace('One', 'Один')
            new_f = open('new_4.txt', 'w')
            new_f.write(a)
            new_f.close()
        if 'Two' in line:
            b = line.replace('Two', 'Два')
            new_f = open('new_4.txt', 'a')
            new_f.write(b)
            new_f.close()
        if 'Three' in line:
            c = line.replace('Three', 'Три')
            new_f = open('new_4.txt', 'a')
            new_f.write(c)
            new_f.close()
        if 'Four' in line:
            d = line.replace('Four', 'Четыре')
            new_f = open('new_4.txt', 'a')
            new_f.write(f'{d}\n')
            new_f.close()
