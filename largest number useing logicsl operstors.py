number1 = int(input("Enter number 1 = "))
number2 = int(input("Enter number 2 = "))
number3 = int(input("Enter number 3 = "))

if number1 > number2 and number1 > number3:
    print("largest number = ",number1)
elif number2 > number1 and number2 > number3:
    print("Largest number = ",number2)
else:
    print("Largest number = ",number3)