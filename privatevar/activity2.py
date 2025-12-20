class computer():
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print('selling price is',self.__maxprice)
    def setmaxprice(self,Price):
        self.__maxprice=Price
COMP=computer()
COMP.sell()
COMP.__maxprice=1000
COMP.sell()
COMP.setmaxprice(1000)
COMP.sell()

