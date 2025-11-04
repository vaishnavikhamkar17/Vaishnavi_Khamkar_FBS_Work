##Python program to find larger string without using built-in-functions.

def larger_string(str1,str2):
    len1 = 0
    len2 = 0

    for _ in str1:
        len1 += 1

    for _ in str2:
        len2 += 1

    if len1 > len2:
        return str1
    elif len2 > len1:
        return str2
    else:
        return "Both strings are of equal length."
    
s1 = input("Enter first string:")
s2 = input("Enter second string:")

print("\nLarger string is:", larger_string(s1,s2))