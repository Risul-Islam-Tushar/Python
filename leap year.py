year = int(input("Enter Any Year = "))

if (year % 4 == 0 and year %100 != 0)or(year%400 == 0):
    print(year,"Is a Leap Year")

else:
    print("Its not a leap year")
