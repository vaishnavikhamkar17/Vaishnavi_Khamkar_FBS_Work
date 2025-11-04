#WAp to check if entered year is leap or not.

def is_leap_year(n):
    if(n % 4 == 0 and n % 100 != 0 or n % 400 == 0):
        return True
    else:
        return False
    
n = int(input("Enter a year:"))
if(is_leap_year(n)):
    print(n, " is a leap year.")
else:
    print(n, " is not a leap year.")