import random

def merge(x):
    if(len(x) == 1): return x
    y=[]
    z=[]
    m=[]
    
    for i in range(round(len(x)/2)):
        y.append(x[i])
    for j in range(round(len(x)/2),len(x)):
        z.append(x[j])
    
    k = merge(y)
    #print("k ",k)
    l = merge(z)
    #print("z ",z)
    
    while(len(k) != 0 or len(l) != 0):
        if(len(k) == 0):
            m.extend(l)
            l = []
        elif(len(l) == 0):
            m.extend(k)
            k = []
        elif (k[0] < l[0]):
            m.append(k[0])
            k.pop(0)
        elif (k[0] >= l[0]):
            m.append(l[0])
            l.pop(0)

        
    #print("m= ",m,"\n")    
    return m
x =[]        
for i in range(1000):
    x.append(random.randrange(100))
print("x = ", x)
x = merge(x)
print(x)

        
