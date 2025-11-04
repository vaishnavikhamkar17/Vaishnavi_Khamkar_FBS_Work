#Python program to Form a New String where the First Character and the Last Character have been Exchanged

def exchange_first_last(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]

user_input = input("Enter a string:")
new_string = exchange_first_last(user_input)
print("New string after exchanging first and last character:",new_string)