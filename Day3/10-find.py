#program to search an element in a tuple
n = int(input("Enter the element to search: "))
tupl =(1,2,3,4,5)
for i in tupl:
	if n == i:
		print("Found")
		break
	else:
		print("not found")
		continue