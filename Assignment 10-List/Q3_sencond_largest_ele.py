#WAP to find second largest element in list.
def second_largest(li):
    li = list(set(li))

    li.sort()
    
    if (len(li)<2):
        return None
    return li[-2]

numbers = [12, 45, 65, 34, 23, 78]
print("Second largest element in list is:",second_largest(numbers))
