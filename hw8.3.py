class MyOwnException(Exception):
    def __init__(self,txt):
        self.txt = txt
my_list = []
while True:
    try:
        num = input('Input number or stop to finish: ')
        if num == 'stop':
            print(my_list)
            break
        else:
            if num.isnumeric() == True:
                int_num = int(num)
                my_list.append(int_num)
            else:
                raise MyOwnException('It is not a number!')
    except MyOwnException as err:
        print(err)