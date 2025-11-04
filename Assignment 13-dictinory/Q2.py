##python progran to concatenate two dictionaries into one

def concatenate_dicts(dict1,dict2):

    result = dict1.copy()
    result.update(dict2)
    return result

dict1 = {}
dict2 = {}

n1 = int(input("Enter number of items in first dictionary:"))
for i in range(n1):
    key = input(f"Enter key {i+1} for dict1:")
    value = input(f"Enter value for '{key}':")
    dict1[key] = value

n2 = int(input("\nEnter number of items in second dictionary:"))
for i in range(n2):
    key = input(f"Enter key {i+1} for dict2:")
    value = input(f"Enter value for '{key}':")
    dict2[key] = value 

merged_dict =concatenate_dicts(dict1,dict2)

print("\nFirst dictionary:",dict1)
print("\nSecond dictionary:",dict2)
print("Concatenated dictionary:",merged_dict)