## WAp to check if person  is eligible to marry or not(male age >= 21 and female age >=18)

gender = input("Enter the gender(M/F):")
age = int(input("Enter the age:"))

if(gender == "M" or gender == "m" or gender == "F" or gender == "f"):
    if(age >= 21):
       print("Eligible for marriage.")
    else:
        print("Not eligible for marriage.")
else:
    if(age >= 18):
        print("eligible for marriage.")
    else:
        print("Not eligible for Marriage.")