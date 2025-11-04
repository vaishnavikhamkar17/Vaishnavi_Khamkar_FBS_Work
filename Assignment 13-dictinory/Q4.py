#Python ptogram to generate a dictionary that contains numbers (between 1 and n) in the form(x, x*x*x).

def generate_dict(n):
    d = {}
    for x in range(1, n+1):
        d[x] = x ** 3
    return d
n = int(input("Enter a number:"))
result = generate_dict(n)
print("Generated dictionary:",result)