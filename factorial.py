def factorial(number):
    if(number == 0 or number == 1):
        return 1
    else:
        return number*factorial(number-1)

number = int(input("Enter a number: "))
print("Factorial of",number,":",factorial(number))
