import time

def add(a, b):
    result = a + b
    return result
def subtract(a, b):
    result = a - b
    return result
def divide(a, b):
    if b==0:
        return None
    result = a / b
    return result
def multiply(a, b):
    result = a * b
    return result
def floor_divide(a, b):
    if b==0:
        return None
    result = a // b
    return result
def modulus(a, b):
    if b==0:
        return None
    result = a % b
    return result
def exponent(a, b):
    result = a ** b
    return result
print()
print()
print("Welcome to the basic calculator".center(125,"-"))
time.sleep(2)
print()
print("Here you can perform basic calculations such as:")
print()
time.sleep(2)
print("Addition,Subtraction,Multiplication,Division,Floor divition,Modulus/Remainder And Exponents")
time.sleep(2)
while True:
    print()
    print()
    print("Select From these option")
    time.sleep(1)
    print()
    print("1.Addition")
    print("2.Subtraction")
    print("3.Divion")
    print("4.Multiplication")
    print("5.Floor divition")
    print("6.Modulus/Remainder")
    print("7.Exponent")
    print("8.Exit")
    print()
    time.sleep(1)
    cho=input("Type option: ")
    print()
    if cho.lower() == "exit" or cho == "8":
        break
    time.sleep(0.5)
    a=input("Enter First Number: ")
    if a.lower() == "exit":
        break
    if not a.isdigit():
        print("Invalid input ❌")
        continue
    a =int(a)
    time.sleep(0.5)
    print()
    b=input("Enter Second Number: ")
    if b.lower()=="exit":
        break
    if not b.isdigit():
        print("Invalid input ❌")
        continue
    b=int(b)
    time.sleep(0.5)
    print()
    print("calculating...")
    time.sleep(1.5)
    print()
    print()
    if cho=="1":
        print(f"Addition = {add(a, b)}")

    elif cho=="2":
        print(f"Subtraction = {subtract(a, b)}")

    elif cho=="3":
        result = divide(a, b)
        if result == None:
            print("Can't divide by zero ❌")
        else:
            print(f"Division = {result}")

    elif cho=="4":
        print(f"Multiplication = {multiply(a, b)}")

    elif cho=="5": 
        result = floor_divide(a, b)
        if result == None:
            print("Can't divide by zero ❌")
        else:
            print(f"Floor Division = {result}")

    elif cho=="6":
        result = modulus(a, b)
        if result == None:
            print("Can't divide by zero ❌")
        else:
            print(f"Modulus/Remainder = {result} ")

    elif cho=="7":
        print(f"Exponent = {exponent(a, b)}")

    else:
        print("Invalid option ❌") 
    print()
    y=input("Do you want to repeat program \nType yes/no : ")
    print()
    if y == "no":
        break
time.sleep(0.75)
print()
print(" THANK YOU ".center(150,"-"))
print()
print()