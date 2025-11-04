#python program to Take in a String and Replace every blank space with Hypen.

def repalce_space_with_hyphen(s):
    new_string = " "
    for char in s:

        if char == " ":
            new_string += "_"
        else:
            new_string += char
            
    return new_string

user_input = input("Enter a string:")
result = repalce_space_with_hyphen(user_input)
print("String after replacing spaces with hyphens :",result)