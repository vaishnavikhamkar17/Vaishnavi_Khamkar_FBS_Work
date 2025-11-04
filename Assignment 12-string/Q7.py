###Python program to calculate the length of a string without using library functions

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

user_input = input("ENter a string:")
length = string_length(user_input)
print("Length of the string is:",length)    