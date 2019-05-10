cols = 7
rows = 1
var  = 7
while rows <= 3:
	cols = 1
	while cols <= var:
		if cols % 2 == 0:
			print("0", end=" ")
		else:
			print("1",end=" ")
		cols = cols+1
	var = var-2
	print("\n")
	rows = rows+1