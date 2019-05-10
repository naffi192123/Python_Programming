#find out the factorial of any number
num =int(input("enter the number for which you want find the factorial"))
fact = 1
while num > 1:
	fact =fact*num
	num = num-1
print("factorial of numner is: ", fact) 