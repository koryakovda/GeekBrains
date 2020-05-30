class Store:
    def __init__(self):
        self.store = {}

    def to_take(self,param):
        store_dict[param] = {param.index,param.name,param.quantity,param.price,param.type}


    def to_ship(self,param,devision):
        pass

devision1 = {}
devision2 = {}
store_dict = {}


class Equipment:
    def __init__(self,index,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.index = index
    def __str__(self):
        return str(self.index) + ' ' + self.name + ' ' + str(self.quantity) + ' ' + str(self.price)

class Printer(Equipment): #index 1 type color/blak_and_wight
    def __init__(self,index,name,quantity,price,type):
        super().__init__(index,name,quantity,price)
        self.type = type
    def __str__(self):
        return str(self.index) + ' ' + self.name + ' ' + str(self.quantity) + ' ' + str(self.price) + ' ' + self.type

class Scaner(Equipment): #index 2 type table/manual
    def __init__(self, index, name, quantity, price, type):
        super().__init__(index, name, quantity, price)
        self.type = type
    def __str__(self):
        return str(self.index) + ' ' + self.name + ' ' + str(self.quantity) + ' ' + str(self.price) + ' ' + self.type

class Xerox(Equipment):#index 3 type analog/digital
    def __init__(self, index, name, quantity, price, color):
        super().__init__(index, name, quantity, price)
        self.color = color
    def __str__(self):
        return str(self.index) + ' ' + self.name + ' ' + str(self.quantity) + ' ' + str(self.price) + ' ' + self.color

store = Store()
printer1 = Printer(1,'Expression',2,8000,'color')
print(printer1)
store.to_take(printer1)
# sore.to_ship(printer1,devision1)
print(store_dict)
