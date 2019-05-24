from Item import *
from Receipt import *
if __name__=="__main__":
    print("Welcome to Reciept Creator")
    nitem= "yes"
    fullreceipt = Receipt(.07)
    while nitem.lower() == "yes":
        name = input("Enter Item name:")
        price = float(input("Enter item price:"))
        taxable = input("is the item taxable (yes/no):")
        if taxable.lower()== "yes":
            taxable= True
        else:
            taxable = False
        item= Item(name, price, taxable) 
        fullreceipt.addItem(item)
        nitem = input("Add another item(yes/no):")
    print(fullreceipt)
