print("".center(150,"-"))
print("Welcome To KBC (Kaun Banega Crorepati)".center(150))
print()
print("Here you will need to answer 5 Questions.\nIn the end you will Receive Money Amount\nBased on your correct answers.")
print()
ques = ["Q1. Name the studio which made anime like Faith & Demon slayer","Q2. Which of the following anime is not made my studio 'mappa'."
       ,"Q3. How many country's are there in world.","Q4. What is the answer of this equation :- (7 + 8) * 5 + 7 ","Q5. Which one of the dialog is related to KBC :" ]
que = 0
for s in ques :
    print()
    print(s)
    que = que+1
    if que==2:
        print()
        print("Select from these option:\n1.JJK\n2.Hell's paradise\n3.Banana Fish\n4.AOT (season 3)")
        ans2= int(input("Answer : "))
    elif que==5:
        print()
        print("Select option:\n1.Saat lakh, pachas hazaar rupaye, isme se pachas hazaar tumhara, saat laakh humara\n2.Is answer pe tala laga diya jaye?")
        ans5 = int(input("Answer : "))
    elif que==1 :
        print()
        print("You are given no option")
        ans1 = input("Answer : ")
    elif que==3:
        print()
        print("You are given no option")
        ans3 = input("Answer : ")
    elif que==4:
        print()
        print("You are given no option")
        ans4 = input("Answer : ")
if ans1.lower() == "ufotable":
    a1a = 10000
else:
    a1a = 0
if ans2 == 4:
    a2a = 50000
else:
    a2a = 0
if ans3 == "195":
    a3a = 100000
else:
    a3a = 0
if ans4 == "82" :
    a4a = 150000
else:
    a4a = 0
if ans5 == 2:
    a5a = 500000 
else:
    a5a = 0
print()
print("You won an amount of : ₹",a1a+a2a+a3a+a4a+a5a)