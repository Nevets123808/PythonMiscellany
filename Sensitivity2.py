#Define Functions
def rsquare(x,y,z):
	return (x**2+y**2+z**2)**0.5

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
	return (b[l]*(l+1)*z*P(l,gamma))
	
#Set Parameters
coil_d = float(15e-3)
coil_l = float(10e-3)
coil_b = float(5e-3)

xspace = float (150e-3)
zspace = float(40e-3)
yspace = float(0)

xmax = float(6)
ymax = float(6)
step_size = float(1)

#Position insensitve Calculations
alpha = coil_d/coil_b
beta = coil_l/coil_b

b1 = ((coil_b/2)**4)*(beta/6)*(alpha**3-1)
b2 = ((coil_b/2)**6)*(beta/120)*(9*(alpha**5-1)-20*(beta**2)*(alpha**3-1))
b3 = ((coil_b/2)**8)*(beta/336)*(15*(alpha**7-1)-84*(beta**2)*(alpha**5-1)+56*(beta**4)*(alpha**3-1))

b=[0,b1,b2,b3]


position = []
point = []

x = -xmax
z = 0
while x <= xmax:
	point = []
	y = float(-ymax)
	while y <= ymax:
	
		s = 0
		
		loc1 = coil_locate(x,y,z)
		loc2 = coil_locate(-x,y,z)
		loc3 = coil_locate(x,y,-z)
		loc4 = coil_locate(-x,y,-z)
		
		r1 = rsquare(loc1[0],loc1[1],loc1[2])
		r2 = rsquare(loc2[0],loc2[1],loc2[2])
		r3 = rsquare(loc3[0],loc3[1],loc3[2])
		r4 = rsquare(loc4[0],loc4[1],loc4[2])
		
		#print ( r )
		#print ("+++++++")
		
		gamma1= loc1[0]/r1
		gamma2= loc2[0]/r2
		gamma3= loc3[0]/r3
		gamma4= loc4[0]/r4
		
		l=1
		
		while l <= 3:
			s1 = sensitivity_coil(l,r1,loc1[2],gamma1)
			s2 = sensitivity_coil(l,r2,loc2[2],gamma2)
			s3 = sensitivity_coil(l,r3,loc3[2],gamma3)
			s4 = sensitivity_coil(l,r4,loc4[2],gamma4)
			s = s + s1 + s2 + s3 + s4
			l+=1
		
		point.append(s)
		
		y = y + step_size
	
	position.append(point)
	x = x + step_size

f=open("Sensitivity.dat","w")
n= 0
for i in position:
	row = ""
	j= 0 
	for m in position[n]:
		row = row + str(position[n][j])+"	"
		j+=1
	f.write (row +"\n")
	n+=1
