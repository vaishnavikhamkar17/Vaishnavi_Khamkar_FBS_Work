#WAP to check if entered number id palindrome or not.

def is_palindrome(num):
    s = str(num)
    if(s == s[::-1]):
        return True
    else:
        return False
    
data = input("Enter a number or word :")
if(is_palindrome(data)):
    print(f"{data} is a palindrome.")
else:
    print(f"{data} is not a palindrome.")