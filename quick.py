import random
import time

def quick(x):
    if len(x) <= 1: return x
    index = random.randrange(0,len(x))
    pivot = x[index]
    #print (pivot)
    less = []
    more = []
    for i in x:
        if i <= pivot:
            less.append(i)
            #print("less, ", less)
        elif i > pivot:
            more.append(i)
            #print("more, ", more)
    
    #print("sort less: ",less)
    less = quick(less)
    #print("less + pivot: ", less)
    #print("sort more: ",more)
    more = quick(more)
    
   # print("less + pivot: ", less)
    y = less + more
    return y

x = []
y= []
for i in range(30):
    y.append(i)
for j in range(30):
    index = random.randrange(0,len(y))
    x.append(y[index])
    del y[index]

print(x)
time = 
x = quick(x)
print(x)
