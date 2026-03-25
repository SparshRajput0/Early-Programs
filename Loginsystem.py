import time
print()
print("Login System".center(125,"-"))
time.sleep(0.5)
print()
print("You Have Only 3 Attempts .Enter carefully Otherwise Acount Would Be Locked")
time.sleep(0.5)
print()
print("You Can Exit From the program by typing 'exit'")
time.sleep(0.5)
username = "admin"
password = "1234"
attempt = 3
while attempt >0:
    time.sleep(0.5)
    print()
    if attempt == 1:
        print("You have 1 attempt left")
    else:
        print(f"You have {attempt} attempts left")
    print()
    usernameinput = input("Enter Username: ")
    if usernameinput.lower() == "exit":   
        break
    time.sleep(0.25)
    print()
    passwordinput = input("Enter password: ")
    if passwordinput.lower() == "exit":
        break
    time.sleep(0.25)
    if usernameinput==username and passwordinput ==password:
        time.sleep(0.5)
        print("Login Successful ✅")
        time.sleep(0.25)
        print()
        print("Please Wait We Are Loading Site.")
        break
    else:
        attempt-=1
        if usernameinput!=username and passwordinput==password:
            print()
            time.sleep(0.5)
            print("Username is Wrong")
            continue
        if passwordinput!=password and usernameinput==username:
            print()
            time.sleep(0.5)
            print("Password is Wrong")
            continue
        else:
            print()
            time.sleep(0.5)
            print("Invalid credentials ❌")
            print()
            print("Please try again")
            continue
if attempt == 0:
    print()
    time.sleep(0.5)
    print("Account Locked ❌")
    print()
    time.sleep(0.5)
    print("Sorry, But Your Account is Locked")
print()