## Accept a number from user and check if this element is present in th list or not. Also tell many time it is present in alist.

def ele_in_list(li,element):
    count = li.count(element)
    if(count > 0):
        print(f"{element} is present in the list {count} times.")
    else:
        print(f"{element} is not present in the list.")

numbers = [12,43,76,43,98,43,90,43]
num = int(input("Enter a number to check :"))
ele_in_list(numbers, num)

