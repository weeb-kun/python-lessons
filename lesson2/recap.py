# IO - input/output
# input() will return a str
# int(), float()

# if [condition]:
#       statement
# elif [condition]:
#       statement
# else:
#       statement
# not, and, or

myList = [1, 2, 3]
# elements can have diff types
diffList = [1, "hello", "asdasdas", 1.01]

# loops
# two types of loops in python, for, while.
# for value in list:
#       statement
#       break
#       continue
# foreach loop to loop through each element in a list

# range() returns a list
# range() has 3 arguments/parameters
# range(start num, stop num, step)
# range(0, n, 1) - [0, 1, 2, ..., n-1]
# each iteration/cycle
# first iter, i = 0
# 2nd iter, i = 1
# 3rd iter, i = 2 etc etc
#for i in [1, "ed", "sully", "jeric"]:
#   print(i)

#while loop
# while [condition]:
#       statements
count = 1
while count <= 10:
    print(count)
    count += 1


# functions are a piece of code that takes in inputs/arguments/parameters and returns outputs
def sum(numList):
    result = 0
    for num in numList:
        result += num
    return result

print(sum([1, 10, 12, 123123,423423,123123,41231]))
# function call is a statement to activate/invoke the function
