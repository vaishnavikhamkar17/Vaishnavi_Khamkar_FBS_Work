## Accept age of five people and also per person ticket amount  and then calculate total amount to ticket to travel for all of them based n following condition: a. children below 12 = 30% discount b. senior citizen (above 59) = 50% discount c. others need to pay 

ticket = int(input("Enter the per person amount of ticket:"))

#person1
age1 = int(input("Enter age of person:"))
if(age1 < 12):
    amt1 = ticket * 0.70 #30%
elif(age1 > 59):
    amt1 = ticket * 0.50  #50%
else:
    amt1 = ticket

#person2
age2 = int(input("Enter age of person:"))
if(age2 < 12):
    amt2 = ticket * 0.70 #30%
elif(age2 > 59):
    amt2 = ticket * 0.50  #50%
else:
    amt2 = ticket
   
#person3
age3 = int(input("Enter age of person:"))
if(age3 < 12):
    amt3 = ticket * 0.70 #30%
elif(age3 > 59):
    amt3 = ticket * 0.50  #50%
else:
    amt3 = ticket

#person4
age4 = int(input("Enter age of person:"))
if(age4 < 12):
    amt4 = ticket * 0.70 #30%
elif(age4 > 59):
    amt4 = ticket * 0.50  #50%
else:
    amt4 = ticket

#person5
age5 = int(input("Enter age of person:"))
if(age5 < 12):
    amt5 = ticket * 0.70 #30%
elif(age5 > 59):
    amt5 = ticket * 0.50  #50%
else:
    amt5 = ticket

Total_amount = amt1 + amt2 + amt3 + amt4 + amt5

print("Total amount:",Total_amount)


