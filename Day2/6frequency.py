# n = int(input("Enter number the number of elements for which we have "))
# array = []
# for i in range(n):
# 	array.append(int(input("enter element: ")))
# print(array)
array = [1,1,1,2,2,2,1,5,5]
i = 0
count = 1
n = 6
#print(len(array))
while i <(len(array)):
	#print("len of array",len(array))
	var = array[i]
	j = i
	count = 1
	while j <(len(array) ):
		
		if var == array[j]:
			count = count + 1
			del array[j]
		j=j+1
 	print("var = %d count = %d "%(var,count))
	#del array[i]
	i=i+1

