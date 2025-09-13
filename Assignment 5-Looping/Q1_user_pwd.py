#Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.

userid = "admin"
password = "12345"

for attempt in range(1 , 4):
    user = input("Enter the userid:")
    pwd = input("Enter the password:")

    if(user == userid and pwd == password):
        print("Login Successful")
        break
    else:
        print(f"Invalid credentials. Attempts left:{3 - attempt}")

else:
    print("Login failed.Too many Attempts.")