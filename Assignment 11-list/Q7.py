#python program to find intersection of two lists.

def intersection(list1, list2):
    result = []

    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

common = intersection(list1,list2)

print("List 1:",list1)
print("List 2:",list2)
print("Intersection:",common)

