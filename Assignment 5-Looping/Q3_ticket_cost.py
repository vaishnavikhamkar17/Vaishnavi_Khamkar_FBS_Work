#Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.

num = int(input("Enter number of passengers:"))
per_ticket_cost = int(input("Enter per ticket cost:"))

total = 0

for i in range(1 , num+1):
    age = int(input(f"Enter age of passenger{i}:"))

    if(age < 12):
        total += per_ticket_cost * 0.7
    elif(age > 59):
        total += per_ticket_cost *0.5
    else:
        total += per_ticket_cost

print("Total ticket cost:",total)


