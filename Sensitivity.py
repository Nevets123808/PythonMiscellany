#Define Functions
def rsquare(x,y,z):
	return (x**2+y**2+z**2)
def P(l, gamma):
	if l == 1:
		return (1.5*(5*gamma**2-1))
	elif l == 2:
		return((15/8)*(21*gamma**4-18*gamma**2+1))
	else :
		return((3/16)*(1001*gamma**6-1155*gamma**4+315*gamma**2-10))
		
	
def coil_locate(x,y,z):
	x_1 = xspace*0.5+x
	y_1 = yspace*0.5+y
	z_1 = zspace*0.5+z
	
	return [x_1,y_1,z_1]
	
def sensitivity_coil(l,r,z,gamma):
	return (b[l]*(l+1)*z*P(l,gamma)
	
	
#Set Parameters
coil_d = 15e-3
coil_l = float(10e-3)
coil_b = float(5e-3)

xspace = float (150e-3)
zspace = float(40e-3)
yspace = float(0)

xmax = float(6)
ymax = float(5)
step_size = float(1)

#Position insensitve Calculations
alpha = coil_d/coil_b
beta = coil_l/coil_b

b1 = ((coil_b/2)**4)*(beta/6)*(alpha**3-1)
b2 = ((coil_b/2)**6)*(beta/120)*(9*(alpha**5-1)-20*(beta**2)*(alpha**3-1))
b3 = ((coil_b/2)**8)*(beta/336)*(15(alpha**7-1)-84*(beta**2)*(alpha**5-1)+56(beta**4)*(alpha**3-1))

b=[0,b1,b2,b3]


position = []
point = []

x = -xmax
z = 0
while x <= xmax:
	y = float(-ymax)
	while y <= ymax:
		r = rsquare(x,y,z)
		point.append(r)
		y = y + step_size
	position.append(point)
	x = x + step_size


