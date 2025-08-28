## WAP to check if given 3 digit number is palindrome or  not.

num = int(input("Enter the number:"))
rev = int(str(num)[::-1])

if(num == rev):
    print(num,"is a palindrome.")
else:
    print(num,"is not a palindrome.")

