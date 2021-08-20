year = int(input("Enter the year you wish:"))

if(year%400 == 0 or year%4==0):
    print("%d is a leap year"%year)
elif(year%100 == 0):
    print("%d is not a leap year"%year)
else:
    print("%d is Not the leap year"%year)
