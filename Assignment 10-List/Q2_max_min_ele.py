##WAp  to find maximun and minimum element in a list.

def find_max_min(li):
    maximum = max(li)
    minimum = min(li)
    return maximum , minimum

li =[45, 23 ,89, 56, 34 , 77]
max_num , min_num = find_max_min(li)

print("Maximum number:",max_num)
print("Minimum number:",min_num)
