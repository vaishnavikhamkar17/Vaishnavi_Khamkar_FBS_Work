##Python program to count number of digits and letters in string.

def count_digits_letters(string):
    digits = 0
    letters = 0

    for ch in string:
        if ch.isdigit():
            digits += 1
        elif ch.isalpha():
            letters += 1
    return digits,letters

s = input("Enter a string:")
d,l = count_digits_letters(s)
print("Number of digits:" ,d)
print("Number of letters:" ,l)