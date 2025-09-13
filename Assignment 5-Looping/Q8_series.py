# 1!+2!=3!+4!+....n!

n = int(input("Enter n :"))

s = 0
fact = 1

for i in range(1, n + 1):
    fact += i
    s += fact

print("Sum=",s)

#N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

n = int(input("ENter a number:"))
square = 1
for i in range(2):
    square *= n
power = 1
for i in range(n):
    power *= n

s = n + square + power

print("Series Result = ",s)

#Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter number of terms:"))

sum_gp = 0
term = 1

for i in range(n):
    sum_gp += term
    term *= 2

print("Sum of series =",sum_gp)

#S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter value of a:"))
s = 0

for n in range(1,11):
    s +=(a ** n) / n
print("Sum of series :",s)

# x - x2/3 + x3/5 - x5/7... to n terms

x = int(input("Enter value of x:"))
n = int(input("Enter number of terms:"))

s = 0
for i in range(1,n+1):
    term = ((-1) ** (i + 1)) * (x ** i) / (2 * i - 1)

print("sum of series:",s)