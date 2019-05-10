n = int(input("Enter number the number of elements for which we have "))
array = []
for i in range(n):
	array.append(int(input("enter element: ")))
print(array)

array.remove(4)
print(array)
array.pop()
print(array)
del array[2:3]
print(array)
