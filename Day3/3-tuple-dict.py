#convert a tuple into dictionary
tupl = ('a','b','c','d','e')

dictionary = {}
i = 1
while i < len(tupl):
	dictionary.update({i:tupl[i]})
	i = i+1
print(dictionary)
