with open('3.txt','r') as f:
    summ_salary = 0
    summ_employee = 0
    for line in f:
        new_list = line.split()
        name,salary = new_list[0],new_list[1]
        summ_salary += float(salary)
        summ_employee += 1
        if float(salary) < 20000:
            print('Зарплата ниже 20000: ', name)
        average = summ_salary/summ_employee
    print('Средняя ЗП:',average)
