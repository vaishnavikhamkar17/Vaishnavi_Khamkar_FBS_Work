##WAP to accept a year from user and check if it is a leap year or not.

year = int(input("Enter a year:"))

if(year % 4 != 0):
    print(year," is not a leap year")
elif(year % 100 != 0):
    print(year ,"is a leap year")
elif(year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year , "is not a leap year")