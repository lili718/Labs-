import datetime

class Receipt:
    def __init__(self, tax_rate):
        self.__tax_rate = tax_rate
        self.__purchases = []
    def __str__(self):
        emptystring=""
        notaxtotal=0
        tax = 0
        emptystring += str("----- Receipt " + str(datetime.datetime.now()) + "-----\n")
        for i in self.__purchases:
            emptystring += "{:_<20}".format(i.__str__())
            emptystring += "{:_>19}{:.2f}\n".format("_", i.getPrice())
            notaxtotal+= i.getPrice()
            tax += i.getTax(0.07)
        emptystring+= "{:_<20}".format("Sub Total")
        emptystring+= "{:_>19}{:.2f}\n".format("_", notaxtotal)
        emptystring+= "{:_<20}".format("Tax")
        emptystring += "{:_>19}{:.2f}\n".format("_", tax)
        emptystring += "{:_<20}".format("Total")
        emptystring += "{:_>19}{:.2f}\n".format("_", (tax+notaxtotal))
        return (emptystring)
        
    def addItem(self, item):
        self.__purchases.append(item)
    