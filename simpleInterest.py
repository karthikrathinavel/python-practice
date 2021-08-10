def simpleInterest(p,t,r):
    print("The principle is",p)
    print("The time period is",t)
    print("The rate of interest is",r)
    simpleInterest = (p*t*r)/100
    print("Simple Interest(SI):",simpleInterest)
    return simpleInterest

p = int(input("Enter the principle amount: "))
t = int(input("Enter the time period: "))
r = int(input("Enter the rate: "))

simpleInterest(p,t,r)
