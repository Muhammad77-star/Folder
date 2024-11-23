class Computer:
    def __init__(self):
        self. __maxprice = 900
    def Sell(self):
        print("Selling price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.Sell()
c.__maxprice = 1000
c.Sell()
c.setMaxPrice(1000)
c.Sell()