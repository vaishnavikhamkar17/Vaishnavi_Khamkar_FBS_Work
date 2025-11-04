## WAP to put even and odd elements of a list ino two diferent lists.

def seprate_even_odd(li):
    even_li = [x for x in li if(x % 2 == 0)]
    odd_li = [x for x in li if(x % 2 != 0)]

    return even_li, odd_li

n = int(input("Enter number of elements:"))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i + 1} :"))
    numbers.append(num)

evens,odds = seprate_even_odd(numbers)
print("Original list:",numbers)
print("Even list:",evens)
print("Odd list:",odds)