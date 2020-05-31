# python is dynamically and weakly typed
# python can automatically convert for you the variable type.
# types in python is very flexible
# weak typing means it doesnt enforce type rules

# python runs slower than compiled languages and also strongly and statically typed languages
# the binary is easy to understand by the computer, so execution time is much faster
# strongly typed languages have lesser effort of catch typing errors
# catched at compile time - when you compile the source code

# 1. primitive types
# string, int, float, boolean

# 2. reference type
# objects, list, dictionary, set, tuple

my_var = 10
my_float = 5.5
my_str = "ediejsandaksdnas"
my_bool = True
my_empty = None

my_list = [1, "hello", True, None, 2, "sadasdasd"]
my_dict = {1:"d", "dasd":True}
my_set = {1,2,3,4,5}
my_tuple = (1, "sadsad", True)

# list is mutable = the values can change
test = [1, 2, 3]
print(test)
test.append(4) # test - [1, 2, 3, 4]
print(test)

# tuple is immutable
test_tuple = (1, 2, 3)
print(test_tuple)
new = test_tuple + (4,)
print(new)

# list and tuple elements can be accessed by index
# starts at 0
print(test[0])
print(test_tuple[0])

# set cannot be accessed by index
if 5 in my_set:
    print("true")
