n = int(input("Enter number the number of elements for which we have "))
array = []
for i in range(n):
	array.append(int(input("enter element: ")))
print(array)
sumofobser = 0
for i in array:
	sumofobser += i

average = sumofobser/n

print("Average of elements is", int(average)

