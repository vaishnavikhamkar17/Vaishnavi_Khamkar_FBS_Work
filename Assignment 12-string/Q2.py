#Python program to Remove the nth Index Character from a Non-Empty String.

def remove_char_at_index(s,n):
    return s[:n] + s[n+1:]     #slicing

text = input("Enter a non-empty string:")
index = int(input("Enter the index to remove:"))

if 0 <= index < len(text):
    result = remove_char_at_index(text,index)
    print("String after removal:",result)
else:
    print("Invalid index. Please enter an index between 0 and ", len(text)-1)