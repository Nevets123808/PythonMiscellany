import random
import math

dice_size = 120e6
iterations = 1000
count = 0
for i in range(iterations):
    x = math.ceil(random.random()*dice_size)
    y = math.ceil(random.random()*dice_size)
    if (math.gcd(x,y)==1):
        count+=1

prob = count/iterations
estimate = math.sqrt(6/prob)
print(estimate)
