xmax = float(6)
ymax = float(5)
step_size = float(1)

position = []

x = -xmax

while x <= xmax:
	point=[]
	y = float(-ymax)
	while y <= ymax:
		p =round((x**2+y**2)**0.5, 2)
		point.append(p)
		y = y + step_size
	position.append(point)
	x = x + step_size

for n in position:
	print(n)