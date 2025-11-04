#print 1 to 100 in snakes and ladder pattern.
def snakes_and_ladders():

    num = 100
    rows = 10
    cols = 10

    for i in range(rows): #for even rows:print left to right

        if i % 2 == 0:
            for j in range(cols):
                print(f"{num - j:3}",end=" ")
        else:                                  #for odd rows:print right to left
            for j in range(cols):
                print(f"{num - (cols - 1 - j):3}",end=" ")

        num -= cols
        print()  #new line

snakes_and_ladders() #call the function
