##Python program to Add a key-Value pair to the Dictionary.

def add_key_value_pair(d,key,value):
    d[key] = value
    return d

my_dict = {}
n = int(input("Enter number of key-value pairs you want to add:"))

for i in range(n):
    key = input(f"Enter key {i+1}:")
    value = input(f"Enter value for '{key}':")

    my_dict = add_key_value_pair(my_dict,key,value)

print("\nUpadted Dictionary:")
print(my_dict)
