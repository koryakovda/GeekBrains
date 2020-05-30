class Data:
    def __init__(self,chislo):
        self.chislo = chislo
    @classmethod
    def extract(cls,date_str):
        array = list(map(int,date_str.split('-')))
        print(array)

    @staticmethod
    def date_validation(date_str):
        days_in_month = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        day,month,year= map(int,date_str.split('-'))
        return print(day <= days_in_month[month] and month <=12 and year <=2021)

data = Data('29-05-2020')
print(data.chislo)
data.extract('29-05-2020')
Data.extract('29-05-2020')
validation = Data.date_validation('29-05-2020')