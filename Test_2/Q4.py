##WAP to calculate the total cost of painting . The interrior of building with four equal sized walls.
length = int(input("Enter the length of wall(in meters):"))
breadth = int(input("Enter the breadth of wall(in meters):"))
height = int(input("Enter the height of wall(in meters):"))

cost_per_m = int(input("Enter cost of painting in square meter:"))

if(length > 0 and breadth > 0 and height > 0 and cost_per_m > 0):
    area = 2 * height * (length + breadth)
    total_cost = area * cost_per_m
    print("Total painting cost = Rs.",total_cost)
else:
    print("Invalid input!")