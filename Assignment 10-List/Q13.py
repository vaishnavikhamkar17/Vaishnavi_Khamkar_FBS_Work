##WAP to print list after removing even numbers

def remove_even(li):
    return [x for x in li if(x % 2 != 0)]

numbers = [10, 15, 22, 33, 65, 44, 76]
print("Original list:",numbers)
new_list = remove_even(numbers)
print("List after removing even numbers :",new_list)