#find repeated element of a tuple
tupl = (3,4,4,6,7,8,8,7,4,4,4,44,9,0)
dic = {}
for i in tupl:
	dic.update({i: tupl.count(i)}) 
for i in dic:
	if dic[i]>1:
		print("%s repeated %s times"%(i, dic[i]))
