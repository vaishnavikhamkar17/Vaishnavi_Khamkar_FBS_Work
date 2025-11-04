##WAP tp print all numbers  which are divisible by  m and n in the list.

def divisible_by_m_n(li,m,n):
    return [x for x in li if(x % m == 0 and x % n == 0)]

li = [12,18,24,65,78,98,54]
print("Original list:")

m = int(input("Enter value of m:"))
n = int(input("Enter value of n:"))

result = divisible_by_m_n(li,m,n)
print(f"Numbers divisible by {m} and {n} are :",result)