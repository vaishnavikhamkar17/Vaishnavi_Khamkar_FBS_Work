## WAP to create a duplicate of an exisitng list. It should not point to same list.

def duplicate_list(li):
    return li.copy()

original = [1, 2, 3, 4, 5, 6]
duplicate = duplicate_list(original)

print("Original list:",original)
print("Duplicate list:",duplicate)

print("Are both lists same objets?",original is duplicate)