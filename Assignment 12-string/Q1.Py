#Python Program to Replace all Occurrences of 'a' with $ in a String.

def replace_a_with_doller(s):
    return s.replace('a','$')

text = input("Enter a string:")
modified_text = replace_a_with_doller(text)

print("Modified string:",modified_text)