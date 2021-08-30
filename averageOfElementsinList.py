count = int(input("Enter number of elements in the list:"))
array = []
for i in range(0,count):
    element = int(input("Enter the element:"))
    array.append(element)
average = sum(array)/count
print("average of elements in the list",round(average,2))
