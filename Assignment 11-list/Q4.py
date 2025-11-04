#python program tp find second largest number in alist using bubble sort

def bubble_sort(li):
    n = len(li)
    for i in range(n-1):
        for j in range(n-1-i):
            if(li[j]>li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]
    return li

def second_largest(li):
    sorted_list = bubble_sort(li.copy())

    return sorted_list[-2]

numbers = [10, 5, 20, 8, 12]

result = second_largest(numbers)
print("Second largest number is:",result)