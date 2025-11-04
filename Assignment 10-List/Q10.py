##WAP to remove all occurrences of a given element in the list

def remove_occurences(li,element):
    return [ x for x in li if (x != element)]

numbers = [ 1, 2, 3, 4, 5, 6,7]
print("Original list :",numbers)
ele = int(input("Enter element to remove :"))

new_list = remove_occurences(numbers,ele)
print("List after removing all occurrences of",ele,".",new_list)