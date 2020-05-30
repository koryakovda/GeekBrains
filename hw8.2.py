class MyOwnException(Exception):
    def __init__(self,txt):
        self.txt = txt
try:
    a = int(input('Input a:'))
    b = int(input('Input b:'))
    if b == 0:
        raise MyOwnException('Devision by 0 is not possible!')
    else:
        result = a / b
except ValueError:
    print('Input numbers!')
except MyOwnException as err:
    print(err)
else:
    print(result)