class Item:
    def __init__(self, name, price, taxable):
        self.__name = name
        self.__price= price
        self.__taxable= taxable
    def __str__(self):
        return self.__name
    def getPrice(self):
        return self.__price
    def getTax(self, tax):
        if self.__taxable == False:
                return 0
        else:
            return self.getPrice()*tax
        
            
        
            
            
            
        