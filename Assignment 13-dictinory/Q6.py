##python program to multiply all the items in adictionary.

def multiply_dictionary_items(d):
    result = 1
    for value in d.values():
        result *= value
    return result

my_dict = {'a' : 2, 'b' : 3, 'c' : 4}
product = multiply_dictionary_items(my_dict)
print("Product of all items in the dictionary:", product)