#check wether the numebr is complex or not and find its conjugate
num = complex(input("Enter Number: "))
if type(num) == complex:
	print("Number is complex")
print(num.conjugate())
