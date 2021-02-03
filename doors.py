

#define how many doors
number = 30

#loop for different number of states
for n in range(2,11):

    doors = []
    #Create one hundred open doors.
    for x in range(number):
        doors.append(0)

    #change every ith door
    for i in range(1,number+1):
        j = i - 1
        while j <= (number-1):
            doors[j]=(doors[j]+1)%n
            j= j + i
    print(n, " = ", doors)
        
