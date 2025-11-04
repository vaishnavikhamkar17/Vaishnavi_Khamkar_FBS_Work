##Python program to count number of lowercase characters in a string.

def count_lowercase(string):
    count = 0
    for ch in string:
        if ch.islower():
            count += 1
    return count

s = input("Enter s strings:")
print("Number of lowercase characters:", count_lowercase(s))