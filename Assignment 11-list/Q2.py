# python program to merge two list and sort it.

n1 = int(input("Enter number of elements in first list:"))
li1 = [int(input("Enter element {i + 1} for list1:"))
for i in range(n1)]

n2 = int(input("Enter number of elements in second list:"))
li2= [int(input("Enter element {i + 1} for list2:"))
      for i in range(n1)]

merged_list = li1 + li2

merged_list.sort()

print("First List:",li1)
print("Second List:",li2)
print("Merged and sorted list:",merged_list)
