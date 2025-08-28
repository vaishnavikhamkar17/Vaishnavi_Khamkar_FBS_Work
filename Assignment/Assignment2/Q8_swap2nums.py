#### swap two numbers using third variable
x = int(input('Enter the number 1:'))
y = int(input('Enter the number 2:'))

z = x
x = y
y = z

print(f'After swapping - x:{x} ,y:{y}')