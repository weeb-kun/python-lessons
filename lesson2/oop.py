# oop - object oriented programming
# objects are pieces of data that is used in programming

# classes are like templates to create objects/ instantiation
# objects/instances have certain attributes and behaviours/methods
# a duck can quack
# self - relating to the current object(THIS)
class Duck:
    def __init__(self, w, age, name):
        self.name = name
        # set weight attr to be w
        # 15
        self.weight = w
        # age attr
        # 10
        self.age = age
    def quack(self):
        print("quack")


# w = 15, age = 10
duckDict = {}
# user.username: user
# print(dict[username])
# Enter the username u want to delete:
# del dict[username]

while True:
    option = input("enter your choice: ")
    if option == "add":
        duck = Duck(15, 10, "ted")
        duckDict[duck.name] = duck
    elif option == "del":
        del duckDict["ted"]
    elif option == "show":
        for key in duckDict:
            print(key)
    elif option == "quit":
        break
