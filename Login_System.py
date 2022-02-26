import time
username=input("Enter the user name: ")
password=input("Enter the password: ")
print("Your account has created succesfully")

username2=input("Enter the user name to login: ")
password2=input("Enter the password to login: ")
if username==username2 and password==password2:
    print("Wait a minute.....checking the login details....")
    time.sleep(5)
    print("You have login to the system successfully!")
elif username!=username2 and password==password2:
    time.sleep(5)
    print("Invalid Username!!!")
elif username==username2 and password!=password2:
    print("checking login details....")
    time.sleep(5)
    print("Wrong Password")
elif username!=username2 and password!=password2:
    print("checking......")
    time.sleep(5)
    print("INVALID CREDINTIALS")