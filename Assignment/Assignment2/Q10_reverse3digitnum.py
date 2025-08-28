## WAP to reverse three digit number.

num = int(input("Enter a three digit number:"))

d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10

rev = (d3 * 100) + (d2 * 10) + d1

print("Reversed number", rev)
