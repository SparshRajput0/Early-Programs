import time
print()
print()
z=input("Click Enter To Activate Program")
print()
print()
text=("Basic program for good morning messages")
print()
print()
time.sleep(0.25)
print(text.title().center(125))
t=time.strftime("= %H : %M : %S")
print("Current Time ", t)
print()
time.sleep(0.25)
name=input("Enter your name : ")
print()
print()
h=int(time.strftime("%H"))
if h < 12 :
    print("Good Morning",name.title())
    
elif h < 17:
    print("Good Afternoon",name.title())
elif h < 20:
    print("Good Evening",name.title())
else:
    print("Good Night",name.title())
print()
print()
