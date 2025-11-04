#python program to sort the list according to the second element in sublist

def sort_by_second_element(li):
    return sorted(li,key=lambda x:x[1])

list = [[1,3],[2,1],[4,2],[3,5]]

sorted_list = sort_by_second_element(list)
print("Sorted list:",sorted_list)