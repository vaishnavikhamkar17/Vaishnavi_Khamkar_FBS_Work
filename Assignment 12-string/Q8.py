##python program to Remove the characters of Odd Index Values in a string

def remove_odd_inedx_chars(s):
    result = ""
    for i in range(len(s)):
        if(i % 2 == 0):
            result += s[i]
    return result

user_input = input("ENter a string:")
output = remove_odd_inedx_chars(user_input)
print("String after removing the characters o odd index values in a string:",output)