# what is a function?
# a function is a piece of code that takes in inputs and returns an output

def my_func(name:str, age:int = 0):
    print(name)
    print(age)

my_func("ed")
my_func("ed", 18)

def max_in_list(numList):
    maxNum = numList[0]
    for num in numList:
        if num > maxNum:
            maxNum = num
    return maxNum

max_num = max_in_list([1, 4, 2, 10, 11, 14, 6, 3, 5, 2, 6, 7, 13])
print(max_num)


def ask_for_name_and_age():
    return input("enter your name: "), int(input("enter your age: "))

retrieved_name, retrieved_age = ask_for_name_and_age()
print(f"{retrieved_name}, {retrieved_age}")
