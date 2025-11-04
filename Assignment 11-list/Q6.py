#python program to find union of two lists.
def union_lists(list1,list2):
    union = list1.copy()

    for item in list2:
        if item not in union:
            union.append(item)
    return union

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = union_lists(list1, list2)
print("Union of two lists:", result)
