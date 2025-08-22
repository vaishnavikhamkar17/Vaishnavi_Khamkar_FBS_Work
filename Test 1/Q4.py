area_one_wall = int(input("Enter the area of one wall:"))
interior_cost = int(input("Enter the interior cost:"))
exterior_cost = int(input("Enter the exterior cost:"))

total_interior_area = area_one_wall * 8
total_exterior_area = area_one_wall * 7

total_interior_cost = total_interior_area * interior_cost
total_exterior_cost = total_exterior_area * exterior_cost

print(f'Total interior painting cost:',total_interior_cost)
print(f'Total exterior painting cost:',total_exterior_cost)

