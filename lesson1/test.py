class Item:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock


myDict = {"test": Item("test", 10), "test2": Item("test2", 20)}

itemName = input("enter the item name: ")
if itemName in myDict:
    myDict[itemName].stock += int(input("enter the stock amount: "))

for item in myDict.values():
    print(item.name)
    print(item.stock)
