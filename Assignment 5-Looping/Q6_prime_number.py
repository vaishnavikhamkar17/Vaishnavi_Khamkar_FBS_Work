# WAp to print prime number betwwen 1to 100
print("Prime numbers between 1 to 100 are:")

i = 1
for num in range(2, 100+1):
   is_prime = True
   for i in range(2, int(num ** 0.5) + 1):
      if(num % i == 0):
         is_prime = False
         break
   if(is_prime):
      print(num, end=" ")