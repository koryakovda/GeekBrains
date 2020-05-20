with open('text.txt','w') as f:
    while True:
        a = input('Введите данные для записи: ')
        if a == '':
            break
        f.writelines(f'{a}\n')

