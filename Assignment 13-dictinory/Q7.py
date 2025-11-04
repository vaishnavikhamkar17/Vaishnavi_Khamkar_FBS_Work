##Python program to remove the given key from a dictionary

def remove_key(d, key):
    if key in id:
        del d[key]
        print(f"key '{key}' removed successfully.")
    else:
        print(f"key '{key}' not found in the dictionary.")
    return d

my_dict = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
key_to_remove = input("Enter the key to remove:")
updated_dict = remove_key(my_dict , key_to_remove)
print("Updated dictionary:", updated_dict)
