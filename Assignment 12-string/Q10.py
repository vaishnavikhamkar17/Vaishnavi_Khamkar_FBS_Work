##Python program to Take in Two strings and Display the Larger string without using built in functions.

def larger_string(str1,str2):
    len1 = 0
    len2 = 0

    for _ in str1:
        len1 += 1

    for _ in str2:
        len2 += 1

    if len1 > len2:
        return str1
    elif len2 > len2:
        return str2
    else:
        return "Both strings are of equal length."
    
string1 = input("Enter first string:")
string2 = input("Enter second string:")

result = larger_string(string1,string2)
print("Larger string is:",result)
    



