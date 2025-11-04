#python program to sum all the items in a dictionary.

def sum_of_dict_items(d):
    return  sum (d.values())

my_dict = {'a' : 100, 'b' : 200, 'c' : 300}

total = sum_of_dict_items(my_dict)
print("Sum of all items in a dictionary:",total)