#program to convert fahrenheit to celcius
choice = int (input("Enter choice to 1 for fahrenheit to celcius 2 for celciusto fahrenheit"))
if choice == 1:
	c = int(input("Enter temprature in celcius: "))
	f = c*(9/5)+32
	print(f)
elif choice == 2:
	f = int(input("Enter the program to conver "))
	c = (f-32)*5/9
	print(c)
else:
	print("invalid input")
