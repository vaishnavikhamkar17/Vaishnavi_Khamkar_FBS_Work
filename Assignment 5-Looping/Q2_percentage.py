#Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.

n = int(input("Enter number of students:"))

total_percent = 0

for student in range(1, n + 1):
    print(f"Enter the marks of 5 subject:")
    total_marks = 0

    for sub in range(1,6):
        marks = int(input(f"Enter marks of subject {sub}:"))
        total_marks += marks

    percentage = total_marks / 5
    print(f"percentage of student{student}={percentage:.2f}%")
    
    total_percent += percentage
avg_percent = total_percent / n

print("Average percentage of all students=",round(avg_percent,2),"%")