## WAP to create a new list from existing list which contains cube of each number of list.

def cube_list(n):
    return [x ** 3 for x in n]

numbers = [1, 2, 3, 4, 5, 6]
print("Original list:",numbers)

cubes = cube_list(numbers)
print("List of cubes:",cubes)