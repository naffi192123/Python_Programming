radius = int(input("Enter the radius: "))
pi = 3.14
if radius <= 0:
	print("invalid input")
else:
	area = pi*(radius**2)
	perimeter = 2*pi*radius
print("Area of circle is: ", area)
print("Perimeter of circle is", perimeter)