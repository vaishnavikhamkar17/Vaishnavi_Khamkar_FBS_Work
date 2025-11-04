#WAP to find print the following fibonacci series 
# 1 1 2 3 5 8 n terms
def fibo_series(n):
    a , b = 1 , 1
    print(a , b, end=" ")
    for i in range(3 , n + 1):
        c = a + b
        print(c, end=" ")
        a , b = b , c
n = int(input("Enter a number of terms:"))
if n == 1:
    print(1)
else:
    fibo_series(n)

   