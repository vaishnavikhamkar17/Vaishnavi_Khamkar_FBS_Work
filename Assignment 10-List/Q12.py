##WAP to create three list of numbers, their squares and cubes.

def create_lists(n):
    numbers = list(range(1, n + 1))
    squares = [x ** 2 for x in numbers]
    cubes = [x ** 3 for x in numbers]

    return numbers,squares, cubes

n = int(input("Enter the range(n):"))

nums, sqrs, cbs = create_lists(n)
print("Numbers list :",nums)
print("Squares list :",sqrs)
print("Cubes list :",cbs)
