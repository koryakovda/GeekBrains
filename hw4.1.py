from sys import argv
time,rate,bonus = argv[1:]
summ = float(time)*float(rate) + float(bonus)
print(summ)