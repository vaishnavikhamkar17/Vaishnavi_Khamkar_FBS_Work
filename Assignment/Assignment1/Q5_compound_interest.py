## WAP to enter P ,T , R and calculate compound interest.

P = int(input("Enter the principle:"))
R = int(input("Enter the rate:"))
T = int(input("Enter the time:"))

Compound_Interest = (P * (1 + R/100) ** T )- P

print(f"Compound Interest is:{Compound_Interest}")