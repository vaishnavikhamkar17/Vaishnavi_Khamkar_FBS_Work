## WAP to accept 3 digit number. if first digit is double of second digit and half of second digit then display " yes"

num = int(input("Enter a 3 digit number: "))

first = num // 100
second = (num // 10) % 10
third = num % 10

if(first == 2 * second and first == third / 2):
    print("Yes, you have done it.")
else:
    print("Please try next time.")