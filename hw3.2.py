shablon = ['имя', 'фамилия', 'год рождения','город проживания', 'email', 'телефон']
info = {}
def function(a):
    for i in a:
        dannie = input('Введите {}: '.format(i))
        info[i] = dannie
    return info
a = function(shablon)
print(a)


# def function(a):
#     for i in a:
#         dannie = input('Введите {}: '.format(i))
#     return dannie
# a = list(map(function,info.keys()))
# print(a)