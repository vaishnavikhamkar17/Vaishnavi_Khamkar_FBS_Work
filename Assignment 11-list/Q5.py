#python program to sort alist according to the length of the elements within a list.

def sort_by_length(li):
    return sorted(li,key=len)

li = ["apple","kiwi","banana","fig","orange"]

sorted_list = sort_by_length(li)
print("List sorted by length:",sorted_list)