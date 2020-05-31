print("hello world")

# input() will return a str
answer = input("enter your name: ")
# format input to int
age = int(input("enter your age: "))
print(age)
print(answer)

# string formatting
print("hello %s %d %d" %(answer, 1, 2))
# %s %d %f

#string literal - precede with 'f', use {} with variable name
print(f"hello, {answer}")

print("your age is", age)
