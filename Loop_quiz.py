#Print * * * * * * * * * *
for j in range(1,10):
    for k in range (10-j):
        print (end="  ")
    for i in range(j):
        print(i+1, end = " ")
    for i in range(j-1,0,-1):
        print (i, end = " ")
    print("\n")
    
for j in range (1,10):
    for k in range (j+1):
        print (end="  ")
    for i in range(9-j):
        print (i+1, end=" ")
    for i in range (8-j,0,-1):
        print (i, end=" ")
    print("\n")
