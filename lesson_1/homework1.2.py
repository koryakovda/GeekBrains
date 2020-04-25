time = int(input('Введите количество секунд: '))
hours = time // 3600
minutes = (time // 60) - hours * 60
seconds =  time % 60
print(f'Часы:{hours} Минуты:{minutes} Секуды:{seconds}')