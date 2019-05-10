array = [1,2,3,4,5,6]
for i in array:
	print(i,end =' ' )
print()

modified = list(map(lambda x: x**3, array))
print(modified)
filtered = list(filter( lambda x: x < 30,modified))
print(filtered)