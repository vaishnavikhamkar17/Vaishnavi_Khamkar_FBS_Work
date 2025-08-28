## WAP to prompt user enter userid and password. After verifying user and password display a 4 digit random number and  ask user to enter the same. If user enters the same numbers than show him success message otherwise failed.(Something like captcha.)

userid = "admin"
password = 1234

user = input("Enter the userid:")
pwd = int(input("Enter the password:"))

captcha = 9965
print(f"Captcha is:",captcha)
user_captcha = int(input("Enter the captcha:"))

if(user == userid and password == pwd):
    if(user_captcha == captcha):
        print("Login successfully.")
    else:
        print("Captcha failed.")
else:
    print("Invalid password or userid.")
    
    

