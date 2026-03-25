import time
def percentage(a,b,c,d,e):
    return ( a + b + c + d + e) / 5
print()    
print(" Student Report Card Generator ".center(150,"="))
time.sleep(1)
print()
print("The progrem can generate a report card based on 5 Subjects.\nIt will also give a overall grade according to the percentage.")
time.sleep(2)
print()
while True:
    exited = False
    while True:
        time.sleep(0.5)
        name = input("Enter name of student (Without space) :- ")
        if name.isalpha() == False:
            time.sleep(0.25)
            print("Invalid input ❌")
            print("Please enter a name.")
            continue
        elif name.lower()=="exit":
            exited = True
            break
        print()
        while True:
            print()
            time.sleep(0.25)
            sub1 = input("Enter Marks of Subject (1st) [0-100]:- ")
            if sub1 == "exit":
                exited = True
                print("Exited")
                break
            elif sub1.isdigit() == False:
                time.sleep(0.25)
                print("Invalid input ❌")
                print("Please enter a number.")
                print()
                continue
            elif int(sub1) >= 0 and int(sub1) <= 100:
                sub1 = int(sub1)
            else:
                time.sleep(0.25)
                print("Invalid input ❌")
                print("Enter Between 0 to 100")
                continue
            print()
            time.sleep(0.25)
            sub2 = input("Enter Marks of Subject (2nd) [0-100]:- ")
            if sub2 == "exit":
                exited = True
                print("Exited")
                break
            elif sub2.isdigit() == False:
                time.sleep(0.25)
                print("Invalid input ❌")
                print("Please enter a number.")
                time.sleep(0.25)
                print()
                continue
            elif int(sub2) >= 0 and int(sub2) <= 100:
                sub2 = int(sub2)
            else:
                time.sleep(0.25)
                print("Invalid input ❌")
                print("Enter Between 0 to 100")
                time.sleep(0.25)
                continue
            print()
            time.sleep(0.25)
            sub3 = input("Enter Marks of Subject (3rd) [0-100]:- ")
            if sub3 == "exit":
                exited = True
                print("Exited")
                break
            elif sub3.isdigit() == False:
                time.sleep(0.25)
                print("Invalid input ❌")
                print("Please enter a number.")
                time.sleep(0.25)
                continue
            elif int(sub3) >= 0 and int(sub3) <= 100:
                sub3 = int(sub3)
            else:
                time.sleep(0.25)
                print("Invalid input ❌")
                print("Enter Between 0 to 100")
                time.sleep(0.25)
                continue
            print()
            time.sleep(0.25)
            sub4 = input("Enter Marks of Subject (4th) [0-100]:- ")
            if sub4 == "exit":
                exited = True
                print("Exited")
                break
            elif sub4.isdigit() == False:
                time.sleep(0.25)
                print("Invalid input ❌")
                print("Please enter a number.")
                time.sleep(0.25)
                continue
            elif int(sub4) >= 0 and int(sub4) <= 100:
                sub4 = int(sub4)
            else:
                time.sleep(0.25)
                print("Invalid input ❌")
                print("Enter Between 0 to 100")
                time.sleep(0.25)
                continue
            print()
            time.sleep(0.25)
            sub5 = input("Enter Marks of Subject (5th) [0-100]:- ")
            if sub5 == "exit":
                exited = True
                print("Exited")
                break
            elif sub5.isdigit() == False:
                time.sleep(0.25)
                print("Invalid input ❌")
                print("Please enter a number.")
                time.sleep(0.25)
                continue
            elif int(sub5) >= 0 and int(sub5) <= 100:
                sub5 = int(sub5)
            else:
                time.sleep(0.25)
                print("Invalid input ❌")
                print("Enter Between 0 to 100")
                time.sleep(0.25)
                continue
            time.sleep(0.25)
            break
        print()
        break
    if exited == False:
        print("Please Wait Generating . . .")
        time.sleep(1)
        print()
        print(" Report Card ".center(150,"-"))
        print()
        print(f"Name :- {name} ".center(25))
        print()
        print("Marks :".center(5))
        print()
        print(f"First Subject  -  {sub1}")
        print()
        print(f"Second Subject -  {sub2}")
        print()
        print(f"Third Subject  -  {sub3}")
        print()
        print(f"Fourth Subject -  {sub4}")
        print()
        print(f"Fifth Subject  -  {sub5}")
        print()
        print("Total :- ",sub1+sub2+sub3+sub4+sub5)
        print()
        print("Percentage = ",percentage(sub1,sub2,sub3,sub4,sub5)," %")
        print()
        g = percentage(sub1,sub2,sub3,sub4,sub5)
        if g >= 90:
            print("Grade : A+")
        elif g < 90 and g >= 75:
            print("Grade : A")
        elif g < 75 and g >= 60:
            print("Grade : B")
        elif g < 60 and g >=45:
            print("Grade : C")
        else:
            print("Grade : F (Fail)")
        print()
        print("".center(150,"-"))
        print()
        time.sleep(0.25)
        yn = input("Do you want to calculate Another (yes/no): ")
        if yn == "yes":
            continue
        elif yn == "no" or yn.lower() == "exit":
            break
    print()
    break
time.sleep(0.25)
print(" Thank You ".center(150,"="))