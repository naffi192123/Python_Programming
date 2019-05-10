var = "CDAC Mohalli"
addent = "Is"

subvar = var[5: ]

if not(subvar.startswith(addent)):
	print(addent+" "+subvar)
