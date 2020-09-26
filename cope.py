while True:
    age = int(input("Please enter your age: "))
    if age < 0 or age > 130:
        print("That age is invalid")
    else:
        print("Age accepted. Have a nice day")
        break


