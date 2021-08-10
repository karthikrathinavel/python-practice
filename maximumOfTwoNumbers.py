def maximum(a,b):
    if(a>=b):
        return a
    else:
        return b

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Max Number: " + str(maximum(num1,num2)))
