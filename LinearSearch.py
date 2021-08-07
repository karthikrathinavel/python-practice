def search(arr,xElement,count):
	for i in range(0,count):
		if arr[i] == xElement:
			return i
	return -1
arr = []
count = int(input("Enter number of elements in arr[]:"))
for i in range(count):
	element = int(input("Enter %d element: " % (i+1)))
	arr.append(element)
xElement = int(input("Enter the element to be search:"))
result = search(arr,xElement,count)
if(result == -1):
	print("Element is not present in the list")
else:
	print("Element is present in index", result)