m1 = int(input("Enter the marks of subject1:"))
m2 = int(input("Enter the marks of subject2:"))
m3 = int(input("Enter the marks of subject3:"))
m4 = int(input("Enter the marks of subject4:"))
m5 = int(input("Enter the marks of subject5:"))

marks = m1 + m2 + m3 + m4 + m5
perc = (marks / 500) * 100
if(perc >= 70):
    print("First class")
elif(perc >= 50):
    print("Second class.")
elif(perc >= 35 ):
    print("Third class.")
else:
    print("fail.")