## WAP to check if user has entered correct userid and password.

userid ="admin"
password = 12345

user = input("Enter the userid:")
pwd = int(input("Enter the password:"))

if(user == userid and password == pwd):
    print("Login successfully.")
else:
    print("Invalid password or userid.")
