##Python program to replace every blank space with hyphen in a string.

def replace_space_with_hyphen(text):
    new_string = ""
    for ch in text:
        if ch == " ":
            new_string += "-"
        else:
            new_string += ch
    return new_string

string = input('Enter a string:')

result = replace_space_with_hyphen(string)
print("String after replacing blank spcae with hyphens:", result)