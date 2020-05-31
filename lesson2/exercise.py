name = input("Enter your name: ")
gender = input("enter your gender(M or F): ")

if gender.upper() == "M":
    print(f"Hello, mr {name}!")
else:
    print(f"Hello, ms {name}!")
