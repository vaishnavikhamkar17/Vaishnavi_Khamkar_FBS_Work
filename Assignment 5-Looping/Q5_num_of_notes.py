#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount. (Use looping to optimize the problem)

amount = int(input("Enter amount:"))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
print("Minimum numbers of notes:")

for note in notes:
    if(amount >= note):
        count = amount // note

        print(note, "x" , count)
        amount %= note