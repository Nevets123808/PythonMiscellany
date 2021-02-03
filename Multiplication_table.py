x=[1]
for i in range (1,13):
	x.append(i)

print(x)
for j in range (1,13):
	y=[]
	for i in x:
		y.append(x[i]*j)
	print(y) 