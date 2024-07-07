number1 = input("Enter number 1 :")
number2 = input("Enter number 2 :")
number3 = input("Enter number 3 :")

if number2 > number3:
    if number2 > number1:
        print("number 2 is greter then others")
elif number1 > number2:
    if number1 > number3:
        print("number 1 is greter then others")
else:
        print("number 3 is greter then others")