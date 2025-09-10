##A farmer has field which is half in circle share and rest rectangle. He needs to do fencing for entire field using barbedw wire 5 times. Circular section has radius 20m and rectangle length is 50 m and breadth is 40 m. If cost barbed wire is 32 RS/m  then calculate the total cost of fencing the field.

import math

r = 20
length = 50
breadth = 40
cost_per_m = 35
rounds = 5

perimeter = 2 * (length + breadth) + math.pi * r

total_length = perimeter * rounds 
total_cost = total_length * cost_per_m

print("Total cost of fencing:",total_cost,"Rs")