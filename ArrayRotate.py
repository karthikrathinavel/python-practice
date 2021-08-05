arr = []
temp = []
noOfElement = int(input("Enter the number of element:"))
for i in range(noOfElement):
	element = int(input("Enter the %d st element:" % (i+1)))
	arr.append(element)
print("Your array is ",arr)
d = int((input("Enter the number of elements to be rotate: ")))
for i in range(d):
	temp.append(arr[i])
del arr[0:d]
print("These elements are moving to rotate: ",temp)
print("Your array after rotation: ", (arr + temp))