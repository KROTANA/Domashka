class Shop:
    def __init__(self):
        self.prod = []
    def AddMag(self, name):
        return self.prod.append(name)
    def Afd(self):
        try:
            while True:
                list = [int(input('Номер\n')), input('Название\n'), int(input('Цена\n'))]
                v.AddMag(list)
                for i in v.prod:
                    print(i)
        except:
            print('Неравильный тип данных')
v = Shop()
v.Afd()
