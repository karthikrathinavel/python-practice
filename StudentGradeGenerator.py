tamil = float(input("Enter your Tamil Marks:"))
english = float(input("Enter your English Marks:"))
maths = float(input("Enter your Maths Marks:"))
science = float(input("Enter your Science Marks:"))
social = float(input("Enter your Social Science Marks:"))

total = tamil + english + maths + science + social;
percentage = (total / 500) * 100;

print("Total Marks = %.2f"%total)
print("Marks Percentage = %.2f"%percentage)

if(percentage >= 90):
    print("A Grade")
elif(percentage >= 80):
    print("B Grade")
elif(percentage >=70):
    print("C Grade")
elif(percentage >= 60):
    print("D Grade")
elif(percentage >= 40):
    print("E Grade")
else:
    print("Fail :)")
