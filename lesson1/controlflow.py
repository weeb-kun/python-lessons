# if/else statement
age = int(input("enter your age to visit this website: "))
input_name = input("enter your name: ")
if age < 18:
    print("enter")
else:
    print("you are not allowed.")


# not false = true

#if/elif
# elif - else if
if age > 12:
    print("you can ride this ride.")
elif age > 8:
    print("you can ride that other ride.")
else:
    print("you cannot ride any rides.")

# loops
# for, while
# the default implementation of for loop is already foreach
# the range() returns a list
# [0, 1, 2]
# foreach element in [], i is equal to the current element in the iteration
test = ["edric", "sully", "shahid"]
for name in test:
    print(name)

# while loop
num = 0
while True:
    option = input("enter your option(q, age, name): ")
    if option == "age":
        print(age)
        continue
    elif option == "name":
        print(input_name)
    else:
        break
    print("hello from down here")
