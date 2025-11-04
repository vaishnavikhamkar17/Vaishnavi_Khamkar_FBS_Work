#Python program to check  if a given key Exists in a Dictionary or not

def check_key_exists(d,key):
    if key in d:
        print(f"key '{key}' exists in th dictionary.")
    else:
        print(f"key '{key}' does NOT exists in th dictionary.")

my_dict = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
key = input("Enter the key to check:")

check_key_exists(my_dict,key)

    